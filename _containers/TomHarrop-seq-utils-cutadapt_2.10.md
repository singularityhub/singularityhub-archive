---
id: 13469
name: "TomHarrop/seq-utils"
branch: "master"
tag: "cutadapt_2.10"
commit: "c857d40164436e397d902509be816992968fd219"
version: "d28cff1de1a103742ed4cdde64836688d161eba3f08b570a9f28c09566b02406"
build_date: "2020-06-25T22:22:36.962Z"
size_mb: 305.30078125
size: 320131072
sif: "https://datasets.datalad.org/shub/TomHarrop/seq-utils/cutadapt_2.10/2020-06-25-c857d401-d28cff1d/d28cff1de1a103742ed4cdde64836688d161eba3f08b570a9f28c09566b02406.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/seq-utils/cutadapt_2.10/2020-06-25-c857d401-d28cff1d/
recipe: https://datasets.datalad.org/shub/TomHarrop/seq-utils/cutadapt_2.10/2020-06-25-c857d401-d28cff1d/Singularity
collection: TomHarrop/seq-utils
---

# TomHarrop/seq-utils:cutadapt_2.10

```bash
$ singularity pull shub://TomHarrop/seq-utils:cutadapt_2.10
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.8.3-buster

%help

    Python 3.8.3 with Cutadapt 2.10
    
%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "Cutadapt 2.10"

%runscript

    exec /usr/local/bin/cutadapt "$@"

%post
    /usr/local/bin/pip3 install \
        cutadapt==2.10
```

## Collection

 - Name: [TomHarrop/seq-utils](https://github.com/TomHarrop/seq-utils)
 - License: None

