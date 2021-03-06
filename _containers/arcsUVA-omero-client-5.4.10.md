---
id: 8435
name: "arcsUVA/omero-client"
branch: "master"
tag: "5.4.10"
commit: "2cc87ab91751f68289d2b7ed76509575308d9ebe"
version: "289c64c34acb6ffa7ba8886a5d3fc9fe"
build_date: "2020-05-01T18:29:36.072Z"
size_mb: 3783
size: 1266651167
sif: "https://datasets.datalad.org/shub/arcsUVA/omero-client/5.4.10/2020-05-01-2cc87ab9-289c64c3/289c64c34acb6ffa7ba8886a5d3fc9fe.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/arcsUVA/omero-client/5.4.10/2020-05-01-2cc87ab9-289c64c3/
recipe: https://datasets.datalad.org/shub/arcsUVA/omero-client/5.4.10/2020-05-01-2cc87ab9-289c64c3/Singularity
collection: arcsUVA/omero-client
---

# arcsUVA/omero-client:5.4.10

```bash
$ singularity pull shub://arcsUVA/omero-client:5.4.10
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04


%post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this will install all necessary packages and prepare the container

    OMERO_VERSION=5.4.10-ice36-b105
    OMERO_ROOT=/opt/omero

    apt-get -y update --fix-missing

    # install cuDNN and accessories
    apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        db5.3-util \
        libssl-dev \
        libbz2-dev \
        libmcpp-dev \
        libdb++-dev \
        libdb-dev \
        nginx \
        libtiff5-dev \
        libjpeg8-dev \
        zlib1g-dev \
        libfreetype6-dev \
        liblcms2-dev \
        libwebp-dev \
        tcl8.6-dev \
        tk8.6-dev \
        unzip \
        default-jdk

    # install other tools and dependencies
    apt-get -y install --allow-downgrades --no-install-recommends \
        dbus \
        wget \
        git \
        mercurial \
        subversion \
        vim \
        nano \

#    dbus-uuidgen --ensure=/etc/machine-id

    # install anaconda 
    wget --no-check-certificate https://repo.continuum.io/archive/Anaconda2-5.2.0-Linux-x86_64.sh -O ~/anaconda.sh
    /bin/bash ~/anaconda.sh -b -p /opt/conda
    rm ~/anaconda.sh
    export PATH=/opt/conda/bin:$PATH
    conda install pip

    # install Ice 3.6
    pip install zeroc-ice==3.6

    # install OMERO.insight
    mkdir -p $OMERO_ROOT
    cd $OMERO_ROOT
    wget https://downloads.openmicroscopy.org/omero/5.4.10/artifacts/OMERO.insight-${OMERO_VERSION}-linux.zip --no-check-certificate -O ./omero-insight.zip
    unzip omero-insight.zip
    mv OMERO.insight-${OMERO_VERSION}-linux OMERO.insight

    # install OMERO Python bindings
    cd $OMERO_ROOT
    wget http://downloads.openmicroscopy.org/omero/5.4.10/artifacts/OMERO.server-${OMERO_VERSION}.zip --no-check-certificate -O ./omeropy.zip
    unzip omeropy.zip
    mv OMERO.server-${OMERO_VERSION} OMERO.server

    # clean up to reduce disk space required during installation
    conda clean --index-cache --tarballs --packages --yes
    rm omeropy.zip
    rm omero-insight.zip

%runscript
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this text code will run whenever the container
# is called as an executable or with `singularity run`
exec python $@

%help
This container provides the Python 2.7 bindings for:
    * Omero 5.4.10 (CLI and Python bindings)

%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container

    export ANACONDA_HOME=/opt/conda
    export PATH="$ANACONDA_HOME/bin:$PATH"
    unset CONDA_DEFAULT_ENV

    OMERO_ROOT=/opt/omero
    export PATH="$OMERO_ROOT/OMERO.server/bin:$OMERO_ROOT/OMERO.insight:$PATH"
    export PYTHONPATH=$OMERO_ROOT/OMERO.server/lib/python:$PYTHONPATH
```

## Collection

 - Name: [arcsUVA/omero-client](https://github.com/arcsUVA/omero-client)
 - License: None

