---
id: 8487
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "minknow_18.12.9"
commit: "1ef53676c0c27d07e654fe3eb718fa45cc3e45d7"
version: "59da5db0535e5718a8a3c277620b297b"
build_date: "2019-10-30T00:48:16.093Z"
size_mb: 1395
size: 443228191
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/minknow_18.12.9/2019-10-30-1ef53676-59da5db0/59da5db0535e5718a8a3c277620b297b.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/minknow_18.12.9/2019-10-30-1ef53676-59da5db0/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/minknow_18.12.9/2019-10-30-1ef53676-59da5db0/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:minknow_18.12.9

```bash
$ singularity pull shub://TomHarrop/singularity-containers:minknow_18.12.9
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
    ONT MinKNOW 18.12.9-1 GUI in a container

    Run as follows:

    singularity instance start \
        -B output/dir/run:/run,output/dir/var:/var \
        minknow_18.12.9.sif \
        minknow

%labels
    MAINTAINER "Tom Harrop"
    VERSION "MinKNOW 18.12.9-1"

%post
    # install dependencies
    apt update
    apt install -y \
        apt-transport-https \
        libasound2 \
        libgconf-2-4 \
        libgtk-3-dev \
        libnss3 \
        libxss1 \
        wget

    # install minknow
    wget \
        -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub \
        | apt-key add -
    echo "deb http://mirror.oxfordnanoportal.com/apt xenial-stable non-free" \
        | tee /etc/apt/sources.list.d/nanoporetech.sources.list
    apt update
    apt install -y minknow-nc=18.12.9-1~xenial

%startscript
    /opt/ONT/MinKNOW/bin/mk_manager_svc &
    nohup /opt/ui/MinKNOW > /dev/null 2>&1 < /dev/null &
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

