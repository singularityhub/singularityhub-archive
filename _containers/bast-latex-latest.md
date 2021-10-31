---
id: 13536
name: "bast/latex"
branch: "master"
tag: "latest"
commit: "ee39525f71f753f8b329310cd8c518a76a8503ad"
version: "2d24ca283486ba0b20d66e8a154a856f68f9b77363b615babbd954611a52d772"
build_date: "2021-04-11T14:34:45.797Z"
size_mb: 1782.90234375
size: 1869508608
sif: "https://datasets.datalad.org/shub/bast/latex/latest/2021-04-11-ee39525f-2d24ca28/2d24ca283486ba0b20d66e8a154a856f68f9b77363b615babbd954611a52d772.sif"
url: https://datasets.datalad.org/shub/bast/latex/latest/2021-04-11-ee39525f-2d24ca28/
recipe: https://datasets.datalad.org/shub/bast/latex/latest/2021-04-11-ee39525f-2d24ca28/Singularity
collection: bast/latex
---

# bast/latex:latest

```bash
$ singularity pull shub://bast/latex:latest
```

## Singularity Recipe

```singularity
BootStrap: library
From: ubuntu:20.04

%post
    apt-get install -y software-properties-common
    add-apt-repository universe
    apt-get update -y
    apt-get install -y texlive texlive-fonts-extra

%environment
    export LC_ALL=C

%runscript
    pdflatex $@

%labels
    Author radovan.bast@uit.no
```

## Collection

 - Name: [bast/latex](https://github.com/bast/latex)
 - License: None

