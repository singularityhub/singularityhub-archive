---
id: 2981
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "busco_3.0.2"
commit: "ceb5a080bfd1e02ab4af2518472d5303365cdb14"
version: "aa1523bcbcb6cfa64776c6bad2c040fe"
build_date: "2021-03-01T01:54:00.231Z"
size_mb: 2369
size: 735940639
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/busco_3.0.2/2021-03-01-ceb5a080-aa1523bc/aa1523bcbcb6cfa64776c6bad2c040fe.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/busco_3.0.2/2021-03-01-ceb5a080-aa1523bc/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/busco_3.0.2/2021-03-01-ceb5a080-aa1523bc/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:busco_3.0.2

```bash
$ singularity pull shub://TomHarrop/singularity-containers:busco_3.0.2
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: build-essential software-properties-common python3 wget zlib1g-dev language-pack-en

%help

    Container for BUSCO 3.0.2
    http://busco.ezlab.org/

    Includes augustus 3.3 & ncbi-blast+ 2.2.31

%labels

    VERSION "BUSCO 3.0.2"

%post

    # build variables
    export AUGUSTUS_CONFIG_PATH="/opt/augustus-3.3/config"
    export BUSCO_CONFIG_FILE="/busco/config/config.ini"
    export PATH="${PATH}:/blast/bin:/opt/augustus-3.3/bin:/opt/augustus-3.3/scripts:/busco/scripts"
    export TOOLDIR=/tools

    # use python3
    ln -s /usr/bin/python3 /usr/local/bin/python

    # add apt repos
    add-apt-repository \
        "deb http://archive.ubuntu.com/ubuntu bionic main universe restricted multiverse"
    add-apt-repository \
        "deb http://archive.canonical.com/ubuntu bionic partner"
    apt update

    # install dependencies via apt
    apt install -y \
        autoconf \
        automake \
        bamtools \
        git \
        hmmer \
        libbamtools-dev \
        libboost-iostreams-dev \
        libbz2-dev \
        libncurses5-dev \
        liblzma-dev \
        python3-pip

    # augustus dependencies
    mkdir "${TOOLDIR}"

    # augustus dependencies - htslib
    cd "${TOOLDIR}"
    git clone https://github.com/samtools/htslib.git
    cd htslib
    autoheader && autoconf && ./configure && make && make install

    # augustus dependencies - bcftools
    cd "${TOOLDIR}"
    git clone https://github.com/samtools/bcftools.git
    cd bcftools
    autoheader && autoconf && ./configure && make && make install

    # augustus dependencies - tabix
    cd "${TOOLDIR}"
    git clone https://github.com/samtools/tabix.git
    cd tabix
    make

    # augustus dependencies - samtools
    cd "${TOOLDIR}"
    git clone https://github.com/samtools/samtools.git
    cd samtools
    autoheader && autoconf -Wno-syntax && ./configure && make && make install

    # install augustus
    cd
    mkdir /augustus
    wget -O "augustus.tar.gz" \
        http://bioinf.uni-greifswald.de/augustus/binaries/augustus.current.tar.gz
    tar -zxf augustus.tar.gz \
        -C /augustus \
        --strip-components 1
    rm -f augustus.tar.gz
    cd /augustus 
    make && make install

    # allow BUSCO to *write* to the augustus config dir. Yuck.
    chmod -R 777 "${AUGUSTUS_CONFIG_PATH}"

    # install blast 2.2.31
    cd
    wget -O "blast.tar.gz" \
        ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.31/ncbi-blast-2.2.31+-x64-linux.tar.gz
    mkdir /blast
    tar -zxf blast.tar.gz \
        -C /blast \
        --strip-components 1
    rm -f blast.tar.gz

    # install BUSCO
    pip3 install git+http://gitlab.com/ezlab/busco.git
    git clone https://gitlab.com/ezlab/busco.git /busco

    # edit config file
    cat > "${BUSCO_CONFIG_FILE}" << _EOF_
[busco]
[tblastn]
path = /blast/bin
[makeblastdb]
path = /blast/bin
[augustus]
path = /usr/local/bin
[etraining]
path = /usr/local/bin
[gff2gbSmallDNA.pl]
path = /opt/augustus-3.3/scripts
[new_species.pl]
path = /opt/augustus-3.3/scripts
[optimize_augustus.pl]
path = /opt/augustus-3.3/scripts
[hmmsearch]
path = /usr/bin
_EOF_

%environment

    export AUGUSTUS_CONFIG_PATH="/opt/augustus-3.3/config"
    export BUSCO_CONFIG_FILE="/busco/config/config.ini"
    export TOOLDIR="/tools"
    export PATH="${PATH}:/blast/bin:/opt/augustus-3.3/bin:/opt/augustus-3.3/scripts:/busco/scripts"

%runscript

    exec /busco/scripts/run_BUSCO.py "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

