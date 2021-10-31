---
id: 5765
name: "bcdarwin/minc-toolkit-containers"
branch: "master"
tag: "1.9.16"
commit: "df4202ee09dd9a9684472b9a6ab4ad251c3939be"
version: "2b89645d569bdddd90f57d68a730f9c1"
build_date: "2018-12-01T16:42:26.390Z"
size_mb: 4833
size: 1506779167
sif: "https://datasets.datalad.org/shub/bcdarwin/minc-toolkit-containers/1.9.16/2018-12-01-df4202ee-2b89645d/2b89645d569bdddd90f57d68a730f9c1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bcdarwin/minc-toolkit-containers/1.9.16/2018-12-01-df4202ee-2b89645d/
recipe: https://datasets.datalad.org/shub/bcdarwin/minc-toolkit-containers/1.9.16/2018-12-01-df4202ee-2b89645d/Singularity
collection: bcdarwin/minc-toolkit-containers
---

# bcdarwin/minc-toolkit-containers:1.9.16

```bash
$ singularity pull shub://bcdarwin/minc-toolkit-containers:1.9.16
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: bcdarwin/minc-toolkit-containers:base

# install minc packages
%post
    set -e

    # install minc-toolkit 1.9.16
    MINC_TOOLKIT_VERSION_BASE="1.9.16"
    MINC_TOOLKIT_VERSION="${MINC_TOOLKIT_VERSION_BASE}-20180117"
    wget http://packages.bic.mni.mcgill.ca/minc-toolkit/Debian/minc-toolkit-${MINC_TOOLKIT_VERSION}-Ubuntu_18.04-x86_64.deb
    dpkg -i minc-toolkit-${MINC_TOOLKIT_VERSION}-Ubuntu_18.04-x86_64.deb
    rm -f minc-toolkit-${MINC_TOOLKIT_VERSION}-Ubuntu_18.04-x86_64.deb
    wget http://packages.bic.mni.mcgill.ca/minc-toolkit/Debian/beast-library-1.1.0-20121212.deb
    dpkg -i beast-library-1.1.0-20121212.deb
    rm -f beast-library-1.1.0-20121212.deb
    wget http://packages.bic.mni.mcgill.ca/minc-toolkit/Debian/bic-mni-models-0.1.1-20120421.deb
    dpkg -i bic-mni-models-0.1.1-20120421.deb
    rm -f bic-mni-models-0.1.1-20120421.deb

    apt-get autoclean 
    rm -rf /var/lib/apt/lists/*

    #pip3 install pip setuptools wheel typing --upgrade

    # needed since the minc-toolkit-config.sh break Debian's system numpy and
    # and minc2-based programs we install have broken setup.py files so don't install it themselves:
    . /opt/minc/1.9.16/minc-toolkit-config.sh && pip2 install numpy

    # install minc-stuffs (automatically installs Pyminc)
    git clone --recursive https://github.com/Mouse-Imaging-Centre/minc-stuffs.git && \
    . /opt/minc/1.9.16/minc-toolkit-config.sh && \
    cd minc-stuffs && \
    ./autogen.sh && \
    ./configure --with-minc2 --with-build-path=/opt/minc/1.9.16 && \
    make && make install && \
    python3 setup.py install && \
    cd .. && rm -rf minc-stuffs
    
    # install RMINC
    RMINC_VERSION=1.5.2.1
    . /opt/minc/1.9.16/minc-toolkit-config.sh && \
    wget https://github.com/Mouse-Imaging-Centre/RMINC/archive/v${RMINC_VERSION}.tar.gz && \
    R CMD INSTALL v${RMINC_VERSION}.tar.gz --configure-args='--with-build-path=/opt/minc/1.9.16' && \
    rm -f RMINC_${RMINC_VERSION}.tar.gz

    # install Pydpiper
    PYDPIPER_VERSION=2.0.12
    . /opt/minc/1.9.16/minc-toolkit-config.sh && \
    wget https://github.com/Mouse-Imaging-Centre/pydpiper/archive/v${PYDPIPER_VERSION}.tar.gz && \
    tar zxf v${PYDPIPER_VERSION}.tar.gz && \
    cd pydpiper-${PYDPIPER_VERSION} && \
    python3 setup.py install && \
    cd .. && rm -rf v${PYDPIPER_VERSION}.tar.gz

    # install pyezminc, minc2-simple
    . /opt/minc/1.9.16/minc-toolkit-config.sh && \
    wget https://github.com/BIC-MNI/pyezminc/archive/release-1.2.01.tar.gz && \
    pip2 install release-1.2.01.tar.gz --no-cache-dir && \
    pip3 install release-1.2.01.tar.gz --no-cache-dir && \
    wget https://github.com/vfonov/minc2-simple/archive/v0.tar.gz && \
    tar zxf v0.tar.gz && \
    python2 minc2-simple-0/python/setup.py install && \
    python3 minc2-simple-0/python/setup.py install && \
    rm -rf v0.tar.gz release-1.2.01.tar.gz minc2-simple-0 
    
    echo ". /opt/minc/1.9.16/minc-toolkit-config.sh" >> $SINGULARITY_ENVIRONMENT

%labels
    Maintainer Vladimir S. Fonov
    AUTHOR vladimir.fonov@gmail.com
    Version 1.9.16
```

## Collection

 - Name: [bcdarwin/minc-toolkit-containers](https://github.com/bcdarwin/minc-toolkit-containers)
 - License: None

