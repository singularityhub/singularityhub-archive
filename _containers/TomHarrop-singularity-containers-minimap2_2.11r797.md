---
id: 3784
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "minimap2_2.11r797"
commit: "48dac27ef65390e21b9c798fc200c02a3eca4968"
version: "6cb68f34c64c0d06289eb01965b9d679"
build_date: "2021-01-04T23:41:17.752Z"
size_mb: 327
size: 124977183
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/minimap2_2.11r797/2021-01-04-48dac27e-6cb68f34/6cb68f34c64c0d06289eb01965b9d679.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/minimap2_2.11r797/2021-01-04-48dac27e-6cb68f34/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/minimap2_2.11r797/2021-01-04-48dac27e-6cb68f34/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:minimap2_2.11r797

```bash
$ singularity pull shub://TomHarrop/singularity-containers:minimap2_2.11r797
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help

    minimap2 2.11 (r797)
    
%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "minimap2 2.11 (r797)"

%post

    # install dependencies
    apt-get update
    apt-get install -y \
        build-essential wget zlib1g-dev

    # install minimap2
    wget -O "minimap2.tar.gz" \
        --no-check-certificate \
        https://github.com/lh3/minimap2/archive/v2.11.tar.gz
    mkdir minimap2
    tar -zxf minimap2.tar.gz \
        -C minimap2 \
        --strip-components 1

    cd minimap2 || exit 1
    make
    mv minimap2 /usr/local/bin/

    cd .. || exit 1
    rm -rf minimap2 minimap2.tar.gz

%runscript

    exec /usr/local/bin/minimap2 "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

