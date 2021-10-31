---
id: 7820
name: "J35P312/PileupPipe"
branch: "master"
tag: "latest"
commit: "a7bd1b77888916bd1dbf1b8363b73d95ce9532c2"
version: "b2610238b07e67f9d9451124da047bc2"
build_date: "2019-10-31T14:05:16.194Z"
size_mb: 1678
size: 1040302111
sif: "https://datasets.datalad.org/shub/J35P312/PileupPipe/latest/2019-10-31-a7bd1b77-b2610238/b2610238b07e67f9d9451124da047bc2.simg"
url: https://datasets.datalad.org/shub/J35P312/PileupPipe/latest/2019-10-31-a7bd1b77-b2610238/
recipe: https://datasets.datalad.org/shub/J35P312/PileupPipe/latest/2019-10-31-a7bd1b77-b2610238/Singularity
collection: J35P312/PileupPipe
---

# J35P312/PileupPipe:latest

```bash
$ singularity pull shub://J35P312/PileupPipe:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
SHELL=/bin/bash
PATH=/opt/anaconda/bin:${PATH}
LC_ALL=C.UTF-8
ROOTSYS=/opt/root/
LD_LIBRARY_PATH=/opt/root/lib


%runscript
    echo "This is what happens when you run the container..."
    export PATH=/opt/anaconda/bin:${PATH}

%post
    echo "Hello from inside the container"
    apt-get update
    apt-get -y install wget git bzip2 build-essential gcc zlib1g-dev language-pack-en-base apt-transport-https make cmake unzip libncurses5-dev libncursesw5-dev
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

    cd /root/ && wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
    cd /root/ && chmod 700 ./Miniconda2-latest-Linux-x86_64.sh
    cd /root/ && bash ./Miniconda2-latest-Linux-x86_64.sh -b -p /opt/anaconda/   

    export PATH=/opt/anaconda/bin:${PATH} 

    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda

    conda install -c bioconda samtools vt tabix gatk4
```

## Collection

 - Name: [J35P312/PileupPipe](https://github.com/J35P312/PileupPipe)
 - License: None

