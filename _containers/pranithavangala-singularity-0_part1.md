---
id: 2140
name: "pranithavangala/singularity"
branch: "master"
tag: "0_part1"
commit: "929502f4239d695f53e616d7f2b6bf5bb4910b2d"
version: "4cbe2fa7a71a85fc1916f9e5dc552627"
build_date: "2021-03-16T15:48:20.933Z"
size_mb: 1627
size: 570581023
sif: "https://datasets.datalad.org/shub/pranithavangala/singularity/0_part1/2021-03-16-929502f4-4cbe2fa7/4cbe2fa7a71a85fc1916f9e5dc552627.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pranithavangala/singularity/0_part1/2021-03-16-929502f4-4cbe2fa7/
recipe: https://datasets.datalad.org/shub/pranithavangala/singularity/0_part1/2021-03-16-929502f4-4cbe2fa7/Singularity
collection: pranithavangala/singularity
---

# pranithavangala/singularity:0_part1

```bash
$ singularity pull shub://pranithavangala/singularity:0_part1
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:latest

%labels

    AUTHOR Pranitha Vangala <pranitha.vangala@gmail.com>
    Version v1.0

# 2. This is how to copy files for >= 2.3, each line is a pair of <source> < destination>
#%files
#    avocados.txt # added to the root of the image
#    avocados.txt /opt # added to the directory opt

%environment
    export SRC=/usr/local/src
    export BIN=/usr/local/bin
    export R_VERSION=R-3.4.3
    

%post

apt-get update && apt-get install -y gcc g++ perl python automake make \
                                       wget git curl libdb-dev \
                                       zlib1g-dev bzip2 libncurses5-dev \
				       texlive-latex-base \
                                       default-jre \
				       python-pip python-dev \
				       gfortran libssl-dev\
				       build-essential libghc-zlib-dev libncurses-dev libbz2-dev liblzma-dev libpcre3-dev libxml2-dev \
				       libblas-dev gfortran git unzip ftp libzmq3-dev nano ftp fort77 libreadline-dev \
				       libcurl4-openssl-dev libx11-dev libxt-dev \
				       x11-common libcairo2-dev libpng12-dev libreadline6-dev libjpeg8-dev pkg-config libtbb-dev \
                   && apt-get clean

curl -L https://cpanmin.us | perl - App::cpanminus

cpanm install DB_File

cpanm install URI::Escape

## set up tool config and deployment area:

export SRC=/usr/local/src
export BIN=/usr/local/bin
```

## Collection

 - Name: [pranithavangala/singularity](https://github.com/pranithavangala/singularity)
 - License: None

