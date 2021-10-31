---
id: 15009
name: "TomHarrop/ont-containers"
branch: "master"
tag: "minionqc_1.4.2"
commit: "1d9880398bedf64b175eae81ef240156e440de34"
version: "889fe2b45280bc125dc6133ecb1d82506f9e96700d03f1d18aff724e0ca13a67"
build_date: "2020-11-30T22:26:49.944Z"
size_mb: 1206.12109375
size: 1264709632
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/minionqc_1.4.2/2020-11-30-1d988039-889fe2b4/889fe2b45280bc125dc6133ecb1d82506f9e96700d03f1d18aff724e0ca13a67.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/ont-containers/minionqc_1.4.2/2020-11-30-1d988039-889fe2b4/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/minionqc_1.4.2/2020-11-30-1d988039-889fe2b4/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:minionqc_1.4.2

```bash
$ singularity pull shub://TomHarrop/ont-containers:minionqc_1.4.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/verse:4.0.3

%help
    Container for MinIONQC.R
    https://github.com/roblanf/minion_qc

%labels
    MAINTAINER "Tom Harrop"
    VERSION "MinIONQC.R 1.4.2"

%post
    # install package deps
    Rscript -e "options(Ncpus=8); \
        install.packages(c(\
            'futile.logger', \
            'optparse', \
            'plyr', \
            'reshape2', \
            'viridis'), \
            type='source', ask=FALSE)"

    # install minionqc.R
    wget -O /usr/local/bin/MinIONQC.R \
        --no-check-certificate \
        https://github.com/roblanf/minion_qc/releases/download/1.4.2/MinIONQC.R
    chmod 755 /usr/local/bin/MinIONQC.R

%runscript
    exec /usr/local/bin/Rscript /usr/local/bin/MinIONQC.R "$@"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

