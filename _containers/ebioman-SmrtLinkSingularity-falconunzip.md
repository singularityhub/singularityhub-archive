---
id: 4036
name: "ebioman/SmrtLinkSingularity"
branch: "add-license-1"
tag: "falconunzip"
commit: "d3989f674ce797c65818ceaab3ba470988e8bbfc"
version: "42e46734a86a71b8898263322ea1da87"
build_date: "2018-08-17T18:19:56.386Z"
size_mb: 1530
size: 617795615
sif: "https://datasets.datalad.org/shub/ebioman/SmrtLinkSingularity/falconunzip/2018-08-17-d3989f67-42e46734/42e46734a86a71b8898263322ea1da87.simg"
url: https://datasets.datalad.org/shub/ebioman/SmrtLinkSingularity/falconunzip/2018-08-17-d3989f67-42e46734/
recipe: https://datasets.datalad.org/shub/ebioman/SmrtLinkSingularity/falconunzip/2018-08-17-d3989f67-42e46734/Singularity
collection: ebioman/SmrtLinkSingularity
---

# ebioman/SmrtLinkSingularity:falconunzip

```bash
$ singularity pull shub://ebioman/SmrtLinkSingularity:falconunzip
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest

%labels
Maintainer by Emanuel Schmid @ VITAL-IT
Version v2018.03.12-04.00


%help
Welcome to the FALCON falcon-2018.03.12-04.00 installation!
This is the current stable FALCON binary installation

Please invoke tools using "singularity exec --bind $PWD thisImage.img myCommand"
valid ones are e.g.: blasr,quiver,pbalign,....

%post

# install software
yum update -y -q && yum install -y -q \
        build-essential \
        gcc-multilib \
        libboost-all-dev \
        libhdf5-serial-dev \
        zlib1g-dev \
        pkg-config \
        wget \
        rsync \
        unzip \
        which \
        bzip2 \
        dirname

TARBALL="falcon-2018.03.12-04.00-py2.7-ucs4.tar.gz"
wget -c https://downloads.pacbcloud.com/public/falcon/$TARBALL --no-check-certificate
PREFIX=/usr/local/miniconda

wget https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh -O miniconda.sh --no-check-certificate
bash miniconda.sh -b -p $PREFIX
export PATH="$PREFIX/bin/:$PATH"
conda config --add channels conda-forge
conda config --add channels defaults
conda config --add channels bioconda
conda install -y mummer minimap2
conda install -y -c conda-forge -c bioconda samtools bzip2 ncurses
tar -xvzf ${TARBALL} -C ${PREFIX}



%environment
export LD_LIBRARY_PATH=/usr/local/miniconda/lib/:${LD_LIBRARY_PATH}
export PATH=/usr/local/miniconda/bin/:/bin/:${PATH}
export PYTHONPATH=/usr/local/miniconda/lib/python2.7/site-packages

%runscript
exec /bin/bash "$@"
```

## Collection

 - Name: [ebioman/SmrtLinkSingularity](https://github.com/ebioman/SmrtLinkSingularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

