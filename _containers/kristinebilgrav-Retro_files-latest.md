---
id: 15422
name: "kristinebilgrav/Retro_files"
branch: "main"
tag: "latest"
commit: "5deb744b2938c70316d3983e391654b7baae5834"
version: "d6fe1fc608ebb69dcf37605e6782a336"
build_date: "2021-01-28T13:07:31.183Z"
size_mb: 928.0
size: 399802399
sif: "https://datasets.datalad.org/shub/kristinebilgrav/Retro_files/latest/2021-01-28-5deb744b-d6fe1fc6/d6fe1fc608ebb69dcf37605e6782a336.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/kristinebilgrav/Retro_files/latest/2021-01-28-5deb744b-d6fe1fc6/
recipe: https://datasets.datalad.org/shub/kristinebilgrav/Retro_files/latest/2021-01-28-5deb744b-d6fe1fc6/Singularity
collection: kristinebilgrav/Retro_files
---

# kristinebilgrav/Retro_files:latest

```bash
$ singularity pull shub://kristinebilgrav/Retro_files:latest
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
    
    conda install -c bioconda samtools=0.1.19
    conda install -c bioconda bcftools
    conda install -c bioconda BEDTools
    
    cd /bin/ && git clone https://github.com/tk2/RetroSeq.git
```

## Collection

 - Name: [kristinebilgrav/Retro_files](https://github.com/kristinebilgrav/Retro_files)
 - License: None

