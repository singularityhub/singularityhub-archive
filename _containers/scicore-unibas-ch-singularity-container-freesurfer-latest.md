---
id: 12133
name: "scicore-unibas-ch/singularity-container-freesurfer"
branch: "master"
tag: "latest"
commit: "bee76ed8a6c77f5996975173797dc5662e69a70e"
version: "ede9b68517f4090f2a69fb414b55ea57c076b65d5002434a54362f46687509e9"
build_date: "2020-02-13T21:55:44.106Z"
size_mb: 4398.25390625
size: 4611903488
sif: "https://datasets.datalad.org/shub/scicore-unibas-ch/singularity-container-freesurfer/latest/2020-02-13-bee76ed8-ede9b685/ede9b68517f4090f2a69fb414b55ea57c076b65d5002434a54362f46687509e9.sif"
url: https://datasets.datalad.org/shub/scicore-unibas-ch/singularity-container-freesurfer/latest/2020-02-13-bee76ed8-ede9b685/
recipe: https://datasets.datalad.org/shub/scicore-unibas-ch/singularity-container-freesurfer/latest/2020-02-13-bee76ed8-ede9b685/Singularity
collection: scicore-unibas-ch/singularity-container-freesurfer
---

# scicore-unibas-ch/singularity-container-freesurfer:latest

```bash
$ singularity pull shub://scicore-unibas-ch/singularity-container-freesurfer:latest
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

