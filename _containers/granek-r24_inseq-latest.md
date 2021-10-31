---
id: 6191
name: "granek/r24_inseq"
branch: "master"
tag: "latest"
commit: "5e81c8cd24cd02d8005752bdbefeab592b204be1"
version: "a8af2f7e341aaa78f1e3a957ab804b53"
build_date: "2019-06-25T19:01:24.770Z"
size_mb: 2041
size: 547917855
sif: "https://datasets.datalad.org/shub/granek/r24_inseq/latest/2019-06-25-5e81c8cd-a8af2f7e/a8af2f7e341aaa78f1e3a957ab804b53.simg"
url: https://datasets.datalad.org/shub/granek/r24_inseq/latest/2019-06-25-5e81c8cd-a8af2f7e/
recipe: https://datasets.datalad.org/shub/granek/r24_inseq/latest/2019-06-25-5e81c8cd-a8af2f7e/Singularity
collection: granek/r24_inseq
---

# granek/r24_inseq:latest

```bash
$ singularity pull shub://granek/r24_inseq:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: granek/singularity-rstudio-base:3.6.0

%labels
    Maintainer Josh Granek
    Image_Version 009

##------------------------------------------------------------
## Build example:
## sudo singularity build inseq_rstudio.simg Singularity.rstudio
## sudo singularity build ~/container_images/inseq_rstudio_v007.simg Singularity.rstudio
##
## Run example:
## singularity run inseq_rstudio.simg ls
## singularity run --app rstudio inseq_rstudio.simg
##------------------------------------------------------------

%runscript
  exec "${@}"

%apprun rstudio
  exec rserver "${@}"

%environment
  export PATH=/usr/lib/rstudio-server/bin:${PATH}
  export SHELL=/bin/bash
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8
  export LANGUAGE=en_US.UTF-8

%post
  # Install extra stuff
  apt-get update
  apt-get install -y --no-install-recommends \
    bowtie \
    python3-biopython
   apt-get clean
   rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [granek/r24_inseq](https://github.com/granek/r24_inseq)
 - License: None

