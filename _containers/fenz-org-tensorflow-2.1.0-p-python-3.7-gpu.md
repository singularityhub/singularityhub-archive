---
id: 14779
name: "fenz-org/tensorflow"
branch: "master"
tag: "2.1.0-p-python-3.7-gpu"
commit: "1c308e07de97ed7b32f3c80cfaec04da0705d58c"
version: "e97ebc39d10a977be4874da4ce7d595cfd45ed53b1ae411656d2d771b8c96f90"
build_date: "2020-10-31T09:13:21.080Z"
size_mb: 2875.2578125
size: 3014926336
sif: "https://datasets.datalad.org/shub/fenz-org/tensorflow/2.1.0-p-python-3.7-gpu/2020-10-31-1c308e07-e97ebc39/e97ebc39d10a977be4874da4ce7d595cfd45ed53b1ae411656d2d771b8c96f90.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/fenz-org/tensorflow/2.1.0-p-python-3.7-gpu/2020-10-31-1c308e07-e97ebc39/
recipe: https://datasets.datalad.org/shub/fenz-org/tensorflow/2.1.0-p-python-3.7-gpu/2020-10-31-1c308e07-e97ebc39/Singularity
collection: fenz-org/tensorflow
---

# fenz-org/tensorflow:2.1.0-p-python-3.7-gpu

```bash
$ singularity pull shub://fenz-org/tensorflow:2.1.0-p-python-3.7-gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

%post
    export CUDNN_VERSION=7.6.5.32
    export CUDA_PKG_VERSION=10-1=10.1.243-1
    export CUDA_VERSION=10.1.243
    export NCCL_VERSION=2.7.8
    export NVIDIA_REQUIRE_CUDA="cuda>=10.1 brand=tesla,driver>=396,driver<397 brand=tesla,driver>=410,driver<411 brand=tesla,driver>=418,driver<419"
    export LIBRARY_PATH=/usr/local/cuda/lib64/stubs
    export LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64
    export NVIDIA_DRIVER_CAPABILITIES=compute,utility
    export PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/bin:/usr/local/sbin:/usr/sbin:/usr/bin:/sbin:/bin
    export LANG=C.UTF-8
    export LC_ALL=C.UTF-8
    export DEBIAN_FRONTEND=noninteractive

    apt-get update
    apt-get install -y --no-install-recommends \
        ca-certificates \
        netbase \
        wget
    rm -rf /var/lib/apt/lists/*

    export GPG_KEY=0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D
    export PYTHON_VERSION=3.7.7

    set -ex \
        \
        && savedAptMark="$(apt-mark showmanual)" \
        && apt-get update && apt-get install -y --no-install-recommends \
            dpkg-dev \
            gcc \
            libbluetooth-dev \
            libbz2-dev \
            libc6-dev \
            libexpat1-dev \
            libffi-dev \
            libgdbm-dev \
            liblzma-dev \
            libncursesw5-dev \
            libreadline-dev \
            libsqlite3-dev \
            libssl-dev \
            make \
            tk-dev \
            uuid-dev \
            wget \
            xz-utils \
            zlib1g-dev \
    # as of Stretch, "gpg" is no longer included by default
            $(command -v gpg > /dev/null || echo 'gnupg dirmngr') \
        \
        && wget -O python.tar.xz "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz" \
        && wget -O python.tar.xz.asc "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc" \
        && export GNUPGHOME="$(mktemp -d)" \
        && gpg --batch --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$GPG_KEY" \
        && gpg --batch --verify python.tar.xz.asc python.tar.xz \
        && { command -v gpgconf > /dev/null && gpgconf --kill all || :; } \
        && rm -rf "$GNUPGHOME" python.tar.xz.asc \
        && mkdir -p /usr/src/python \
        && tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \
        && rm python.tar.xz \
        \
        && cd /usr/src/python \
        && gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
        && ./configure \
            --build="$gnuArch" \
            --enable-loadable-sqlite-extensions \
            --enable-optimizations \
            --enable-option-checking=fatal \
            --enable-shared \
            --with-system-expat \
            --with-system-ffi \
            --without-ensurepip \
        && make -j "$(nproc)" \
    # setting PROFILE_TASK makes "--enable-optimizations" reasonable: https://bugs.python.org/issue36044 / https://github.com/docker-library/python/issues/160#issuecomment-509426916
            PROFILE_TASK='-m test.regrtest --pgo \
                test_array \
                test_base64 \
                test_binascii \
                test_binhex \
                test_binop \
                test_bytes \
                test_c_locale_coercion \
                test_class \
                test_cmath \
                test_codecs \
                test_compile \
                test_complex \
                test_csv \
                test_decimal \
                test_dict \
                test_float \
                test_fstring \
                test_hashlib \
                test_io \
                test_iter \
                test_json \
                test_long \
                test_math \
                test_memoryview \
                test_pickle \
                test_re \
                test_set \
                test_slice \
                test_struct \
                test_threading \
                test_time \
                test_traceback \
                test_unicode \
            ' \
        && make install \
        && ldconfig \
        \
        && apt-mark auto '.*' > /dev/null \
        && apt-mark manual $savedAptMark \
        && find /usr/local -type f -executable -not \( -name '*tkinter*' \) -exec ldd '{}' ';' \
            | awk '/=>/ { print $(NF-1) }' \
            | sort -u \
            | xargs -r dpkg-query --search \
            | cut -d: -f1 \
            | sort -u \
            | xargs -r apt-mark manual \
        && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
        && rm -rf /var/lib/apt/lists/* \
        \
        && find /usr/local -depth \
            \( \
                \( -type d -a \( -name test -o -name tests -o -name idle_test \) \) \
                -o \
                \( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
            \) -exec rm -rf '{}' + \
        && rm -rf /usr/src/python \
        \
        && python3 --version

        # make some useful symlinks that are expected to exist
        cd /usr/local/bin \
        && ln -s idle3 idle \
        && ln -s pydoc3 pydoc \
        && ln -s python3 python \
        && ln -s python3-config python-config

    # if this is called "PIP_VERSION", pip explodes with "ValueError: invalid truth value '<VERSION>'"
    export PYTHON_PIP_VERSION=20.1.1
    # https://github.com/pypa/get-pip
    export PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/eff16c878c7fd6b688b9b4c4267695cf1a0bf01b/get-pip.py
    export PYTHON_GET_PIP_SHA256=b3153ec0cf7b7bbf9556932aa37e4981c35dc2a2c501d70d91d2795aa532be79

    set -ex; \
        \
        savedAptMark="$(apt-mark showmanual)"; \
        apt-get update; \
        apt-get install -y --no-install-recommends wget; \
        \
        wget -O get-pip.py "$PYTHON_GET_PIP_URL"; \
        echo "$PYTHON_GET_PIP_SHA256 *get-pip.py" | sha256sum --check --strict -; \
        \
        apt-mark auto '.*' > /dev/null; \
        [ -z "$savedAptMark" ] || apt-mark manual $savedAptMark; \
        apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
        rm -rf /var/lib/apt/lists/*; \
        \
        python get-pip.py \
            --disable-pip-version-check \
            --no-cache-dir \
            "pip==$PYTHON_PIP_VERSION" \
        ; \
        pip --version; \
        \
        find /usr/local -depth \
            \( \
                \( -type d -a \( -name test -o -name tests -o -name idle_test \) \) \
                -o \
                \( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
            \) -exec rm -rf '{}' +; \
        rm -f get-pip.py

    export PY_VER=37
    export TENSORFLOW_VERSION=2.1.0

    python -m pip install \
        tensorflow-gpu==${TENSORFLOW_VERSION}

%environment
    export CUDNN_VERSION=7.6.5.32
    export CUDA_PKG_VERSION=10-1=10.1.243-1
    export CUDA_VERSION=10.1.243
    export NCCL_VERSION=2.7.8
    export NVIDIA_REQUIRE_CUDA="cuda>=10.1 brand=tesla,driver>=396,driver<397 brand=tesla,driver>=410,driver<411 brand=tesla,driver>=418,driver<419"
    export LIBRARY_PATH=/usr/local/cuda/lib64/stubs
    export LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64
    export NVIDIA_DRIVER_CAPABILITIES=compute,utility
    export PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/bin:/usr/local/sbin:/usr/sbin:/usr/bin:/sbin:/bin
    export LANG=C.UTF-8
    export LC_ALL=C.UTF-8
    export PYTHON_VERSION=3.7.7
```

## Collection

 - Name: [fenz-org/tensorflow](https://github.com/fenz-org/tensorflow)
 - License: None

