---
id: 37
name: "YeoLab/rnashapes"
branch: "master"
tag: "extension"
commit: "f8cf450b6e1ce9a9c51362e7a495b0fb30a66e70"
version: "19373b5a2b5d8a6b98819ef62d062299"
build_date: "2017-10-16T01:34:18.637Z"
size_mb: 476
size: 131485727
sif: "https://datasets.datalad.org/shub/YeoLab/rnashapes/extension/2017-10-16-f8cf450b-19373b5a/19373b5a2b5d8a6b98819ef62d062299.simg"
url: https://datasets.datalad.org/shub/YeoLab/rnashapes/extension/2017-10-16-f8cf450b-19373b5a/
recipe: https://datasets.datalad.org/shub/YeoLab/rnashapes/extension/2017-10-16-f8cf450b-19373b5a/Singularity
collection: YeoLab/rnashapes
---

# YeoLab/rnashapes:extension

```bash
$ singularity pull shub://YeoLab/rnashapes:extension
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

 - Name: [YeoLab/rnashapes](https://github.com/YeoLab/rnashapes)
 - License: None

