---
id: 7868
name: "dominik-handler/AP_singu"
branch: "master"
tag: "pomoxis"
commit: "7276d9f79e254f090a89495100afdfe489138b6e"
version: "cca21733530577d5e56ac683545c56dc"
build_date: "2019-04-26T18:57:08.095Z"
size_mb: 1493
size: 661401631
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/pomoxis/2019-04-26-7276d9f7-cca21733/cca21733530577d5e56ac683545c56dc.simg"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/pomoxis/2019-04-26-7276d9f7-cca21733/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/pomoxis/2019-04-26-7276d9f7-cca21733/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:pomoxis

```bash
$ singularity pull shub://dominik-handler/AP_singu:pomoxis
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at  
  pomoxis v0.2.2 

%post
    apt-get update
    apt-get -y install wget git build-essential zlib1g-dev libbz2-dev liblzma-dev


  #fix locales
    apt-get clean && apt-get update && apt-get install -y \
       locales \
       language-pack-en && \
       export LANGUAGE=en_US.UTF-8 && \
       export LANG=en_US.UTF-8 && \
       export LC_ALL=en_US.UTF-8 && \
       locale-gen en_US.UTF-8 && \
       dpkg-reconfigure --frontend noninteractive locales

  #install miniconda
    apt-get update
    apt-get -y install bzip2 python3-setuptools python3.5 
    
    #update to version 1.19.0
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /Software/anaconda3 && \
    rm Miniconda3-latest-Linux-x86_64.sh
    PATH="/Software/anaconda3/bin:$PATH"

  #insatall conda packages  
    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda

    git clone --recursive https://github.com/nanoporetech/pomoxis
    cd pomoxis

    CONDA=/Software/anaconda3/ make conda
    
%environment
    PATH="PATH=/Software/anaconda3/bin:${PATH}"
    export $PATH
    export LD_LIBRARY_PATH=/cm/local/apps/cuda-driver/libs/390.12/lib64:/cm/local/apps/cuda-driver/libs/390.12/lib:/software/171020/software/cuda/9.0.176/extras/CUPTI/lib64:/software/171020/software/cuda/9.0.176/lib64:/cm/local/apps/cuda-driver/libs/390.12/lib64:/cm/local/apps/cuda-driver/libs/390.12/lib:$LD_LIBRARY_PATH
    export PATH=/cm/local/apps/cuda-driver/libs/390.12/bin:/software/171020/software/cuda/9.0.176:/software/171020/software/cuda/9.0.176/bin:$PATH

%runscript
  $@
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

