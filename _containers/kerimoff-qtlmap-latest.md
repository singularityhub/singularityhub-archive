---
id: 8676
name: "kerimoff/qtlmap"
branch: "master"
tag: "latest"
commit: "8e6b19fb2a643a416d31f00cf83fd4f6d1c000e6"
version: "7ab535b87cdb973dc3a61fba0c56a968"
build_date: "2019-04-28T09:30:56.233Z"
size_mb: 1825
size: 685445151
sif: "https://datasets.datalad.org/shub/kerimoff/qtlmap/latest/2019-04-28-8e6b19fb-7ab535b8/7ab535b87cdb973dc3a61fba0c56a968.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kerimoff/qtlmap/latest/2019-04-28-8e6b19fb-7ab535b8/
recipe: https://datasets.datalad.org/shub/kerimoff/qtlmap/latest/2019-04-28-8e6b19fb-7ab535b8/Singularity
collection: kerimoff/qtlmap
---

# kerimoff/qtlmap:latest

```bash
$ singularity pull shub://kerimoff/qtlmap:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Nurlan Kerimov
    DESCRIPTION Singularity image containing all requirements for the nf-core/qtlmap pipeline
    VERSION 1.0dev

%environment
    PATH=/opt/conda/envs/nf-core-qtlmap-1.0dev/bin:$PATH
    export PATH

%files
    environment.yml /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [kerimoff/qtlmap](https://github.com/kerimoff/qtlmap)
 - License: [MIT License](https://api.github.com/licenses/mit)

