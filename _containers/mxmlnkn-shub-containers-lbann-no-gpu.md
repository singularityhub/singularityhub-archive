---
id: 7617
name: "mxmlnkn/shub-containers"
branch: "master"
tag: "lbann-no-gpu"
commit: "cb4516bd01d80733f7f7bdb65d4d99e6217d1a87"
version: "e0ce4be23adc189e625d1a59f8c32a38"
build_date: "2019-03-06T12:46:34.155Z"
size_mb: 621
size: 208908319
sif: "https://datasets.datalad.org/shub/mxmlnkn/shub-containers/lbann-no-gpu/2019-03-06-cb4516bd-e0ce4be2/e0ce4be23adc189e625d1a59f8c32a38.simg"
url: https://datasets.datalad.org/shub/mxmlnkn/shub-containers/lbann-no-gpu/2019-03-06-cb4516bd-e0ce4be2/
recipe: https://datasets.datalad.org/shub/mxmlnkn/shub-containers/lbann-no-gpu/2019-03-06-cb4516bd-e0ce4be2/Singularity
collection: mxmlnkn/shub-containers
---

# mxmlnkn/shub-containers:lbann-no-gpu

```bash
$ singularity pull shub://mxmlnkn/shub-containers:lbann-no-gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:buster-slim

%environment
    # elevating this to /bin/bash is not possible. Therefore should on ubuntu also be runnable in /bin/dash -.-

    PREFIX='/opt/lbann'

    exportPath()
    {
        if test -d "$2"; then
            export "$1"="$2"
            printf "\e[37mExported existing path '$2' into environment variable '$1'\e[0m\n"
        else
            printf "\e[31m[Warning] '$2' is not a directory. Won't export it\e[0m\n"
        fi
    }

    add2path()
    {
        targetVar=PATH
        if test "$#" -gt 1; then
            targetVar=$1
            shift 1
        fi
        targetContent=$( eval echo \$$targetVar )
        oldContent=$targetContent

        while test "$#" -gt 0; do
            if test -d "$1"; then
                case ":$targetContent:" in
                    *:"$1":*)
                    printf "\e[37m[Info] Path '$1' already exists in \$$targetVar. Won't add it.\e[0m\n"
                    ;;
                    *)
                    targetContent=$1:$targetContent
                    ;;
                esac
            else
                printf "\e[33m[Warning] '$1' is not a directory. Won't append to \$$targetVar variable.\e[0m\n"
            fi
            shift 1
        done

        if test "${#targetContent}" -gt "${#oldContent}"; then
            export $targetVar=$targetContent
            printf "\e[37mExporting new \$$targetVar: $targetContent\e[0m\n"
        elif test "${#targetContent}" -lt "${#oldContent}"; then
            printf "\e[31m[Error] After adding paths, the variable is erroneously shorter (${#targetContent}) than before (${#oldContent})"'!'"\e[0m\n"
        fi
    }

    exportPath CEREAL_DIR "$PREFIX/cereal"
    exportPath CNPY_DIR "$PREFIX/cnpy"
    exportPath CUB_DIR "$PREFIX"/cub-*/
    exportPath HYDROGEN_DIR "$PREFIX/Elemental"

    exportPath LBANN_DIR "$PREFIX/lbann"
    if test -d "$LBANN_DIR"; then
        add2path 'PATH' "$LBANN_DIR/bin"
        add2path 'CMAKE_PREFIX_PATH' "$LBANN_DIR"
        add2path 'LIBRARY_PATH' "$LBANN_DIR/lib"
        add2path 'LD_LIBRARY_PATH' "$LBANN_DIR/lib"
    fi

    add2path 'CMAKE_PREFIX_PATH' "$OPENCV_DIR" "$HYDROGEN_DIR"

%post
    unzip(){ python -c "from zipfile import PyZipFile; PyZipFile( '''$1''' ).extractall()"; }

    remoteExtract()
    {
        remoteExtract_ext="$( printf '%s' "$1" | sed 's/\?.*//; s/.*\.//; s|.*|\L&|;' )"
        remoteExtract_iTry=5
        remoteExtract_wgetCmd='wget -q -O- --retry-connrefused --timeout=5 --tries=5 --waitretry=5 --read-timeout=20'

        while test "$remoteExtract_iTry" -gt 0; do
            remoteExtract_iTry=$(( remoteExtract_iTry - 1 ))

            case "$remoteExtract_ext" in
                tgz|gz) compression=--gzip ;;
                xz) compression=--xz ;;
                tbz2|bz2) compression=--bzip2 ;;
            esac

            if test "$remoteExtract_ext" = "zip"; then
                remoteExtract_tmpFile="$( mktemp )" &&
                $remoteExtract_wgetCmd "$1" > "$remoteExtract_tmpFile" &&
                unzip "$remoteExtract_tmpFile" &&
                rm "$remoteExtract_tmpFile"
            else
                $remoteExtract_wgetCmd "$1" | tar -x $compression
            fi &&
            break
        done
    }

    setupCub()
    {
        cd -- "$PREFIX" &&
        if ! test -d cub-*; then
            remoteExtract 'https://github.com/NVlabs/cub/archive/v1.8.0.tar.gz'
        fi &&
        cd -- cub-* && export CUB_DIR="$( pwd )"
    }

    setupCereal()
    {
        export CEREAL_DIR="$PREFIX"/cereal &&
        if ! test -d "$CEREAL_DIR"; then
            cd -- "$PREFIX/src" &&
            remoteExtract 'https://github.com/USCiLab/cereal/archive/v1.2.2.tar.gz' &&
            cd cereal-* && mkdir -p build && cd build &&
            cmake -Wno-dev -DCMAKE_INSTALL_PREFIX="$PREFIX"/cereal -DJUST_INSTALL_CEREAL=ON .. &&
            make -j "$( nproc )" install
        fi
    }

    setupCnpy()
    {
        export CNPY_DIR="$PREFIX"/cnpy &&
        if ! test -d "$CNPY_DIR"; then
            cd -- "$PREFIX/src" && remoteExtract 'https://github.com/rogersce/cnpy/archive/4e8810b1a8637695171ed346ce68f6984e585ef4.zip' &&
            cd -- cnpy-* && mkdir -p build && cd build &&
            cmake -Wno-dev -DCMAKE_INSTALL_PREFIX="$CNPY_DIR" .. && make -j "$( nproc )" install
        fi
    }

    buildHydrogen()
    {
        # Needs at least CUDA 7.5 because it uses cuda_fp16.h even though Hydrogen_ENABLE_HALF=OFF Oo
        # Need a commit higher than release 1.1.0 or else the version check when bulding LBANN will fail
        cd -- "$PREFIX/src" &&
        remoteExtract 'https://github.com/LLNL/Elemental/archive/6d4bc32515087ed7c8c1dd2687dd2cc771c139d3.zip' &&
        cd Elemental-* && mkdir -p build && cd build &&
        cmake -Wno-dev                               \
              -DCMAKE_BUILD_TYPE=Release             \
              -DCMAKE_INSTALL_PREFIX="$HYDROGEN_DIR" \
              -DCMAKE_LIBRARY_PATH="$LIBRARY_PATH"   \
              -DHydrogen_USE_64BIT_INTS=ON           \
              -DHydrogen_ENABLE_OPENMP=ON            \
              -DBUILD_SHARED_LIBS=ON                 \
              -DHydrogen_ENABLE_ALUMINUM=OFF         \
              .. &&
        make -j "$( nproc )" VERBOSE=1 install
    }

    buildOpenCV()
    {
        cd -- "$PREFIX/src" && remoteExtract 'https://github.com/opencv/opencv/archive/3.4.3.tar.gz' &&
        cd opencv-* && mkdir -p build && cd build &&
        cmake -Wno-dev                                      \
              -DCMAKE_BUILD_TYPE=Release                    \
              -DCMAKE_INSTALL_PREFIX="$OPENCV_DIR"          \
              -DWITH_JPEG=ON                                \
              -DWITH_PNG=ON                                 \
              -DWITH_TIFF=ON                                \
              -DWITH_CUDA=OFF                               \
              -DWITH_JASPER=OFF                             \
              -DBUILD_SHARED_LIBS=ON                        \
              -DBUILD_JAVA=OFF                              \
              -DBUILD_opencv_calib3d=OFF                    \
              -DBUILD_opencv_cuda=OFF                       \
              -DBUILD_opencv_dnn=OFF                        \
              -DBUILD_opencv_features2d=OFF                 \
              -DBUILD_opencv_flann=OFF                      \
              -DBUILD_opencv_java=OFF                       \
              -DBUILD_opencv_java_bindings_generator=OFF    \
              -DBUILD_opencv_python_bindings_generator=OFF  \
              -DBUILD_opencv_ml=OFF                         \
              -DBUILD_opencv_python2=OFF                    \
              -DBUILD_opencv_python3=OFF                    \
              -DBUILD_opencv_stitching=OFF                  \
              -DBUILD_opencv_ts=OFF                         \
              -DBUILD_opencv_superres=OFF                   \
              -DBUILD_opencv_videoio=OFF                    \
              -DBUILD_opencv_videostab=OFF                  \
              .. &&
        make -j "$( nproc )" install
    }

    buildLBANN()
    {
        fixLibZBug()
        {
            find . -type f -execdir  bash -c '
                if grep "g++.*libcnpy\.so" "$0" | grep -q -v " -lz"; then
                    sed -i -r "/g\+\+ .*libcnpy\.so( |$)/{ s:(libcnpy\.so |$):\1-lz : }" "$0";
                fi' {} \;
        }

        # 0.98.1 does not work for me because it hangs: https://github.com/LLNL/lbann/issues/914
        cd -- "$PREFIX/src" && remoteExtract 'https://github.com/LLNL/lbann/archive/10b84da933a7b62e63120c6f9067df17cd9ba5f3.zip' &&
        cd lbann-* && mkdir -p build && cd build &&
        cmake -Wno-dev                               \
              -DCMAKE_BUILD_TYPE=Release             \
              -DCMAKE_INSTALL_PREFIX="$PREFIX"/lbann \
              -DCMAKE_LIBRARY_PATH="$LIBRARY_PATH"   \
              -DHydrogen_DIR="$HYDROGEN_DIR"         \
              -DLBANN_WITH_ALUMINUM:BOOL=OFF         \
              -DLBANN_USE_PROTOBUF_MODULE=$( if test -f "$PROTOBUF_ROOT/lib/cmake/protobuf/protobuf-config.cmake"; then echo OFF; else echo ON; fi )  .. &&
        fixLibZBug && make -j 2 VERBOSE=1 install
        # only building with -j 2 instead of -j 4 because some VMs don't seem to have enough memory to run for compilations in parallel ...
    }

    apt-get -y update &&
    apt-get -y install --no-install-recommends \
        findutils sed grep coreutils ca-certificates tar wget cmake gcc g++ gfortran python make \
        zlib1g-dev libopenblas-dev libopenmpi-dev libprotobuf-dev protobuf-compiler liblapack-dev \
        zlib1g libopenblas-base libopenmpi3 libprotobuf17 liblapack3 libgfortran5 libstdc++6 libc6

    PREFIX='/opt/lbann'

    mkdir -p -- "$PREFIX/src"

    setupCub
    setupCereal
    setupCnpy

    HYDROGEN_DIR="$PREFIX/Elemental" &&
    buildHydrogen &&
    export CMAKE_PREFIX_PATH="$HYDROGEN_DIR:$CMAKE_PREFIX_PATH"

    OPENCV_DIR="$PREFIX/opencv" &&
    buildOpenCV &&
    export CMAKE_PREFIX_PATH="$OPENCV_DIR:$CMAKE_PREFIX_PATH"

    buildLBANN

    # Clean up for smaller image size

    apt-get -y purge \
        wget cmake g++ python make \
        zlib1g-dev libopenblas-dev libopenmpi-dev libprotobuf-dev protobuf-compiler liblapack-dev
    apt-get -y autoremove
    apt-get -y clean
    rm -rf /var/lib/apt/lists/*
    rm -rf "$PREFIX/src"

%runscript
    PREFIX='/opt/lbann'

    "$PREFIX/lbann/bin/lbann2" "$@"
```

## Collection

 - Name: [mxmlnkn/shub-containers](https://github.com/mxmlnkn/shub-containers)
 - License: None

