---
id: 12982
name: "J35P312/FluFFyPipe"
branch: "master"
tag: "latest"
commit: "70e1216b11506828059c04dc0d80de221ed19bb8"
version: "7af3969aa82998a8ef1506f0d382ba6e"
build_date: "2021-03-08T17:54:56.189Z"
size_mb: 3740.0
size: 1870495775
sif: "https://datasets.datalad.org/shub/J35P312/FluFFyPipe/latest/2021-03-08-70e1216b-7af3969a/7af3969aa82998a8ef1506f0d382ba6e.sif"
url: https://datasets.datalad.org/shub/J35P312/FluFFyPipe/latest/2021-03-08-70e1216b-7af3969a/
recipe: https://datasets.datalad.org/shub/J35P312/FluFFyPipe/latest/2021-03-08-70e1216b-7af3969a/Singularity
collection: J35P312/FluFFyPipe
---

# J35P312/FluFFyPipe:latest

```bash
$ singularity pull shub://J35P312/FluFFyPipe:latest
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
    export PATH=/opt/anaconda/bin:${PATH}    

%post
    apt-get update
    apt-get -y install wget git bzip2 build-essential gcc zlib1g-dev language-pack-en-base apt-transport-https make cmake unzip sudo libatlas3-base python3 python3-pip
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

    cd /root/ && wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
    cd /root/ && chmod 700 ./Miniconda2-latest-Linux-x86_64.sh
    cd /root/ && bash ./Miniconda2-latest-Linux-x86_64.sh -b -p /opt/anaconda/

    export PATH=/opt/anaconda/bin:${PATH}

    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda
    conda config --add channels r

    #conda install -c bioconda wisecondorx=1.1.5
    pip install -U git+https://github.com/CenterForMedicalGeneticsGhent/WisecondorX@v1.1.6

    conda install -c bioconda samtools picard bioconductor-dnacopy
    conda install -c bioconda bwa fastqc biobambam
    conda install -c r r-doparallel r-foreach r-neuralnet r-glmnet r-data.table r-mass r-matrix r-jsonlite

    pip install sklearn numpy scipy matplotlib pysam futures bottleneck cython
    pip3 install multiqc
    
    cd /bin/ && wget https://github.com/CenterForMedicalGeneticsGhent/PREFACE/archive/v0.1.1.zip && unzip v0.1.1.zip
    cd /
    
    cd /bin/ && git clone https://github.com/J35P312/AMYCNE.git && cd AMYCNE && python setup.py build_ext --inplace    
    
    git clone https://github.com/SciLifeLab/TIDDIT.git
    mv TIDDIT/* /bin/
    cd /bin/ && ./INSTALL.sh
    chmod +x /bin/TIDDIT.py

   cd /bin/ && git clone https://github.com/J35P312/FluFFyPipe.git
```

## Collection

 - Name: [J35P312/FluFFyPipe](https://github.com/J35P312/FluFFyPipe)
 - License: None

