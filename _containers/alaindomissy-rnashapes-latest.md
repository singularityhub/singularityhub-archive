---
id: 30
name: "alaindomissy/rnashapes"
branch: "master"
tag: "latest"
commit: "7d3779fdddf4b0cc6faad8856efb7b2bf1c20f4b"
version: "ee414f33bfac47984356d853088ad5f1"
build_date: "2021-04-12T21:46:41.689Z"
size_mb: 475
size: 131489823
sif: "https://datasets.datalad.org/shub/alaindomissy/rnashapes/latest/2021-04-12-7d3779fd-ee414f33/ee414f33bfac47984356d853088ad5f1.simg"
url: https://datasets.datalad.org/shub/alaindomissy/rnashapes/latest/2021-04-12-7d3779fd-ee414f33/
recipe: https://datasets.datalad.org/shub/alaindomissy/rnashapes/latest/2021-04-12-7d3779fd-ee414f33/Singularity
collection: alaindomissy/rnashapes
---

# alaindomissy/rnashapes:latest

```bash
$ singularity pull shub://alaindomissy/rnashapes:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From:ubuntu:14.04

# this would include the CMD line from the dockerfile
# ( here: CMD [ "/bin/bash" ] ) as the %runscript
# IncludeCmd: yes


###############################################################################
%setup
  # this is run from outside the container to start setting it up

  echo "Looking in directory '$SINGULARITY_ROOTFS' for /bin/sh"
  if [ ! -x "$SINGULARITY_ROOTFS/bin/sh" ]; then
      echo "Hrmm, this container does not have /bin/sh installed..."
      exit 1
  fi

  mkdir -p $SINGULARITY_ROOTFS/oasis/tscc/scratch
  mkdir -p $SINGULARITY_ROOTFS/projects/ps-yeolab
  mkdir -p $SINGULARITY_ROOTFS/projects/ps-yeolab3
  mkdir -p $SINGULARITY_ROOTFS/projects/ps-scrm


###############################################################################
%files


###############################################################################
%post
  # this is run inside the container to install all necessary packages

  apt-get install -y software-properties-common
  add-apt-repository -y ppa:bibi-help/bibitools
  apt-get -y update
  apt-get -y install rnashapes
  ln -s /usr/bin/RNAshapes /usr/bin/rnashapes


###############################################################################
%labels

MAINTAINER adomissy@ucsd.edu
VERSION 0.0.1
BUILD_DATE 20170718

###############################################################################
%environment

  #PATH=/opt/conda/bin:/usr/local/bin:/usr/bin:/bin
  PATH="/opt/conda/bin:$PATH"
  PATH="/usr/bin/rnashapes:$PATH"
  export PATH


###############################################################################
%runscript
  # this will get copied to /.singularity.d/runscript indide the container
  # which will run whenever the container is called as an executable

  PS1="$SINGULARITY_CONTAINER":"$PS1"
  /usr/bin/rnashapes $@
  PS1=$PREVIOUSPS1
  

###############################################################################
%test
  # this will be run once upon completion of container building
  #
  #/opt/test.sh
  #
```

## Collection

 - Name: [alaindomissy/rnashapes](https://github.com/alaindomissy/rnashapes)
 - License: None

