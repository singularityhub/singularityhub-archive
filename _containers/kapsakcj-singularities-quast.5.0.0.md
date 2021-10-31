---
id: 8554
name: "kapsakcj/singularities"
branch: "master"
tag: "quast.5.0.0"
commit: "a0d2f44f31f165690e809d1470290c36662ce3ea"
version: "daa49f59645247ab3d508cedc6185b18"
build_date: "2019-04-30T20:21:09.227Z"
size_mb: 1035
size: 320782367
sif: "https://datasets.datalad.org/shub/kapsakcj/singularities/quast.5.0.0/2019-04-30-a0d2f44f-daa49f59/daa49f59645247ab3d508cedc6185b18.simg"
url: https://datasets.datalad.org/shub/kapsakcj/singularities/quast.5.0.0/2019-04-30-a0d2f44f-daa49f59/
recipe: https://datasets.datalad.org/shub/kapsakcj/singularities/quast.5.0.0/2019-04-30-a0d2f44f-daa49f59/Singularity
collection: kapsakcj/singularities
---

# kapsakcj/singularities:quast.5.0.0

```bash
$ singularity pull shub://kapsakcj/singularities:quast.5.0.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial

%help
### This is the help for building a singularity image from a recipe (sudo priveleges required).
### To build me into an image, run:
    sudo singularity build my-new-quast-image.simg /path/to/quast/5.0.0/Singularity.quast.5.0.0
### If the image already exists, add the --force flag to overwrite
    sudo singularity build --force my-new-quast-image.simg /path/to/quast/5.0.0/Singularity.quast.5.0.0

#### Then to run in an interactive shell run:
    singularity shell my-new-quast-image.simg
    quast.py [options]

#### To run without interactive shell
    singularity exec my-new-quast-image.simg quast.py [options]

%labels
    MAINTAINER Curtis Kapsak
    SINGULARITY-IMAGE-VERSION 1.0.0
    SOFTWARE-VERSION 5.0.0
    SOFTWARE-WEBSITE https://github.com/ablab/quast
    SOFTWARE-LICENSE https://github.com/ablab/quast/blob/master/LICENSE.txt

%environment

%post
    apt-get update
    apt-get -y install wget \
                       python \
                       zlib1g-dev \
                       pkg-config \
                       libfreetype6-dev \
                       libpng-dev \
                       wget \
                       g++ \
                       make \
                       perl \
                       python \
                       python-setuptools \
                       python-pip
    apt-get clean
    apt-get autoclean
    python -m pip install -U pip
    python -m pip install -U matplotlib
    wget https://downloads.sourceforge.net/project/quast/quast-5.0.0.tar.gz
    tar -xzf quast-5.0.0.tar.gz
    rm quast-5.0.0.tar.gz
    cd /quast-5.0.0
    /quast-5.0.0/setup.py install
    /quast-5.0.0/setup.py test
    mkdir /data

%runscript
    echo "This runscript shows QUAST help options"
    quast.py --help
    echo ""
    echo ""
    echo ""
    echo 'Run "singularity help name-of-quast-image.simg" for more help on running the image'
    echo ""
```

## Collection

 - Name: [kapsakcj/singularities](https://github.com/kapsakcj/singularities)
 - License: [MIT License](https://api.github.com/licenses/mit)

