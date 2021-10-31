---
id: 13157
name: "TomHarrop/align-utils"
branch: "master"
tag: "samtools_1.10"
commit: "d52e0b68cf74f659181d95beac31427c1ade7947"
version: "fa680adfdadc84a9ac91462bbeed3a65d14eae2f614ccf3322fecf0ddd6c1200"
build_date: "2021-03-15T10:24:34.153Z"
size_mb: 401.83984375
size: 421359616
sif: "https://datasets.datalad.org/shub/TomHarrop/align-utils/samtools_1.10/2021-03-15-d52e0b68-fa680adf/fa680adfdadc84a9ac91462bbeed3a65d14eae2f614ccf3322fecf0ddd6c1200.sif"
url: https://datasets.datalad.org/shub/TomHarrop/align-utils/samtools_1.10/2021-03-15-d52e0b68-fa680adf/
recipe: https://datasets.datalad.org/shub/TomHarrop/align-utils/samtools_1.10/2021-03-15-d52e0b68-fa680adf/Singularity
collection: TomHarrop/align-utils
---

# TomHarrop/align-utils:samtools_1.10

```bash
$ singularity pull shub://TomHarrop/align-utils:samtools_1.10
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%help
    samtools 1.10
    bcflib 1.10.2
    htslib 1.10.2
    http://www.htslib.org/

%labels
    VERSION "samtools 1.10"

%runscript
    exec /usr/local/bin/samtools "$@"

%environment
    export LC_ALL=C

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
        git \
        libbz2-dev \
        libcurl4-openssl-dev \
        liblzma-dev \
        libncurses-dev \
        python3-matplotlib \
        texlive-latex-extra \
        texlive-latex-recommended \
        texlive-plain-generic \
        wget \
        zlib1g-dev

    # install releases via github
    git clone \
        https://github.com/samtools/htslib.git \
        /htslib
    cd /htslib || exit 1
    git checkout -f  1.10.2 
    git submodule update --init --recursive
    make
    make install

    git clone \
        https://github.com/samtools/samtools.git \
        /samtools
    cd /samtools || exit 1
    git checkout -f  1.10
    git submodule update --init --recursive
    make
    make install

    git clone \
        https://github.com/samtools/bcftools.git \
        /bcftools
    cd /bcftools || exit 1
    git checkout -f  1.10.2
    git submodule update --init --recursive
    make
    make install

    # tidy up
    rm -rf /htslib /samtools /bcftools
```

## Collection

 - Name: [TomHarrop/align-utils](https://github.com/TomHarrop/align-utils)
 - License: None

