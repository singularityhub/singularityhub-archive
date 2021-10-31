---
id: 4064
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "hmmer_3.2.1"
commit: "849809b1260634e5bed2b66efe5f3871b97b0378"
version: "5e9dc82d80500447dd945feb631cd9f3"
build_date: "2020-12-17T21:23:53.045Z"
size_mb: 340
size: 131424287
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/hmmer_3.2.1/2020-12-17-849809b1-5e9dc82d/5e9dc82d80500447dd945feb631cd9f3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/hmmer_3.2.1/2020-12-17-849809b1-5e9dc82d/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/hmmer_3.2.1/2020-12-17-849809b1-5e9dc82d/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:hmmer_3.2.1

```bash
$ singularity pull shub://TomHarrop/singularity-containers:hmmer_3.2.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help

    HMMER 3.2.1
    http://www.hmmer.org/

%labels

    MAINTAINER "Tom Harrop"
    VERSION "HMMER 3.2.1"

%post

    # dependencies
    apt-get update
    apt-get install -y \
        build-essential \
        wget 

    # install
    wget -O "hmmer.tar.gz" \
        --no-check-certificate \
        "http://eddylab.org/software/hmmer/hmmer-3.2.1.tar.gz"
    mkdir hmmer
    tar -zxf hmmer.tar.gz \
        -C hmmer \
        --strip-components 1
    cd hmmer || exit 1
    ./configure
    make
    make install
    cd .. || exit 1
    rm -rf hmmer hmmer.tar.gz

%runscript

    exec /usr/local/bin/hmmsearch "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

