---
id: 4111
name: "ffineis/nurcs-singularity"
branch: "master"
tag: "openmpi"
commit: "81da3eb026e814c1aa6737737c8a0dd69900896c"
version: "5fb6df7fc3be06d50b64c58e50438478"
build_date: "2018-08-21T22:48:51.890Z"
size_mb: 1212
size: 520618015
sif: "https://datasets.datalad.org/shub/ffineis/nurcs-singularity/openmpi/2018-08-21-81da3eb0-5fb6df7f/5fb6df7fc3be06d50b64c58e50438478.simg"
url: https://datasets.datalad.org/shub/ffineis/nurcs-singularity/openmpi/2018-08-21-81da3eb0-5fb6df7f/
recipe: https://datasets.datalad.org/shub/ffineis/nurcs-singularity/openmpi/2018-08-21-81da3eb0-5fb6df7f/Singularity
collection: ffineis/nurcs-singularity
---

# ffineis/nurcs-singularity:openmpi

```bash
$ singularity pull shub://ffineis/nurcs-singularity:openmpi
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%post

    # ------------------------------------------------ #
    #                   Kernel overhead                #
    # ------------------------------------------------ #

    apt-get -y update && apt-get -y upgrade
    apt-get -y --allow-unauthenticated install \
        apt-utils \
        autoconf \
        automake \
        make \
        cmake \
        build-essential \
        zlib1g-dev \
        libncurses5-dev \
        libssl-dev \
        libffi-dev \
        locales \
        gfortran \
        libtool \
        wget \
        git \
        zip \
        pkg-config \
        python-dev \
        python-pip \
        openmpi-bin \
        libcr-dev \
        mpich \
        mpich-doc

    locale-gen "en_US.UTF-8"
    dpkg-reconfigure locales
    export LANGUAGE="en_US.UTF-8"
    echo 'LANGUAGE="en_US.UTF-8"' >> /etc/default/locale
    echo 'LC_ALL="en_US.UTF-8"' >> /etc/default/locale

    # ------------------------------------------------ #
    #    Scientific computing packages for Python2     #
    # ------------------------------------------------ #

    pip install numpy # requisite for everything else
    pip install cython \
        pandas \
        feather-format \
        mock \
        scipy \
        sklearn \
        matplotlib \
        nose \
        mlpy \
        nltk \
        statsmodels \
        opencv-python \
        biopython

    # mission critical - mpi4py package
    pip install mpi4py


%files

    mpi_hello.py /opt
    singularity_logo.txt /opt


%runscript

    cat /opt/singularity_logo.txt


%test

    mpirun --allow-run-as-root -np 1 python /opt/mpi_hello.py
```

## Collection

 - Name: [ffineis/nurcs-singularity](https://github.com/ffineis/nurcs-singularity)
 - License: None

