---
id: 7419
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "vcflib_1.0.0-rc2"
commit: "a2f174a40f445103f3fe20d0866ee2a47e397a22"
version: "e1ea7a39e213915ffc5ef71b39f8d896"
build_date: "2019-11-25T00:54:28.828Z"
size_mb: 733
size: 291831839
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/vcflib_1.0.0-rc2/2019-11-25-a2f174a4-e1ea7a39/e1ea7a39e213915ffc5ef71b39f8d896.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/vcflib_1.0.0-rc2/2019-11-25-a2f174a4-e1ea7a39/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/vcflib_1.0.0-rc2/2019-11-25-a2f174a4-e1ea7a39/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:vcflib_1.0.0-rc2

```bash
$ singularity pull shub://TomHarrop/singularity-containers:vcflib_1.0.0-rc2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.10

%help
    Container for vcflib 1.0.0-rc2

%labels
    VERSION "vcflib 1.0.0-rc2"

%post
    # packages
    apt update
    apt install -y \
        build-essential \
        git \
        libbz2-dev \
        liblzma-dev \
        wget \
        zlib1g-dev

    # download vcflib
    git clone \
        https://github.com/vcflib/vcflib.git
    cd vcflib || exit 1
    git checkout tags/v1.0.0-rc2
    git submodule update --init --recursive
    make openmp

%environment
    export PATH="${PATH}:/vcflib/bin"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

