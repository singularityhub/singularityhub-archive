---
id: 11694
name: "TomHarrop/variant-utils"
branch: "master"
tag: "freebayes_1.3.1"
commit: "f2cc069c8bcdaac7c3dd4f73cfc555a270e49ae2"
version: "63eb007cd05b2245fc14838c1b6b03613879a009406f3e664e22dfd71880c0ba"
build_date: "2019-11-25T02:45:47.083Z"
size_mb: 424.83984375
size: 445476864
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/freebayes_1.3.1/2019-11-25-f2cc069c-63eb007c/63eb007cd05b2245fc14838c1b6b03613879a009406f3e664e22dfd71880c0ba.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/variant-utils/freebayes_1.3.1/2019-11-25-f2cc069c-63eb007c/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/freebayes_1.3.1/2019-11-25-f2cc069c-63eb007c/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:freebayes_1.3.1

```bash
$ singularity pull shub://TomHarrop/variant-utils:freebayes_1.3.1
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: TomHarrop/variant-utils:vcflib_1.0.1

%help
    Container for freebayes 1.3.1 with modified freebayes-parallel 
    that can be run from outside the scripts directory

%labels
    VERSION "freebayes 1.3.1"

%post
    # faster apt downloads
    export DEBIAN_FRONTEND=noninteractive
    # MIRRORS ALREADY CONFIGURED IN BASE CONTAINER

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
    git checkout tags/v1.3.1
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

 - Name: [TomHarrop/variant-utils](https://github.com/TomHarrop/variant-utils)
 - License: None

