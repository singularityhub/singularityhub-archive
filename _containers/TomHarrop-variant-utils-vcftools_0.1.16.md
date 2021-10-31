---
id: 11722
name: "TomHarrop/variant-utils"
branch: "master"
tag: "vcftools_0.1.16"
commit: "d64cc5a37951760be575c43024c66e69b2563166"
version: "c270d19a922fbb2174b7bfa9dcb772486be675fcf2e703e49c9ea261c1e54aa5"
build_date: "2021-03-04T00:21:39.054Z"
size_mb: 78.953125
size: 82788352
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/vcftools_0.1.16/2021-03-04-d64cc5a3-c270d19a/c270d19a922fbb2174b7bfa9dcb772486be675fcf2e703e49c9ea261c1e54aa5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/variant-utils/vcftools_0.1.16/2021-03-04-d64cc5a3-c270d19a/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/vcftools_0.1.16/2021-03-04-d64cc5a3-c270d19a/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:vcftools_0.1.16

```bash
$ singularity pull shub://TomHarrop/variant-utils:vcftools_0.1.16
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.9

%help
    Container for vcftools 0.1.16

%labels
    VERSION "vcftools 0.1.16"

%post
    # packages
    apk add --update \
        bash \
        build-base \
        gcc \
        git \
        perl \
        wget \
        zlib-dev

    # download vcftools
    mkdir vcftools
    wget \
        -O "vcftools.tar.gz" \
        --no-check-certificate \
        https://github.com/vcftools/vcftools/releases/download/v0.1.16/vcftools-0.1.16.tar.gz
    tar -zxf vcftools.tar.gz \
        -C vcftools \
        --strip-components 2

    cd vcftools || exit 1
    ./configure
    make 
    make install
    cd .. || exit 1
    rm -rf vcftools vcftools.tar.gz

%runscript
    exec /usr/local/bin/vcftools "$@"
```

## Collection

 - Name: [TomHarrop/variant-utils](https://github.com/TomHarrop/variant-utils)
 - License: None

