---
id: 3946
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "sra_2.9.2"
commit: "b6d12582e87c27ef90a1f715b3bee2056b32fa60"
version: "b71cbf3616415afeaa92776656633485"
build_date: "2019-10-01T22:41:31.754Z"
size_mb: 317
size: 144699423
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/sra_2.9.2/2019-10-01-b6d12582-b71cbf36/b71cbf3616415afeaa92776656633485.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/sra_2.9.2/2019-10-01-b6d12582-b71cbf36/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/sra_2.9.2/2019-10-01-b6d12582-b71cbf36/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:sra_2.9.2

```bash
$ singularity pull shub://TomHarrop/singularity-containers:sra_2.9.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help

    NCBI SRA 2.9.2
    https://github.com/ncbi/sra-tools

%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "SRA 2.9.2"

%post

    # install dependencies
    apt-get update
    apt-get install -y \
        wget

    # download SRA
    wget -O "sra.tar.gz" \
        --no-check-certificate \
        https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.9.2/sratoolkit.2.9.2-ubuntu64.tar.gz
    mkdir sra
    tar -zxf sra.tar.gz \
        -C sra \
        --strip-components 1
    rm sra.tar.gz

%environment

    export PATH="${PATH}:/sra/bin"

%runscript

    exec /sra/bin/fasterq-dump "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

