---
id: 8914
name: "dominik-handler/AP_singu"
branch: "master"
tag: "mosdepth"
commit: "e55ba3e87926f1ae97d6e85fa8284f37f594a833"
version: "52e281bbf7d26f5c96c8965df7fcf0a9"
build_date: "2021-02-26T21:45:09.369Z"
size_mb: 1524
size: 643584031
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/mosdepth/2021-02-26-e55ba3e8-52e281bb/52e281bbf7d26f5c96c8965df7fcf0a9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/mosdepth/2021-02-26-e55ba3e8-52e281bb/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/mosdepth/2021-02-26-e55ba3e8-52e281bb/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:mosdepth

```bash
$ singularity pull shub://dominik-handler/AP_singu:mosdepth
```

## Singularity Recipe

```singularity
#mosdepth in singularity

Bootstrap: docker
From: ubuntu:16.04
%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at>
  mosdepth v0.24.0  

%runscript
    mosdepth "$@"

%post
    apt-get update
    apt-get -y install wget git-all
    apt-get -y install sudo


    apt-get clean && apt-get update && apt-get install -y \
       locales \
       language-pack-fi  \
       language-pack-en && \
       export LANGUAGE=en_US.UTF-8 && \
       export LANG=en_US.UTF-8 && \
       export LC_ALL=en_US.UTF-8 && \
       locale-gen en_US.UTF-8 && \
       dpkg-reconfigure --frontend noninteractive locales


    apt-get update
    apt-get install bzip2
    apt-get -y install python3.5 python3-dev python3-pip
 
    apt-get -y install python3-setuptools
    
    #update to version 1.19.0
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /Software/anaconda3 && \
    rm Miniconda3-latest-Linux-x86_64.sh
    PATH="/Software/anaconda3/bin:$PATH"

    apt-get update
    apt-get install bzip2
    apt-get -y install python3.5 python3-dev python3-pip
 
    apt-get -y install python3-setuptools
    
    #update to version 1.19.0
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /Software/anaconda3 && \
    rm Miniconda3-latest-Linux-x86_64.sh
    PATH="/Software/anaconda3/bin:$PATH"
    
  conda config --add channels defaults
  conda config --add channels conda-forge
  conda config --add channels bioconda

  conda install mosdepth

    cd 
    git clone https://github.com/brentp/mosdepth.git


    mkdir /groups
    mkdir /scratch
    mkdir /scratch-ii2

%environment
    PATH="PATH=/Software/anaconda3/bin:${PATH}"
    export $PATH


%test
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

