---
id: 12852
name: "TomHarrop/variant-utils"
branch: "master"
tag: "bayescan_2.1"
commit: "caa77024c263617b8b01331d6abdf5ae3b71f41e"
version: "6f6c2c2054aaa789a526bedabf9ee6b46d160270127bafb5ba44521ee679a4b0"
build_date: "2020-04-30T23:15:51.018Z"
size_mb: 103.4921875
size: 108519424
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/bayescan_2.1/2020-04-30-caa77024-6f6c2c20/6f6c2c2054aaa789a526bedabf9ee6b46d160270127bafb5ba44521ee679a4b0.sif"
url: https://datasets.datalad.org/shub/TomHarrop/variant-utils/bayescan_2.1/2020-04-30-caa77024-6f6c2c20/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/bayescan_2.1/2020-04-30-caa77024-6f6c2c20/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:bayescan_2.1

```bash
$ singularity pull shub://TomHarrop/variant-utils:bayescan_2.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:12.04

%help
    Container for BayeScan 2.1

%labels
    VERSION "bayescan 2.1"

%runscript
    exec /usr/local/bin/bayescan_2.1 "$@"

%post
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C

    apt-get update
    apt-get install -y \
        build-essential \
        wget \
        unzip

    # bayescan
    wget http://cmpg.unibe.ch/software/BayeScan/files/BayeScan2.1.zip
    unzip BayeScan2.1.zip
    cd BayeScan2.1/source || exit 1
    make
    cp bayescan_2.1 /usr/local/bin/
    cd ../.. || exit 1
    rm -rf BayeScan2.1
```

## Collection

 - Name: [TomHarrop/variant-utils](https://github.com/TomHarrop/variant-utils)
 - License: None

