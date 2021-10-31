---
id: 13531
name: "J35P312/Nim_test"
branch: "master"
tag: "latest"
commit: "686adbaa511ea5d1648e25eed3d4e4941b650a67"
version: "9c5172a24ed864a528897f70b565a092"
build_date: "2020-07-04T14:24:54.930Z"
size_mb: 1573.0
size: 642482207
sif: "https://datasets.datalad.org/shub/J35P312/Nim_test/latest/2020-07-04-686adbaa-9c5172a2/9c5172a24ed864a528897f70b565a092.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/J35P312/Nim_test/latest/2020-07-04-686adbaa-9c5172a2/
recipe: https://datasets.datalad.org/shub/J35P312/Nim_test/latest/2020-07-04-686adbaa-9c5172a2/Singularity
collection: J35P312/Nim_test
---

# J35P312/Nim_test:latest

```bash
$ singularity pull shub://J35P312/Nim_test:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
SHELL=/bin/bash
PATH=/opt/anaconda/bin:${PATH}
LC_ALL=C.UTF-8

%runscript
    echo "This is what happens when you run the container..."
    export PATH=/opt/anaconda/bin:${PATH}    

%post
    echo "Hello from inside the container"
    apt-get update
    apt-get -y install wget git bzip2 build-essential gcc zlib1g-dev language-pack-en-base apt-transport-https make cmake unzip python3 sudo python2.7 python-numpy python-matplotlib python-biopython samtools
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

    cd /root/ && wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
    cd /root/ && chmod 700 ./Miniconda2-latest-Linux-x86_64.sh
    cd /root/ && bash ./Miniconda2-latest-Linux-x86_64.sh -b -p /opt/anaconda/

    export PATH=/opt/anaconda/bin:${PATH}

    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda
    conda config --add channels r
    conda install -c conda-forge nim htslib -y

    mkdir /opt/nimble

    cd /opt/ && git clone https://github.com/brentp/hts-nim.git && cd hts-nim && nimble --nimbleDir:/opt/nimble install -y
    nimble --nimbleDir:/opt/nimble install xlsx -y
    nimble --nimbleDir:/opt/nimble install argparse -y
```

## Collection

 - Name: [J35P312/Nim_test](https://github.com/J35P312/Nim_test)
 - License: None

