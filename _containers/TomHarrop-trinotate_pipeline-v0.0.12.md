---
id: 12171
name: "TomHarrop/trinotate_pipeline"
branch: "master"
tag: "v0.0.12"
commit: "db1df17413567d71fec3ad848363a03c230c90dd"
version: "1b8ba3684fca861f0d384b5706b30952a6a4677f6da0dbe24fba402132d73b42"
build_date: "2020-12-02T02:08:22.702Z"
size_mb: 2558.0625
size: 2682322944
sif: "https://datasets.datalad.org/shub/TomHarrop/trinotate_pipeline/v0.0.12/2020-12-02-db1df174-1b8ba368/1b8ba3684fca861f0d384b5706b30952a6a4677f6da0dbe24fba402132d73b42.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/trinotate_pipeline/v0.0.12/2020-12-02-db1df174-1b8ba368/
recipe: https://datasets.datalad.org/shub/TomHarrop/trinotate_pipeline/v0.0.12/2020-12-02-db1df174-1b8ba368/Singularity
collection: TomHarrop/trinotate_pipeline
---

# TomHarrop/trinotate_pipeline:v0.0.12

```bash
$ singularity pull shub://TomHarrop/trinotate_pipeline:v0.0.12
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: trinityrnaseq/trinityrnaseq:2.9.1

%help
    Container for trinotate_pipeline 

%labels

%environment
    export PATH="${PATH}:/trinotate:/trinotate/util:/usr/local/bin/trinityrnaseq:/usr/local/bin/trinityrnaseq/util:/usr/local/bin/trinityrnaseq/util/support_scripts:/usr/local/bin/trinityrnaseq/util/misc"
    export LC_ALL=C

%post
    export LC_ALL=C
    export DEBIAN_FRONTEND=noninteractive
    # faster apt downloads
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

    # missing forever b/c license
    # RnammerTranscriptome.pl
    # rnammer
    # signalp
    # Trinotate

    # apt-able dependencies
    apt-get update
    apt-get install -y \
        hmmer \
        libdbd-sqlite3-perl \
        libdbi-perl \
        python3-dev \
        python3-pip \
        python3-venv \
        sqlite3 \
        transdecoder

    # install trinotate
    wget \
        -O trinotate.tar.gz \
        https://github.com/Trinotate/Trinotate/archive/Trinotate-v3.2.0.tar.gz
    mkdir trinotate
    tar -zxf trinotate.tar.gz \
        -C trinotate \
        --strip-components 1
    rm -f trinotate.tar.gz

    # install pipeline
    /usr/bin/pip3 \
        install \
        git+git://github.com/TomHarrop/trinotate_pipeline.git@v0.0.12

%runscript
    exec /usr/local/bin/trinotate_pipeline "$@"
```

## Collection

 - Name: [TomHarrop/trinotate_pipeline](https://github.com/TomHarrop/trinotate_pipeline)
 - License: None

