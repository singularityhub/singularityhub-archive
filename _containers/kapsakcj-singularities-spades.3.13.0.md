---
id: 8552
name: "kapsakcj/singularities"
branch: "master"
tag: "spades.3.13.0"
commit: "016d5784764d2e4e82b20cf2b226b36ba801f4c4"
version: "ed5e8f8a26d615628fff0eb2c6e256fa"
build_date: "2019-08-15T03:18:12.930Z"
size_mb: 318
size: 113897503
sif: "https://datasets.datalad.org/shub/kapsakcj/singularities/spades.3.13.0/2019-08-15-016d5784-ed5e8f8a/ed5e8f8a26d615628fff0eb2c6e256fa.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kapsakcj/singularities/spades.3.13.0/2019-08-15-016d5784-ed5e8f8a/
recipe: https://datasets.datalad.org/shub/kapsakcj/singularities/spades.3.13.0/2019-08-15-016d5784-ed5e8f8a/Singularity
collection: kapsakcj/singularities
---

# kapsakcj/singularities:spades.3.13.0

```bash
$ singularity pull shub://kapsakcj/singularities:spades.3.13.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7.6.1810

%help
### This is the help for building a singularity image from a recipe (sudo priveleges required).
### To build me into an image, run:
    sudo singularity build my-new-spades-image.simg /path/to/spades/3.13.0/Singularity
### If the image already exists, add the --force flag to overwrite
    sudo singularity build --force my-new-spades-image.simg /path/to/spades/3.13.0/Singularity

#### Then to run in an interactive shell run:
    singularity shell my-new-spades-image.simg
    spades.py [spades options]

#### To run without interactive shell
    singularity exec my-new-spades-image.simg spades.py [spades options]

%labels
    MAINTAINER Curtis Kapsak
    SINGULARITY-IMAGE-VERSION 1.0.0
    SOFTWARE-VERSION 3.13.0

%environment
    PATH=${PATH}:/SPAdes-3.13.0-Linux/bin
    export PATH

%post
    yum -y update
    yum -y install wget python
    wget http://cab.spbu.ru/files/release3.13.0/SPAdes-3.13.0-Linux.tar.gz
    tar -xzf SPAdes-3.13.0-Linux.tar.gz
    rm -r SPAdes-3.13.0-Linux.tar.gz
    mkdir /data

%runscript
    echo "This runscript shows SPAdes help options"
    spades.py --help
    echo ""
    echo ""
    echo ""
    echo 'Run "singularity help name-of-spades-image.simg" for more help on running the image'
    echo ""
```

## Collection

 - Name: [kapsakcj/singularities](https://github.com/kapsakcj/singularities)
 - License: [MIT License](https://api.github.com/licenses/mit)

