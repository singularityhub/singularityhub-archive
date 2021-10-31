---
id: 6301
name: "dominik-handler/AP_singu"
branch: "master"
tag: "oligominer"
commit: "f9ab8bc372994f187d0f0f2850ca78b934eb6354"
version: "effa157c39f7ba0f5dfcf302f3ab8571"
build_date: "2021-03-22T12:04:22.565Z"
size_mb: 1263
size: 497197087
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/oligominer/2021-03-22-f9ab8bc3-effa157c/effa157c39f7ba0f5dfcf302f3ab8571.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/oligominer/2021-03-22-f9ab8bc3-effa157c/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/oligominer/2021-03-22-f9ab8bc3-effa157c/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:oligominer

```bash
$ singularity pull shub://dominik-handler/AP_singu:oligominer
```

## Singularity Recipe

```singularity
#OligoMiner in singularity

Bootstrap: docker
From: ubuntu:16.04

%runscript
    cd /OligoMiner
    python "$@"

%post
    apt-get update
    apt-get -y install wget sudo 

    apt-get update
    apt-get -y install python python-setuptools git-core bzip2

    
    #update to version 1.19.0
    wget https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86_64.sh && \
    bash Miniconda2-latest-Linux-x86_64.sh -b -p /Software/anaconda && \
    rm Miniconda2-latest-Linux-x86_64.sh
    PATH="/Software/anaconda/bin:$PATH"
    
    conda config --add channels r
    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda    
    conda install numpy 
    conda install scipy biopython scikit-learn bowtie2 jellyfish

    cd /
    git clone https://github.com/brianbeliveau/OligoMiner
  
    mkdir /groups
    mkdir /scratch
    mkdir /scratch-ii2

%environment
    PATH="PATH=/Software/anaconda/bin:${PATH}"
    export $PATH

%test
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

