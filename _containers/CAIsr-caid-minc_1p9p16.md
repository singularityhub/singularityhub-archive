---
id: 3536
name: "CAIsr/caid"
branch: "master"
tag: "minc_1p9p16"
commit: "5d2ebec5a0f347d6da0cac9c6500acf78b4d2274"
version: "8ea42702197a90e55ef39b9226dcb70b"
build_date: "2018-07-13T21:19:58.998Z"
size_mb: 4046
size: 1237930015
sif: "https://datasets.datalad.org/shub/CAIsr/caid/minc_1p9p16/2018-07-13-5d2ebec5-8ea42702/8ea42702197a90e55ef39b9226dcb70b.simg"
url: https://datasets.datalad.org/shub/CAIsr/caid/minc_1p9p16/2018-07-13-5d2ebec5-8ea42702/
recipe: https://datasets.datalad.org/shub/CAIsr/caid/minc_1p9p16/2018-07-13-5d2ebec5-8ea42702/Singularity
collection: CAIsr/caid
---

# CAIsr/caid:minc_1p9p16

```bash
$ singularity pull shub://CAIsr/caid:minc_1p9p16
```

## Singularity Recipe

```singularity
#Bootstrap: localimage
#From: /home/vfonov/src/minc-toolkit-containers/singularity/minc-toolkit-base.simg
Bootstrap: shub
From: vfonov/minc-toolkit-containers:base


# install minc packages
%post
    # update locales
    locale-gen en_US.UTF-8 en_US en_CA.UTF-8 en_CA
    dpkg-reconfigure locales


    mkdir /90days /30days /QRISdata /RDS /data /short /gpfs1 /proc_temp /TMPDIR /nvme /local
    # install minc-toolkit 1.9.16
    wget http://packages.bic.mni.mcgill.ca/minc-toolkit/Debian/minc-toolkit-1.9.16-20180117-Ubuntu_16.04-x86_64.deb
    dpkg -i minc-toolkit-1.9.16-20180117-Ubuntu_16.04-x86_64.deb
    rm -f minc-toolkit-1.9.16-20180117-Ubuntu_16.04-x86_64.deb 
    wget http://packages.bic.mni.mcgill.ca/minc-toolkit/Debian/beast-library-1.1.0-20121212.deb 
    dpkg -i beast-library-1.1.0-20121212.deb 
    rm -f beast-library-1.1.0-20121212.deb 
    wget http://packages.bic.mni.mcgill.ca/minc-toolkit/Debian/bic-mni-models-0.1.1-20120421.deb 
    dpkg -i bic-mni-models-0.1.1-20120421.deb 
    rm -f bic-mni-models-0.1.1-20120421.deb
    
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

 - Name: [CAIsr/caid](https://github.com/CAIsr/caid)
 - License: None

