---
id: 11693
name: "TomHarrop/variant-utils"
branch: "master"
tag: "vcflib_1.0.1"
commit: "be31d01e882526682d120e00e9990f94522badc7"
version: "2932f0c17b5fe868f7020751de072c13265af8736eae1db56642836fab8de5ad"
build_date: "2019-11-25T01:12:02.032Z"
size_mb: 294.13671875
size: 308424704
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/vcflib_1.0.1/2019-11-25-be31d01e-2932f0c1/2932f0c17b5fe868f7020751de072c13265af8736eae1db56642836fab8de5ad.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/variant-utils/vcflib_1.0.1/2019-11-25-be31d01e-2932f0c1/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/vcflib_1.0.1/2019-11-25-be31d01e-2932f0c1/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:vcflib_1.0.1

```bash
$ singularity pull shub://TomHarrop/variant-utils:vcflib_1.0.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help
    Container for vcflib 1.0.1

%labels
    VERSION "vcflib 1.0.1"

%post
    # faster apt downloads
    export DEBIAN_FRONTEND=noninteractive
    (
        . /etc/os-release
        cat << _EOF_ > mirror.txt
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME} main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-updates main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-backports main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-security main restricted universe multiverse

_EOF_
        mv /etc/apt/sources.list /etc/apt/sources.list.bak
        cat mirror.txt /etc/apt/sources.list.bak > /etc/apt/sources.list
    )

    # packages
    apt update
    apt install -y \
        build-essential \
        git \
        libbz2-dev \
        liblzma-dev \
        python3 \
        wget \
        zlib1g-dev

    # download vcflib
    git clone \
        https://github.com/vcflib/vcflib.git
    cd vcflib || exit 1
    git checkout tags/v1.0.1
    git submodule update --init --recursive
    make openmp

%environment
    export PATH="${PATH}:/vcflib/bin"
```

## Collection

 - Name: [TomHarrop/variant-utils](https://github.com/TomHarrop/variant-utils)
 - License: None

