---
id: 12303
name: "TomHarrop/assembly-utils"
branch: "master"
tag: "busco_4.0.4"
commit: "909a99ba56b5cbe7d58272cb285fe9c49610baff"
version: "42eda22a80145303fe5636c048ccc7e6d54c3544461c7fe1a1c170b94998b781"
build_date: "2021-01-25T22:12:40.079Z"
size_mb: 753.01171875
size: 789590016
sif: "https://datasets.datalad.org/shub/TomHarrop/assembly-utils/busco_4.0.4/2021-01-25-909a99ba-42eda22a/42eda22a80145303fe5636c048ccc7e6d54c3544461c7fe1a1c170b94998b781.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/assembly-utils/busco_4.0.4/2021-01-25-909a99ba-42eda22a/
recipe: https://datasets.datalad.org/shub/TomHarrop/assembly-utils/busco_4.0.4/2021-01-25-909a99ba-42eda22a/Singularity
collection: TomHarrop/assembly-utils
---

# TomHarrop/assembly-utils:busco_4.0.4

```bash
$ singularity pull shub://TomHarrop/assembly-utils:busco_4.0.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help
    Container for BUSCO 4.0.4
    http://busco.ezlab.org/

    Includes augustus 3.3.3 & ncbi-blast+ 2.2.31

%labels
    VERSION "BUSCO 4.0.4"

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
        autoconf \
        automake \
        bamtools \
        build-essential \
        git \
        hmmer \
        libbamtools-dev \
        libboost-iostreams-dev \
        libbz2-dev \
        libcurl3-dev \
        liblzma-dev \
        libncurses5-dev \
        libssl-dev \
        prodigal \
        python3 \
        python3-pip \
        software-properties-common \
        wget \
        zlib1g-dev

    # build variables
    export AUGUSTUS_CONFIG_PATH="/opt/augustus-3.3.3/config"
    export BUSCO_CONFIG_FILE="/busco/config/config.ini"
    export PATH="${PATH}:/blast/bin:/opt/augustus-3.3.3/bin:/opt/augustus-3.3.3/scripts:/busco/scripts"
    export TOOLDIR=/tools

    # use python3
    update-alternatives \
        --install /usr/local/bin/python \
        python \
        /usr/bin/python3 \
        1

    # augustus dependencies
    mkdir "${TOOLDIR}"

    # augustus dependencies - htslib
    (
    cd "${TOOLDIR}" || exit 1
    git clone https://github.com/samtools/htslib.git
    cd htslib || exit 1
    autoheader && autoconf && ./configure && make && make install
    )

    # augustus dependencies - bcftools
    (
    cd "${TOOLDIR}" || exit 1
    git clone https://github.com/samtools/bcftools.git
    cd bcftools || exit 1
    autoheader && autoconf && ./configure && make && make install
    )

    # augustus dependencies - tabix
    (
    cd "${TOOLDIR}" || exit 1
    git clone https://github.com/samtools/tabix.git
    cd tabix || exit 1
    make
    )

    # augustus dependencies - samtools
    (
    cd "${TOOLDIR}" || exit 1
    git clone https://github.com/samtools/samtools.git
    cd samtools || exit 1
    autoheader && autoconf -Wno-syntax && ./configure && make && make install
    )

    # install augustus
    (
    mkdir /augustus
    wget -O "augustus.tar.gz" \
        http://bioinf.uni-greifswald.de/augustus/binaries/augustus-3.3.3.tar.gz
    tar -zxf augustus.tar.gz \
        -C /augustus \
        --strip-components 1
    rm -f augustus.tar.gz
    cd /augustus || exit 1
    make && make install
    )

    # allow *writing* to the augustus config dir. No really.
    chmod -R 777 "${AUGUSTUS_CONFIG_PATH}"

    # install blast 2.2.31
    (
    wget -O "blast.tar.gz" \
        ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.31/ncbi-blast-2.2.31+-x64-linux.tar.gz
    mkdir /blast
    tar -zxf blast.tar.gz \
        -C /blast \
        --strip-components 1
    rm -f blast.tar.gz
    )

    # install sepp
    (
    git clone https://github.com/smirarab/sepp.git /sepp
    cd /sepp || exit 1
    git checkout -f 4.3.10
    git submodule update --init --recursive
    python setup.py config
    python setup.py install
    )

    # install BUSCO
    (
    /usr/bin/pip3 install biopython
    git clone https://gitlab.com/ezlab/busco.git /busco
    cd /busco || exit 1
    git checkout -f  4.0.4 
    git submodule update --init --recursive
    python3 setup.py install
    mv "${BUSCO_CONFIG_FILE}" "${BUSCO_CONFIG_FILE}.default"
    busco_configurator.py \
        "${BUSCO_CONFIG_FILE}.default" \
        "${BUSCO_CONFIG_FILE}"
    )

%environment

    export AUGUSTUS_CONFIG_PATH="/opt/augustus-3.3.3/config"
    export BUSCO_CONFIG_FILE="/busco/config/config.ini"
    export TOOLDIR="/tools"
    export PATH="${PATH}:/blast/bin:/opt/augustus-3.3.3/bin:/opt/augustus-3.3.3/scripts:/busco/scripts"
    export LC_ALL=C

%runscript

    exec /usr/local/bin/busco "$@"
```

## Collection

 - Name: [TomHarrop/assembly-utils](https://github.com/TomHarrop/assembly-utils)
 - License: None

