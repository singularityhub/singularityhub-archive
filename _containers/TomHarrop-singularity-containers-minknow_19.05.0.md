---
id: 9066
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "minknow_19.05.0"
commit: "0c81748bc9e61545b98a56fc8354654d50041fc5"
version: "0a2eb5d84336bf693044c386711bafe1"
build_date: "2019-10-30T00:48:03.399Z"
size_mb: 1895
size: 555700255
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/minknow_19.05.0/2019-10-30-0c81748b-0a2eb5d8/0a2eb5d84336bf693044c386711bafe1.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/minknow_19.05.0/2019-10-30-0c81748b-0a2eb5d8/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/minknow_19.05.0/2019-10-30-0c81748b-0a2eb5d8/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:minknow_19.05.0

```bash
$ singularity pull shub://TomHarrop/singularity-containers:minknow_19.05.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
    ONT MinKNOW 19.05.0-1 GUI in a container

    Run as follows:

    singularity instance start \
        -B output/dir/run:/run,output/dir/var:/var \
        minknow_19.05.0.sif \
        minknow

%labels
    MAINTAINER "Tom Harrop"
    VERSION "MinKNOW 19.05.0-1"

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
    apt install -y minknow-nc=19.05.0-1~xenial

%startscript
    /opt/ONT/MinKNOW/bin/mk_manager_svc &
    nohup /opt/ui/MinKNOW > /dev/null 2>&1 < /dev/null &
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

