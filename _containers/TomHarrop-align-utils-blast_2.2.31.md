---
id: 12302
name: "TomHarrop/align-utils"
branch: "master"
tag: "blast_2.2.31"
commit: "e87ac827ec99c64528c5fba2f575b8512aa2dcf2"
version: "4364f04767e6022ec939e2e71597a708942615cc4e071a14b7c029e6309c928c"
build_date: "2020-12-15T21:08:28.722Z"
size_mb: 297.1015625
size: 311533568
sif: "https://datasets.datalad.org/shub/TomHarrop/align-utils/blast_2.2.31/2020-12-15-e87ac827-4364f047/4364f04767e6022ec939e2e71597a708942615cc4e071a14b7c029e6309c928c.sif"
url: https://datasets.datalad.org/shub/TomHarrop/align-utils/blast_2.2.31/2020-12-15-e87ac827-4364f047/
recipe: https://datasets.datalad.org/shub/TomHarrop/align-utils/blast_2.2.31/2020-12-15-e87ac827-4364f047/Singularity
collection: TomHarrop/align-utils
---

# TomHarrop/align-utils:blast_2.2.31

```bash
$ singularity pull shub://TomHarrop/align-utils:blast_2.2.31
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help
    NCBI BLAST+ base container for BUSCO 4.0.4

    Includes ncbi-blast+ 2.2.31 built on Ubuntu 19.10

%labels
    VERSION "ncbi-blast+ 2.2.31"

%post
    # faster apt downloads
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C
    (
        . /etc/os-release
        cat << _EOF_ > mirror.txt
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME} main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-updates main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-backports main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-security main restricted universe multiverse

_EOF_
        mv /etc/apt/sources.list /etc/apt/sources.list.bak
        cat mirror.txt /etc/apt/sources.list.bak > /etc/apt/sources.list
    )

    # apt dependencies
    apt-get update
    apt-get install -y \
        build-essential \
        cpio \
        wget

    # download v. 1.58 of Boost, which is needed to compile BLAST 2.2.31
    (
    wget \
        -O "boost.tar.gz" \
        https://sourceforge.net/projects/boost/files/boost/1.58.0/boost_1_58_0.tar.gz
    mkdir /boost
    tar -zxf boost.tar.gz \
        -C /boost \
        --strip-components 1
    rm boost.tar.gz
    )

    # download and compile blast
    (
    wget \
        -O "blast.tar.gz" \
    ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.31/ncbi-blast-2.2.31+-src.tar.gz
    mkdir /blast
    tar -zxf blast.tar.gz \
        -C /blast \
        --strip-components 1
    rm blast.tar.gz
    cd /blast/c++ || exit 1
    # force it to compile with g++-9
    sed -i \
        's/2.95\* | 2.96\* | 3.\* | 4.\*/2.95\* | 2.96\* | 3.\* | 4.\* | 9/' \
        src/build-system/configure
    # configure without tests
    ./configure \
        CXXFLAGS="-I/boost"\
        --without-debug \
        --with-mt \
        --without-mysql \
        --without-freetype \
        --without-gnutls \
        --without-hdf5 \
        --with-static \
        --without-boost

    make && make install
    )
    rm -rf /blast /boost

%runscript
    exec /usr/local/bin/blastn "$@"
```

## Collection

 - Name: [TomHarrop/align-utils](https://github.com/TomHarrop/align-utils)
 - License: None

