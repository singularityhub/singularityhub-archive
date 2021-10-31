---
id: 9930
name: "granek/singularity-rstudio-base"
branch: "master"
tag: "3.6.0"
commit: "1bd10085df3eb00e8ad71bac37526637f15c8eb5"
version: "3c75c8500acbc2dcbde46cf6f3d1e4ec"
build_date: "2021-01-23T10:08:41.234Z"
size_mb: 1971
size: 528134175
sif: "https://datasets.datalad.org/shub/granek/singularity-rstudio-base/3.6.0/2021-01-23-1bd10085-3c75c850/3c75c8500acbc2dcbde46cf6f3d1e4ec.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/granek/singularity-rstudio-base/3.6.0/2021-01-23-1bd10085-3c75c850/
recipe: https://datasets.datalad.org/shub/granek/singularity-rstudio-base/3.6.0/2021-01-23-1bd10085-3c75c850/Singularity
collection: granek/singularity-rstudio-base
---

# granek/singularity-rstudio-base:3.6.0

```bash
$ singularity pull shub://granek/singularity-rstudio-base:3.6.0
```

## Singularity Recipe

```singularity
BootStrap: shub
From: granek/singularity-rstudio:3.6.0

%labels
    Maintainer Josh Granek
    Image_Name singularity-rstudio-base
    Image_Version 0001

%runscript
  exec port_and_password "${@}"

%apprun rstudio
  exec rserver "${@}"

%apprun default
  exec "${@}"

%apprun pp
  exec port_and_password "${@}"

%environment
  export PATH=/usr/lib/rstudio-server/bin:${PATH}
  export SHELL=/bin/bash
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8
  export LANGUAGE=en_US.UTF-8
  
%setup
  install -Dv \
    port_and_password.sh \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/port_and_password

%post
  # Install extra stuff
  apt-get update
  apt-get install -y --no-install-recommends \
    bsdmainutils \
    iproute2 \
    libxml2-dev \
    curl \
    wget \
    bzip2 \
    ca-certificates \
    sudo \
    locales \
    emacs \
    less \
    make \
    git \
    ssh \
    htop \
    jq \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#--------------------------------------------------------------------------------

mkdir -p /data
mkdir -p /workspace
```

## Collection

 - Name: [granek/singularity-rstudio-base](https://github.com/granek/singularity-rstudio-base)
 - License: [MIT License](https://api.github.com/licenses/mit)

