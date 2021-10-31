---
id: 6318
name: "dominik-handler/AP_singu"
branch: "master"
tag: "nanoplot"
commit: "e3373148ec5e6a805ed451502c0afa42d8af9388"
version: "79bb3bcc23ca52886d4d22a518fd329a"
build_date: "2020-03-31T11:45:24.003Z"
size_mb: 2942
size: 1355952159
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/nanoplot/2020-03-31-e3373148-79bb3bcc/79bb3bcc23ca52886d4d22a518fd329a.simg"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/nanoplot/2020-03-31-e3373148-79bb3bcc/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/nanoplot/2020-03-31-e3373148-79bb3bcc/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:nanoplot

```bash
$ singularity pull shub://dominik-handler/AP_singu:nanoplot
```

## Singularity Recipe

```singularity
#nanoplot in singularity

Bootstrap: docker
From: ubuntu:16.04

%runscript
    NanoPlot "$@"

%post
    apt-get update
    apt-get -y install wget
    apt-get -y install sudo

    apt-get update
    apt-get install bzip2
    apt-get -y install python3.5
 
    apt-get -y install python3-setuptools
    
    #update to version 1.19.0
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /Software/anaconda3 && \
    rm Miniconda3-latest-Linux-x86_64.sh
    PATH="/Software/anaconda3/bin:$PATH"
    
    conda install -c bioconda nanoplot
    
   # easy_install3 pip

   # mkdir -p /NanoTools/
   # cd /NanoTools/
   # pip install NanoPlot
    
    mkdir /groups
    mkdir /scratch
    mkdir /scratch-ii2

%environment
    PATH="PATH=/Software/anaconda3/bin:${PATH}"
    export $PATH



%test
    PATH="PATH=/Software/anaconda3/bin:${PATH}"
    export $PATH

    NanoPlot -h
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

