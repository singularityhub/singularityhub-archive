---
id: 11158
name: "J35P312/FindSVSingularity"
branch: "master"
tag: "latest"
commit: "25b0d9969bb41b21c770e17926bbd0f44ee1550f"
version: "0a1809e9e8513d60c3ebf7f8637d3f7b"
build_date: "2021-02-22T11:29:10.709Z"
size_mb: 1531.0
size: 695373855
sif: "https://datasets.datalad.org/shub/J35P312/FindSVSingularity/latest/2021-02-22-25b0d996-0a1809e9/0a1809e9e8513d60c3ebf7f8637d3f7b.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/J35P312/FindSVSingularity/latest/2021-02-22-25b0d996-0a1809e9/
recipe: https://datasets.datalad.org/shub/J35P312/FindSVSingularity/latest/2021-02-22-25b0d996-0a1809e9/Singularity
collection: J35P312/FindSVSingularity
---

# J35P312/FindSVSingularity:latest

```bash
$ singularity pull shub://J35P312/FindSVSingularity:latest
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

    cd /opt/ && wget https://root.cern.ch/download/root_v6.13.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz
    cd /opt/ && tar -xvf root_v6.13.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz

    export ROOTSYS=/opt/root
    export PATH=$PATH:$ROOTSYS/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ROOTSYS/lib

    cd /opt/ && wget https://github.com/abyzovlab/CNVnator/releases/download/v0.3.3/CNVnator_v0.3.3.zip
    cd /opt && unzip CNVnator_v0.3.3.zip
    cd /opt/CNVnator_v0.3.3/src/samtools/ && make
    cd /opt/CNVnator_v0.3.3/src/ && make

    cd /opt/ && wget https://github.com/SciLifeLab/TIDDIT/archive/TIDDIT-2.12.0.zip && unzip TIDDIT-2.12.0.zip
    mv /opt/TIDDIT-TIDDIT-2.12.0 /opt/TIDDIT
    cd /opt/TIDDIT && ./INSTALL.sh .

    cd /opt/ && git clone https://github.com/J35P312/SVDB.git  
    cd /opt/SVDB && pip install -e .

    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda

    conda install -c bioconda samtools vt

    pip install genmod pyaml
```

## Collection

 - Name: [J35P312/FindSVSingularity](https://github.com/J35P312/FindSVSingularity)
 - License: None

