---
id: 1273
name: "vfonov/minc-toolkit-containers"
branch: "master"
tag: "1.9.15"
commit: "395e7d60cabc65e20d8c6385d79d093e026a165a"
version: "4da784f4c64b569e95cb44053dd9c742"
build_date: "2018-01-13T02:41:21.213Z"
size_mb: 3994
size: 1228206111
sif: "https://datasets.datalad.org/shub/vfonov/minc-toolkit-containers/1.9.15/2018-01-13-395e7d60-4da784f4/4da784f4c64b569e95cb44053dd9c742.simg"
url: https://datasets.datalad.org/shub/vfonov/minc-toolkit-containers/1.9.15/2018-01-13-395e7d60-4da784f4/
recipe: https://datasets.datalad.org/shub/vfonov/minc-toolkit-containers/1.9.15/2018-01-13-395e7d60-4da784f4/Singularity
collection: vfonov/minc-toolkit-containers
---

# vfonov/minc-toolkit-containers:1.9.15

```bash
$ singularity pull shub://vfonov/minc-toolkit-containers:1.9.15
```

## Singularity Recipe

```singularity
#Bootstrap: localimage
#From: /home/vfonov/src/minc-toolkit-containers/singularity/minc-toolkit-base.simg
Bootstrap: shub
From: vfonov/minc-toolkit-containers:base

# install basic system packages
%post
    # install minc-toolkit 1.9.15
    wget http://packages.bic.mni.mcgill.ca/minc-toolkit/Debian/minc-toolkit-1.9.15-20170529-Ubuntu_16.04-x86_64.deb  && \
    dpkg -i minc-toolkit-1.9.15-20170529-Ubuntu_16.04-x86_64.deb && \
    rm -f minc-toolkit-1.9.15-20170529-Ubuntu_16.04-x86_64.deb && \
    wget http://packages.bic.mni.mcgill.ca/minc-toolkit/Debian/beast-library-1.1.0-20121212.deb && \
    dpkg -i beast-library-1.1.0-20121212.deb && \
    rm -f beast-library-1.1.0-20121212.deb && \
    wget http://packages.bic.mni.mcgill.ca/minc-toolkit/Debian/bic-mni-models-0.1.1-20120421.deb && \
    dpkg -i bic-mni-models-0.1.1-20120421.deb && \
    rm -f bic-mni-models-0.1.1-20120421.deb
    
    apt-get autoclean 
    rm -rf /var/lib/apt/lists/*
    
    
    # install RMINC
    . /opt/minc/1.9.15/minc-toolkit-config.sh && \
    wget https://github.com/Mouse-Imaging-Centre/RMINC/releases/download/v1.5.1.0/RMINC_1.5.1.0.tar.gz && \
    R CMD INSTALL RMINC_1.5.1.0.tar.gz --configure-args='--with-build-path=/opt/minc/1.9.15' && \
    rm -f RMINC_1.5.1.0.tar.gz


    # install pyezminc, pyminc, minc2-simple
    . /opt/minc/1.9.15/minc-toolkit-config.sh && \
    pip install pyminc --no-cache-dir && \
    wget https://github.com/BIC-MNI/pyezminc/archive/release-1.2.01.tar.gz && \
    pip install release-1.2.01.tar.gz --no-cache-dir && \
    wget https://github.com/vfonov/minc2-simple/archive/v0.tar.gz && \
    tar zxf v0.tar.gz && \
    python minc2-simple-0/python/setup.py install && \
    rm -rf v0.tar.gz release-1.2.01.tar.gz minc2-simple-0 
    
    echo ". /opt/minc/1.9.15/minc-toolkit-config.sh" >> $SINGULARITY_ENVIRONMENT
    
    
%labels
    Maintainer Vladimir S. Fonov
    AUTHOR vladimir.fonov@gmail.com
    Version 1.9.15
    
%help
    Help me. I'm in the container.
```

## Collection

 - Name: [vfonov/minc-toolkit-containers](https://github.com/vfonov/minc-toolkit-containers)
 - License: None

