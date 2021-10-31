---
id: 1442
name: "vfonov/minc-toolkit-containers"
branch: "master"
tag: "1.9.16-min"
commit: "a97db6ad49d930f09e0de4012f182a372eb84b10"
version: "ce7facab5ddf583c78ad4a6f9157156c"
build_date: "2020-08-31T16:28:34.856Z"
size_mb: 2785
size: 762183711
sif: "https://datasets.datalad.org/shub/vfonov/minc-toolkit-containers/1.9.16-min/2020-08-31-a97db6ad-ce7facab/ce7facab5ddf583c78ad4a6f9157156c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/vfonov/minc-toolkit-containers/1.9.16-min/2020-08-31-a97db6ad-ce7facab/
recipe: https://datasets.datalad.org/shub/vfonov/minc-toolkit-containers/1.9.16-min/2020-08-31-a97db6ad-ce7facab/Singularity
collection: vfonov/minc-toolkit-containers
---

# vfonov/minc-toolkit-containers:1.9.16-min

```bash
$ singularity pull shub://vfonov/minc-toolkit-containers:1.9.16-min
```

## Singularity Recipe

```singularity
#Bootstrap: localimage
#From: /home/vfonov/src/minc-toolkit-containers/singularity/minc-toolkit-base-min.simg
Bootstrap: shub
From: vfonov/minc-toolkit-containers:base-min


# install minc packages
%post
    # update locales
    locale-gen en_US.UTF-8 en_US en_CA.UTF-8 en_CA
    dpkg-reconfigure locales
    # install minc-toolkit 1.9.16
    wget http://packages.bic.mni.mcgill.ca/minc-toolkit/min/minc-toolkit-1.9.16-20180117-Ubuntu_16.04-x86_64.deb
    dpkg -i minc-toolkit-1.9.16-20180117-Ubuntu_16.04-x86_64.deb
    rm -f minc-toolkit-1.9.16-20180117-Ubuntu_16.04-x86_64.deb 
    
    apt-get autoclean 
    rm -rf /var/lib/apt/lists/*
    
    
    # install RMINC
    . /opt/minc/1.9.16/minc-toolkit-config.sh && \
    wget https://github.com/Mouse-Imaging-Centre/RMINC/releases/download/v1.5.1.0/RMINC_1.5.1.0.tar.gz && \
    R CMD INSTALL RMINC_1.5.1.0.tar.gz --configure-args='--with-build-path=/opt/minc/1.9.16' && \
    rm -f RMINC_1.5.1.0.tar.gz


    # install pyezminc, pyminc, minc2-simple
    . /opt/minc/1.9.16/minc-toolkit-config.sh && \
    pip install pyminc --no-cache-dir && \
    wget https://github.com/BIC-MNI/pyezminc/archive/release-1.2.01.tar.gz && \
    pip install release-1.2.01.tar.gz --no-cache-dir && \
    wget https://github.com/vfonov/minc2-simple/archive/v0.tar.gz && \
    tar zxf v0.tar.gz && \
    python minc2-simple-0/python/setup.py install && \
    rm -rf v0.tar.gz release-1.2.01.tar.gz minc2-simple-0 
    
    echo ". /opt/minc/1.9.16/minc-toolkit-config.sh" >> $SINGULARITY_ENVIRONMENT
    

%labels
    Maintainer Vladimir S. Fonov
    AUTHOR vladimir.fonov@gmail.com
    Version 1.9.16
```

## Collection

 - Name: [vfonov/minc-toolkit-containers](https://github.com/vfonov/minc-toolkit-containers)
 - License: None

