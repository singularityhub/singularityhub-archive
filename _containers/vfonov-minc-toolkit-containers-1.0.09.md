---
id: 1295
name: "vfonov/minc-toolkit-containers"
branch: "master"
tag: "1.0.09"
commit: "445dd83b9408c048fe819093f5a11d54298e7519"
version: "a42864991f2e71a4790cd47d26997834"
build_date: "2018-01-13T02:41:21.204Z"
size_mb: 2843
size: 1026338847
sif: "https://datasets.datalad.org/shub/vfonov/minc-toolkit-containers/1.0.09/2018-01-13-445dd83b-a4286499/a42864991f2e71a4790cd47d26997834.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/vfonov/minc-toolkit-containers/1.0.09/2018-01-13-445dd83b-a4286499/
recipe: https://datasets.datalad.org/shub/vfonov/minc-toolkit-containers/1.0.09/2018-01-13-445dd83b-a4286499/Singularity
collection: vfonov/minc-toolkit-containers
---

# vfonov/minc-toolkit-containers:1.0.09

```bash
$ singularity pull shub://vfonov/minc-toolkit-containers:1.0.09
```

## Singularity Recipe

```singularity
#Bootstrap: localimage
#From: /home/vfonov/src/minc-toolkit-containers/singularity/minc-toolkit-base.simg
Bootstrap: shub
From: vfonov/minc-toolkit-containers:base

# install basic system packages
%post
    # update locales
    locale-gen en_US.UTF-8 en_US en_CA.UTF-8 en_CA
    dpkg-reconfigure locales
    # install minc-toolkit 1.9.15
    wget http://packages.bic.mni.mcgill.ca/minc-toolkit/Debian/minc-toolkit-1.0.09-20170529-Ubuntu_16.04-x86_64.deb   && \
    dpkg -i minc-toolkit-1.0.09-20170529-Ubuntu_16.04-x86_64.deb && \
    rm -f minc-toolkit-1.0.09-20170529-Ubuntu_16.04-x86_64.deb && \
    wget http://packages.bic.mni.mcgill.ca/minc-toolkit/Debian/beast-library-1.1.0-20121212.deb && \
    dpkg -i beast-library-1.1.0-20121212.deb && \
    rm -f beast-library-1.1.0-20121212.deb && \
    wget http://packages.bic.mni.mcgill.ca/minc-toolkit/Debian/bic-mni-models-0.1.1-20120421.deb && \
    dpkg -i bic-mni-models-0.1.1-20120421.deb && \
    rm -f bic-mni-models-0.1.1-20120421.deb
    
    apt-get autoclean 
    rm -rf /var/lib/apt/lists/*
    
    
    # install RMINC
    . /opt/minc/1.0.09/minc-toolkit-config.sh 
    export MINC_TOOLKIT=/opt/minc/1.0.09
    wget https://github.com/Mouse-Imaging-Centre/RMINC/releases/download/v1.5.1.0/RMINC_1.5.1.0.tar.gz 
    R CMD INSTALL RMINC_1.5.1.0.tar.gz --configure-args='--with-build-path=/opt/minc/1.0.09' 
    rm -f RMINC_1.5.1.0.tar.gz


    # install pyezminc, pyminc, minc2-simple
    . /opt/minc/1.0.09/minc-toolkit-config.sh && \
    pip install pyminc --no-cache-dir && \
    wget https://github.com/BIC-MNI/pyezminc/archive/release-1.2.01.tar.gz && \
    pip install release-1.2.01.tar.gz --no-cache-dir && \
    wget https://github.com/vfonov/minc2-simple/archive/v0.tar.gz && \
    tar zxf v0.tar.gz && \
    python minc2-simple-0/python/setup.py install && \
    rm -rf v0.tar.gz release-1.2.01.tar.gz minc2-simple-0 
    
    echo ". /opt/minc/1.0.09/minc-toolkit-config.sh" >> $SINGULARITY_ENVIRONMENT
    echo "export MINC_TOOLKIT=/opt/minc/1.0.09" >> $SINGULARITY_ENVIRONMENT

%labels
    Maintainer Vladimir S. Fonov
    AUTHOR vladimir.fonov@gmail.com
    Version 1.0.09
    
%help
    Minc-toolkit 1.0.09 in a container
```

## Collection

 - Name: [vfonov/minc-toolkit-containers](https://github.com/vfonov/minc-toolkit-containers)
 - License: None

