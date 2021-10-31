---
id: 13532
name: "bast/pandoc"
branch: "master"
tag: "latest"
commit: "ad6c4f45084bac8d22ec6fd44484ac691436638d"
version: "cab1059b3fd5e6eaf91d800dc4557404fd3532b72fc71e874bfd5f409c73e34b"
build_date: "2021-04-07T13:06:34.667Z"
size_mb: 223.73828125
size: 234606592
sif: "https://datasets.datalad.org/shub/bast/pandoc/latest/2021-04-07-ad6c4f45-cab1059b/cab1059b3fd5e6eaf91d800dc4557404fd3532b72fc71e874bfd5f409c73e34b.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/bast/pandoc/latest/2021-04-07-ad6c4f45-cab1059b/
recipe: https://datasets.datalad.org/shub/bast/pandoc/latest/2021-04-07-ad6c4f45-cab1059b/Singularity
collection: bast/pandoc
---

# bast/pandoc:latest

```bash
$ singularity pull shub://bast/pandoc:latest
```

## Singularity Recipe

```singularity
BootStrap: library
From: ubuntu:20.04

%post
    apt-get install -y software-properties-common
    add-apt-repository universe
    apt-get update -y
    apt-get install -y pandoc

%environment
    export LC_ALL=C

%runscript
    pandoc $@

%labels
    Author radovan.bast@uit.no
```

## Collection

 - Name: [bast/pandoc](https://github.com/bast/pandoc)
 - License: None

