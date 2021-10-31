---
id: 12277
name: "scicore-unibas-ch/singularity-container-freesurfer"
branch: "master"
tag: "1.1"
commit: "bee76ed8a6c77f5996975173797dc5662e69a70e"
version: "d545e1136c50db919738f7a7bdbd82b99fec6d8f137c26f89e1e6a94c2a75f7b"
build_date: "2020-02-14T08:02:40.733Z"
size_mb: 4398.25390625
size: 4611903488
sif: "https://datasets.datalad.org/shub/scicore-unibas-ch/singularity-container-freesurfer/1.1/2020-02-14-bee76ed8-d545e113/d545e1136c50db919738f7a7bdbd82b99fec6d8f137c26f89e1e6a94c2a75f7b.sif"
url: https://datasets.datalad.org/shub/scicore-unibas-ch/singularity-container-freesurfer/1.1/2020-02-14-bee76ed8-d545e113/
recipe: https://datasets.datalad.org/shub/scicore-unibas-ch/singularity-container-freesurfer/1.1/2020-02-14-bee76ed8-d545e113/Singularity
collection: scicore-unibas-ch/singularity-container-freesurfer
---

# scicore-unibas-ch/singularity-container-freesurfer:1.1

```bash
$ singularity pull shub://scicore-unibas-ch/singularity-container-freesurfer:1.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

%post

    # bring up to date
    yum -y update

    # install the dependencies
    yum -y install epel-release
    yum install -y \
    bc \
    git \
    wget \
    tcsh \
    libblas \
    liblapack \
    zlib1g \
    libxmu \
    libxi \
    libxt \
    libx11 \
    libglu1-mesa

    # Uncompress FreeSurfer tarball to /usr/local/
    wget -c https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.0/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz -O - | \
    tar -xz -C /usr/local/

%environment
    export FREESURFER_HOME=/usr/local/freesurfer
    source $FREESURFER_HOME/SetUpFreeSurfer.sh
```

## Collection

 - Name: [scicore-unibas-ch/singularity-container-freesurfer](https://github.com/scicore-unibas-ch/singularity-container-freesurfer)
 - License: None

