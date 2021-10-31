---
id: 34
name: "YeoLab/cellrangerdev"
branch: "master"
tag: "latest"
commit: "e36c0aa321450df5f25834e906f8ee950856c8ea"
version: "1b742881fa63e939a37e1252e96bab09"
build_date: "2021-04-14T23:19:48.158Z"
size_mb: 3517
size: 1456234527
sif: "https://datasets.datalad.org/shub/YeoLab/cellrangerdev/latest/2021-04-14-e36c0aa3-1b742881/1b742881fa63e939a37e1252e96bab09.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/YeoLab/cellrangerdev/latest/2021-04-14-e36c0aa3-1b742881/
recipe: https://datasets.datalad.org/shub/YeoLab/cellrangerdev/latest/2021-04-14-e36c0aa3-1b742881/Singularity
collection: YeoLab/cellrangerdev
---

# YeoLab/cellrangerdev:latest

```bash
$ singularity pull shub://YeoLab/cellrangerdev:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From:  ubuntu:16.04

  ####
%setup
  ####
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


  mkdir -p $SINGULARITY_ROOTFS/opt/condaenvexports
  mkdir -p $SINGULARITY_ROOTFS/opt/donewith

  mkdir -p $SINGULARITY_ROOTFS/opt/reference
  mkdir -p $SINGULARITY_ROOTFS/opt/dataset
  mkdir -p $SINGULARITY_ROOTFS/opt/template

  mkdir -p $SINGULARITY_ROOTFS/opt/members
  mkdir -p $SINGULARITY_ROOTFS/opt/patches

  mkdir -p $SINGULARITY_ROOTFS/opt/bin
  mkdir -p $SINGULARITY_ROOTFS/opt/cwl
  mkdir -p $SINGULARITY_ROOTFS/opt/wf


  # these are needed early for post section - not really ?

 cp -r ./reference/* $SINGULARITY_ROOTFS/opt/reference/
 cp -r ./dataset/* $SINGULARITY_ROOTFS/opt/dataset/
 cp -r ./template/* $SINGULARITY_ROOTFS/opt/template/

  cp -r ./members/*  $SINGULARITY_ROOTFS/opt/members/
  cp -r ./patches/*  $SINGULARITY_ROOTFS/opt/patches/

  cp -r ./bin/*  $SINGULARITY_ROOTFS/opt/bin/
  cp -r ./cwl/*  $SINGULARITY_ROOTFS/opt/cwl/
  cp -r ./wf/*  $SINGULARITY_ROOTFS/opt/wf/


  # will be downloading from google cloud
  # unless if file is present for local laptop build
  if [ -f ./downloads/cellranger-2.0.2.tar.gz ]
  then
      cp   ./downloads/cellranger-2.0.2.tar.gz $SINGULARITY_ROOTFS/opt/
  fi
  if [ -f ./downloads/bcl2fastq2-v2-20-0-tar.zip ]
  then
      cp   ./downloads/bcl2fastq2-v2-20-0-tar.zip $SINGULARITY_ROOTFS/opt/
  fi

  # TODO
  # cp refdata/refdata-cellranger-ercc92-1.2.0.tar.gz $SINGULARITY_ROOTFS/opt/


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

  # ubuntu does not have bash in /usr/bin/env ??
  ln -s /bin/bash /usr/bin/bash

  apt-get -y update
  apt-get -y install nano unzip zip
  # apt-get -y install make gcc g++ zlib1g-dev libncurses5-dev nano unzip zip
  # apt-get install -y xorg
  # g++ --version

  # cleanup   x? M
  apt-get clean


  # fix for /bin/gtar: not found when running devtools::install_git()
  ln -s /bin/tar /bin/gtar

  echo
  touch /opt/donewith/ubuntu
  echo "-----------------------------------------------"


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

  #echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh

  # py2
  # wget --quiet https://repo.continuum.io/miniconda/Miniconda2-4.3.14-Linux-x86_64.sh -O ~/miniconda.sh
  # py3
  wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh

  /bin/bash ~/miniconda.sh -b -p /opt/conda
  rm ~/miniconda.sh

  #apt-get install -y curl grep sed dpkg
  #TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'`
  #curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb
  #dpkg -i tini.deb
  #rm tini.deb
  #apt-get clean

  #ENV PATH /opt/conda/bin:$PATH
  #ENTRYPOINT [ "/usr/bin/tini", "--" ]
  #CMD [ "/bin/bash" ]

  # this is required here as the environment section is not processed yet
  PATH=/opt/conda/bin:$PATH
  export PATH

  echo
  touch /opt/donewith/miniconda
  echo "-----------------------------------------------"

  /opt/conda/bin/conda install -y -c conda-forge \
      python=3.6.1 setuptools=36.3.0 nodejs=6.11.0 openpyxl=2.4.8 pandas=0.20.3
  /opt/conda/bin/pip install --upgrade pip
  /opt/conda/bin/pip install cwltool==1.0.20170828135420
  /opt/conda/bin/conda env export -n root > /opt/condaenvexports/root-0.0.1.yaml

  echo
  touch /opt/donewith/rootenv
  echo "-----------------------------------------------"


#  ###########
#  # JUPYTER
#  #
#  # jupyter=1.0.0
#  echo "-----------------------------------------------"
#  NAME=jupyternotebook
#  VERSION=5.0.0
#  echo "-----------------------------------------------"
#  conda create --yes -n jupyternotebook python=3.6.2 notebook=5.0.0
#  conda env export -n jupyternotebook > /opt/condaenvexports/jupyternotebook-5.0.0.yaml
#  PATH="/opt/conda/envs/jupyternotebook/bin:$PATH"
#  export PATH
#  JUPYTER_PATH=/opt/conda/envs/jupyternotebook/share/jupyter
#  export JUPYTER_PATH
#  KERNELS=${JUPYTER_PATH}/kernels
#  export KERNELS
#  mkdir -p $KERNELS
#  echo
#  touch /opt/donewith/jupyternotebook
#  echo "-----------------------------------------------"
#  echo
#  touch /opt/donewith/members_envs
#  echo "-----------------------------------------------"

  ######
  # node
  # conda install -c conda-forge nodejs

  ##########
  # openpyxl

  # conda create -n openpyxl-2.4.8 python=3.5 openpyxl=2.4.8
  # source activate openpyxl-2.4.8
  # conda env export > ~/eclipcondainstall/condaenv_openpyxl-2.4.8_0.yaml

  # conda install pandas=0.20.3
  # conda env export > ~/eclipcondainstall/condaenv_openpyxl-2.4.8_1.yaml


  ##########
  # cwltool

  # sourceactivateroot
  # conda create -n cwltool-1.0.20170525215327 python=2.7
  # source activate cwltool-1.0.20170525215327
  # conda env export > ~/eclipcondainstall/condaenv_cwltool-1.0.20170525215327_0.yaml

  # pip install cwltool

  ### Successfully installed
  #CacheControl-0.11.7 avro-1.8.2 certifi-2017.4.17 chardet-3.0.4
  #cwltool-1.0.20170525215327 idna-2.5 isodate-0.5.4 lockfile-0.12.2
  #mistune-0.7.4 pyparsing-2.2.0 rdflib-4.2.2 rdflib-jsonld-0.4.0
  #requests-2.18.1 ruamel.ordereddict-0.4.9 ruamel.yaml-0.15.9
  #schema-salad-2.5.20170428142041 shellescape-3.4.1 six-1.10.0
  #typing-3.5.3.0 urllib3-1.21.1


  # conda install setuptools
  # pip install --upgrade pip
  # pip uninstall cwltool
  # pip install cwltool




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
  # # ln -s /opt/cellranger-2.0.0/cellranger-tiny-ref/1.2.0   /opt/cellranger_refdata/refdata-cellranger-tiny-ref-1.2.0
  # # wget http://cf.10xgenomics.com/supp/cell-exp/chromium-shared-sample-indexes-plate.json
  # # wget http://cf.10xgenomics.com/supp/cell-exp/chromium-shared-sample-indexes-plate.csv
  cd -
  echo
  touch /opt/donewith/cellranger
  echo "-----------------------------------------------"

  ############
  # BCL2FASTQ2
  #
  cd /opt
  if [ ! -f  bcl2fastq2-v2-20-0-tar.zip ]
  then
      wget ftp://webdata2:webdata2@ussd-ftp.illumina.com/downloads/software/bcl2fastq/bcl2fastq2-v2-20-0-tar.zip
  fi
  unzip bcl2fastq2-v2-20-0-tar.zip
  rm bcl2fastq2-v2-20-0-tar.zip
  cd -
  echo
  touch /opt/donewith/bcl2fastq2
  echo "-----------------------------------------------"



  /opt/conda/bin/conda env export -n root > /opt/condaenvexports/root_$(date +%Y-%m-%d-%H-%M).yaml

  # cleanup 454 MB
  /opt/conda/bin/conda clean --index-cache --tarballs --packages --yes

  #chmod --recursive --changes +755 /opt/*
  chmod --recursive +755 /opt/*

  echo
  touch /opt/donewith/condaenvexportroot_condaclean_chmod
  echo "-----------------------------------------------"

  set +x


  ##########
%environment
  ##########

  #PATH=/opt/conda/bin:/usr/local/bin:/usr/bin:/bin
  PATH=/opt/conda/bin:$PATH
  # PATH=/opt/conda/envs/cellranger-2.0.2/bin:$PATH
  PATH=/opt/10x:$PATH
  PATH=/opt/bin:$PATH
  PATH=/opt/cwl:$PATH
  PATH=/opt/wf:$PATH
  PATH=/opt/members/cellrangerget:$PATH
  export PATH

  # HOSTIP=$(hostname -i)
  # export HOSTIP
  # JUPYTER_PATH=/opt/conda/envs/jupyternotebook/share/jupyter
  # export JUPYTER_PATH
  # KERNELS=${JUPYTER_PATH}/kernels
  # export KERNELS

  alias echopathtr='echo $PATH | tr ":" "\n"'
  alias ll='ls -lhF'

  #CELLRANGER_HOME=/opt/
  CELLRANGER_REPO=/opt/
  export CELLRANGER_REPO

  CELLRANGER_TEMPLATE=/opt/template
  export CELLRANGER_TEMPLATE

  ######
%labels
  ######
  #
  MAINTAINER alaindomissy@gmail.com
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
  echo Container image downloaded, now setting shortcuts
  echo -------------------------------------------------

  #set -o xtrace
  set -o nounset
  #set -o errexit
  #set -o pipefail

  if [ $# -eq 0 ]
  then
    IDATE=$(date -Iseconds)
    # IDATE=$(date -Iseconds | tr "\:" "-" | tr "T" "+")

    IMAGENAME=cellranger_${IDATE}_${SINGULARITY_NAME}
    mv ${SINGULARITY_NAME} ${IMAGENAME}
    ln -sf ${IMAGENAME} cellranger.img


    # cp -r /opt/conda/envs/jupyternotebook/share/jupyter/kernels   ./
    cp /opt/patches/scripts/*   ./


    ln -sf cellranger cellrangercwl
    ln -sf cellranger cellrangergetreference
    ln -sf cellranger cellrangergetdataset

    echo
    echo "===================================================================="
    echo "to complete this installation, please type:"
    echo
    echo "                     source SOURCEME                                "
    echo
    echo "then, enjoy cellranger !"
    echo "===================================================================="
    echo

    # scbatch_notebook

  else
      echo "cellranger image called with run and some arguments - did you mean to exec instead ?"
  fi

  ####
%test
  ####

  # /opt/tests/test
```

## Collection

 - Name: [YeoLab/cellrangerdev](https://github.com/YeoLab/cellrangerdev)
 - License: None

