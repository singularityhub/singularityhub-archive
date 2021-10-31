---
id: 11472
name: "TomHarrop/ont-containers"
branch: "master"
tag: "minionqc_1.4.1"
commit: "dc7cdb0d33429691055e41f8bb6f6cf5697ccea9"
version: "a08ebcd3c81c8686894386254af7bc0289ae342ec7f23fadcb98e30feba38b71"
build_date: "2020-11-30T20:26:47.886Z"
size_mb: 901.93359375
size: 945745920
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/minionqc_1.4.1/2020-11-30-dc7cdb0d-a08ebcd3/a08ebcd3c81c8686894386254af7bc0289ae342ec7f23fadcb98e30feba38b71.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/ont-containers/minionqc_1.4.1/2020-11-30-dc7cdb0d-a08ebcd3/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/minionqc_1.4.1/2020-11-30-dc7cdb0d-a08ebcd3/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:minionqc_1.4.1

```bash
$ singularity pull shub://TomHarrop/ont-containers:minionqc_1.4.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/verse:3.5.3

%help
    Container for MinIONQC.R
    https://github.com/roblanf/minion_qc

%labels
    MAINTAINER "Tom Harrop"
    VERSION "MinIONQC.R 1.4.1"

%post
    # install package deps
    Rscript -e "options(Ncpus=8); \
        install.packages(c(\
            'futile.logger', \
            'optparse', \
            'viridis'), \
            type='source', ask=FALSE)"

    # install minionqc.R
    wget -O /usr/local/bin/MinIONQC.R \
        --no-check-certificate \
        https://github.com/roblanf/minion_qc/releases/download/v1.4.1/MinIONQC.R
    chmod 755 /usr/local/bin/MinIONQC.R

%runscript
    exec /usr/local/bin/Rscript /usr/local/bin/MinIONQC.R "$@"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

