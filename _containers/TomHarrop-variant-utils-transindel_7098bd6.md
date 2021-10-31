---
id: 11825
name: "TomHarrop/variant-utils"
branch: "master"
tag: "transindel_7098bd6"
commit: "b5e6f92659d4e4d90bb33613f6b1bcd6a942cbe4"
version: "a0aa985746dfe810fb9af6f9740f0e7811b680458b9a2e1ed4c5fb1cec170ff4"
build_date: "2019-12-16T21:58:12.908Z"
size_mb: 447.29296875
size: 469020672
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/transindel_7098bd6/2019-12-16-b5e6f926-a0aa9857/a0aa985746dfe810fb9af6f9740f0e7811b680458b9a2e1ed4c5fb1cec170ff4.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/variant-utils/transindel_7098bd6/2019-12-16-b5e6f926-a0aa9857/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/transindel_7098bd6/2019-12-16-b5e6f926-a0aa9857/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:transindel_7098bd6

```bash
$ singularity pull shub://TomHarrop/variant-utils:transindel_7098bd6
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:2.7.17-buster

%help
    transIndel 7098bd6
    https://github.com/cauyrd/transIndel

%labels
    MAINTAINER "Tom Harrop"
    VERSION "transIndel 7098bd6"

%post
    # install samtools
    apt-get update
    apt-get install -y samtools

    # install python2 dependencies
    /usr/local/bin/pip install \
        pysam==0.15.3 \
        numpy==1.16.5
    /usr/local/bin/pip install \
        HTSeq==0.11.2

    # install transindel
    git clone git://github.com/cauyrd/transIndel.git
    cd transIndel || exit 1
    git checkout -f 7098bd6

    # change to python 2.17.7
    sed -i 's/#!\/usr\/bin\/python/#!\/usr\/local\/bin\/python/' \
        *.py
    chmod 755 *.py

%environment
    export PATH="${PATH}:/transIndel"

%runscript
    exec /transIndel/transIndel_build_DNA.py "$@"
```

## Collection

 - Name: [TomHarrop/variant-utils](https://github.com/TomHarrop/variant-utils)
 - License: None

