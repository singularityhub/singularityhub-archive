---
id: 924
name: "marcc-hpc/cellrangerdev"
branch: "v2.0.2"
tag: "latest"
commit: "a6c999c1ea87b2500b2c7d6105c18cb1c2d45d08"
version: "7136dc8ce599418dcd04a018902618a8"
build_date: "2017-11-23T00:35:31.364Z"
size_mb: 4849
size: 1801125919
sif: "https://datasets.datalad.org/shub/marcc-hpc/cellrangerdev/latest/2017-11-23-a6c999c1-7136dc8c/7136dc8ce599418dcd04a018902618a8.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/cellrangerdev/latest/2017-11-23-a6c999c1-7136dc8c/
recipe: https://datasets.datalad.org/shub/marcc-hpc/cellrangerdev/latest/2017-11-23-a6c999c1-7136dc8c/Singularity
collection: marcc-hpc/cellrangerdev
---

# marcc-hpc/cellrangerdev:latest

```bash
$ singularity pull shub://marcc-hpc/cellrangerdev:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From:  ubuntu:17.04

######
%setup
######
# initial setups from outside the container
# this is run from outside the container to start setting it up

echo "Looking in directory '$SINGULARITY_ROOTFS' for /bin/sh"
if [ ! -x "$SINGULARITY_ROOTFS/bin/sh" ]; then
  echo "Hrmm, this container does not have /bin/sh installed..."
  exit 1
fi

# for SDSC mounts
mkdir -p $SINGULARITY_ROOTFS/oasis/tscc/scratch
mkdir -p $SINGULARITY_ROOTFS/projects/ps-yeolab
mkdir -p $SINGULARITY_ROOTFS/projects/ps-yeolab3
mkdir -p $SINGULARITY_ROOTFS/projects/ps-scrm
mkdir -p $SINGULARITY_ROOTFS/oasis/projects/nsf

# for Cincinnati Chidren's Hospital mounts
mkdir -p $SINGULARITY_ROOTFS/users
mkdir -p $SINGULARITY_ROOTFS/data
mkdir -p $SINGULARITY_ROOTFS/scratch

# for West Virginia University mounts
mkdir -p $SINGULARITY_ROOTFS/users
mkdir -p $SINGULARITY_ROOTFS/gpfs
mkdir -p $SINGULARITY_ROOTFS/groups

# for Alain's laptop
mkdir -p $SINGULARITY_ROOTFS/media/mis

# for Maryland Advanced Research Computing Center (MARCC is Mar-see)
mkdir -p $SINGULARITY_ROOTFS/home-0
mkdir -p $SINGULARITY_ROOTFS/home-1
mkdir -p $SINGULARITY_ROOTFS/home-2
mkdir -p $SINGULARITY_ROOTFS/home-3
mkdir -p $SINGULARITY_ROOTFS/home-4
  
mkdir -p $SINGULARITY_ROOTFS/opt/reference
mkdir -p $SINGULARITY_ROOTFS/opt/dataset
mkdir -p $SINGULARITY_ROOTFS/opt/template

mkdir -p $SINGULARITY_ROOTFS/opt/members
mkdir -p $SINGULARITY_ROOTFS/opt/patches

mkdir -p $SINGULARITY_ROOTFS/opt/bin
mkdir -p $SINGULARITY_ROOTFS/opt/cwl
mkdir -p $SINGULARITY_ROOTFS/opt/wf

###
%post
###

# running post scriptlet
# this is run inside the container to install all necessary packages

# set -o xtrace
set -o nounset
set -o errexit
# set -o pipefail

########
# UBUNTU

# ubuntu does not have bash in /usr/bin/env ?
ln -s /bin/bash /usr/bin/bash

apt-get -y update
apt-get -y install nano unzip zip
apt-get -y install build-essential # we need compilers
apt-get -y install libboost-all-dev gzip
apt-get -y install libbz2-dev # bzip2 down in miniconda
apt-get -y install libz-dev

# cleanup x? M
apt-get clean

# fix for /bin/gtar: not found when running devtools::install_git()
ln -s /bin/tar /bin/gtar

###########
# MINICONDA
#
# instead of having: From: continuumio/miniconda:4.3.11
# from https://hub.docker.com/r/continuumio/miniconda/~/dockerfile/

# ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

apt-get update --fix-missing

apt-get install -y wget bzip2 ca-certificates \
  libglib2.0-0 libxext6 libsm6 libxrender1 \
  git mercurial subversion

# py2
# wget --quiet https://repo.continuum.io/miniconda/Miniconda2-4.3.14-Linux-x86_64.sh -O ~/miniconda.sh
# py3
wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh

/bin/bash ~/miniconda.sh -b -p /opt/conda
rm ~/miniconda.sh

# this is required here as the environment section is not processed yet
PATH=/opt/conda/bin:$PATH
export PATH

/opt/conda/bin/conda install -y -c conda-forge \
  python=3.6.1 setuptools=36.3.0 nodejs=6.11.0 openpyxl=2.4.8 pandas=0.20.3
/opt/conda/bin/pip install --upgrade pip
/opt/conda/bin/pip install cwltool==1.0.20170828135420

############
# CELLRANGER
#

cd /opt
# 10x genomics website links expires quickly
# wget -O cellranger-2.0.2.tar.gz "http://cf.10xgenomics.com/releases/cell-exp/cellranger-2.0.2.tar.gz?Expires=1505243477&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cDovL2NmLjEweGdlbm9taWNzLmNvbS9yZWxlYXNlcy9jZWxsLWV4cC9jZWxscmFuZ2VyLTIuMC4yLnRhci5neiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTUwNTI0MzQ3N319fV19&Signature=m9aA~g6TX18pk-EuoUMSYyBbWzTpdq737D7MZ6HfyucRBTnwo84kFgU5UOCDUMrNUoI7AGL35mjKQm34~~Mzy~knhpe1IcawIRcjUqx3vqDdrpZNIpGaLS6-znlr6MExSGz5UtS6BeBdWsTb4lwWlqO0~Tu~AcNH3BJ-n88Mi1EBiYrzdYTFYyLsJUsd~0h~l6RIu9PdYCBR6as4ImtExOTtpomx2QdWVuY3Rrb7MwGxjfyQA~s4st8FhsDGZnEkKqij0LR5AcC6cfeWL6lZ2J6ei2eGL35lLBYDdWDC~uO011mqlAoozyTT3UUq4CQ5Nx42FZujxRUsYr~TPC7s8Q__&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA"
# using alternative download from google cloud
if [ ! -f  /opt/cellranger-2.0.2.tar.gz ]
then
  wget -O cellranger-2.0.2.tar.gz "https://storage.googleapis.com/singularity-cellranger/cellranger-2.0.2.tar.gz"
fi
tar -xzf cellranger-2.0.2.tar.gz
mv cellranger-2.0.2 10x
rm cellranger-2.0.2.tar.gz

cd -

############
# BCL2FASTQ2
#

# Notes:
# https://nhoffman.github.io/borborygmi/compiling-bcl2fastq-on-ubuntu.html
# http://seqanswers.com/forums/showthread.php?t=11106
# https://biogist.wordpress.com/2012/10/23/casava-1-8-2-installation/
mkdir -p /usr/include/sys
ln -s /usr/include/x86_64-linux-gnu/sys/stat.h /usr/include/sys/stat.h
#ln -s /usr/lib/x86_64-linux-gnu/libbz2* /usr/lib
#ln -s /usr/lib/x86_64-linux-gnu/libz* /usr/lib

cd /opt
if [ ! -f  bcl2fastq2-v2-20-0-tar.zip ]
then
   wget ftp://webdata2:webdata2@ussd-ftp.illumina.com/downloads/software/bcl2fastq/bcl2fastq2-v2-20-0-tar.zip
fi
unzip bcl2fastq2-v2-20-0-tar.zip
tar xf bcl2fastq2-v2.20.0.422-Source.tar.gz
rm bcl2fastq2-v2-20-0-tar.zip
rm bcl2fastq2-v2.20.0.422-Source.tar.gz
cd -

SOURCE=/opt/bcl2fastq
BUILD=/opt/bcl2fastq2-build
INSTALL_DIR=/opt/bcl2fastq2

# make this critical update for boost https://gist.github.com/jblachly/f8dc0f328d66659d9ee005548a5a2d2e
sed -i.bak /opt/bcl2fastq/src/cxx/lib/io/Xml.cpp -e "s#xml_writer_make_settings(#xml_writer_make_settings<ptree::key_type>(#"

# build it
mkdir ${BUILD}
cd ${BUILD}
${SOURCE}/src/configure --prefix=${INSTALL_DIR}
make
make install

# cleanup 454 MB
/opt/conda/bin/conda clean --index-cache --tarballs --packages --yes

chmod --recursive +755 /opt/*

set +x

##########
%environment
##########

PATH=/opt/conda/bin:$PATH
PATH=/opt/bcl2fastq2/bin:$PATH
PATH=/opt/10x:$PATH
PATH=/opt/bin:$PATH
PATH=/opt/cwl:$PATH
PATH=/opt/wf:$PATH
PATH=/opt/members/cellrangerget:$PATH
export PATH

alias echopathtr='echo $PATH | tr ":" "\n"'
alias ll='ls -lhF'

CELLRANGER_REPO=/opt/
export CELLRANGER_REPO

CELLRANGER_TEMPLATE=/opt/template
export CELLRANGER_TEMPLATE

######
%labels
######
# Forked from Alain Domissy Singularity File MAINTAINER alaindomissy@gmail.com
VERSION 2.0.2
BUILD_DATE "${date -Iminutes}"

####
%files
####
# TODO permissions will nbe 700 !
# documentation      /opt/
# tests              /opt/

########
%runscript
########
# this will get copied to /.singularity.d/runscript indide the container
# which will run whenever the container is called as an executable

echo
echo Container image downloaded
echo

#set -o xtrace
set -o nounset
#set -o errexit
#set -o pipefail

if [ $# -eq 0 ]
then
  echo
  echo "===================================================================="
  echo "See example usage at
  echo "https://github.com/marcc-hpc/cellrangerdev
  echo "===================================================================="
  echo
else
  exec /opt/10x/cellranger "$@"
fi

#####
%test
#####

# cellranger testrun --id=tiny
```

## Collection

 - Name: [marcc-hpc/cellrangerdev](https://github.com/marcc-hpc/cellrangerdev)
 - License: None

