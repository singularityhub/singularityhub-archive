---
id: 11200
name: "poojabhat1690/rRequirements"
branch: "master"
tag: "latest"
commit: "99fa51de2984f162506d6e5405ea938e57244467"
version: "65dbce3b41e637d2f67fa6b730a76bd1"
build_date: "2019-10-09T07:41:25.311Z"
size_mb: 1284.0
size: 454885407
sif: "https://datasets.datalad.org/shub/poojabhat1690/rRequirements/latest/2019-10-09-99fa51de-65dbce3b/65dbce3b41e637d2f67fa6b730a76bd1.sif"
url: https://datasets.datalad.org/shub/poojabhat1690/rRequirements/latest/2019-10-09-99fa51de-65dbce3b/
recipe: https://datasets.datalad.org/shub/poojabhat1690/rRequirements/latest/2019-10-09-99fa51de-65dbce3b/Singularity
collection: poojabhat1690/rRequirements
---

# poojabhat1690/rRequirements:latest

```bash
$ singularity pull shub://poojabhat1690/rRequirements:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From:ubuntu:16.04


%post

        apt-get -y update
        apt-get install -y tzdata && \
        apt-get install -y software-properties-common && \
        add-apt-repository -y -u ppa:certbot/certbot && \
        apt-get install -y libopenblas-dev  libcurl4-openssl-dev libopenmpi-dev openmpi-bin openmpi-common openmpi-doc openssh-client openssh-server libssh-dev wget vim git nano git cmake  gfortran g++ curl wget python autoconf bzip2 libtool libtool-bin r-base-core libxml2-dev



R --slave -e 'source("https://bioconductor.org/biocLite.R")'
R --slave -e 'BiocInstaller::biocLite(c("GenomicRanges"))'
R --slave -e 'BiocInstaller::biocLite(c("biomaRt"))'
R --slave -e 'BiocInstaller::biocLite(c("Biostrings"))'
R --slave -e 'install.packages(c("checkmate", "ggplot2","reshape","dplyr","plyr","tibble"), repos="https://cloud.r-project.org/")'


%environment
export LC_ALL=C
export PATH=$PATH
```

## Collection

 - Name: [poojabhat1690/rRequirements](https://github.com/poojabhat1690/rRequirements)
 - License: None

