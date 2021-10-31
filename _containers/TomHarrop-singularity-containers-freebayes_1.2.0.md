---
id: 7285
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "freebayes_1.2.0"
commit: "d25a489081072b131c2937d6c92ba7d15509d16d"
version: "1af8f2a0f6ab59af998b5853124476f3"
build_date: "2019-12-16T22:21:26.412Z"
size_mb: 1071
size: 412246047
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/freebayes_1.2.0/2019-12-16-d25a4890-1af8f2a0/1af8f2a0f6ab59af998b5853124476f3.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/freebayes_1.2.0/2019-12-16-d25a4890-1af8f2a0/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/freebayes_1.2.0/2019-12-16-d25a4890-1af8f2a0/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:freebayes_1.2.0

```bash
$ singularity pull shub://TomHarrop/singularity-containers:freebayes_1.2.0
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: TomHarrop/singularity-containers:vcflib_1.0.0-rc2

%help
    Container for freebayes 1.2.0 with modified freebayes-parallel 
    that can be run from outside the scripts directory

%labels
    VERSION "freebayes 1.2.0"

%post
    # packages
    apt update
    apt install -y \
        libtabixpp-dev \
        parallel \
        python

    # download freebayes
    git clone \
        https://github.com/ekg/freebayes.git
    cd freebayes || exit 1
    git checkout tags/v1.2.0
    git submodule update --init --recursive
    make

    # fix the scripts
    sed \
        's/..\/vcflib\/scripts\/vcffirstheader/vcffirstheader/g' \
        scripts/freebayes-parallel \
        | sed \
        's/..\/vcflib\/bin\/vcfstreamsort/vcfstreamsort/g' \
        > scripts/freebayes-parallel.new
    rm scripts/freebayes-parallel
    mv scripts/freebayes-parallel.new scripts/freebayes-parallel
    chmod 755 scripts/freebayes-parallel

%environment
    export PATH="${PATH}:/freebayes/bin:/freebayes/scripts"

%runscript
    exec /freebayes/bin/freebayes "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

