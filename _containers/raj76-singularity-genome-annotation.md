---
id: 1759
name: "raj76/singularity"
branch: "master"
tag: "genome-annotation"
commit: "73c71316350ac3b008fe32d951a45dad83e56d8a"
version: "6d1c9fe6d9cd923641d6c30139d75340"
build_date: "2018-03-04T02:27:33.656Z"
size_mb: 4894
size: 1751863327
sif: "https://datasets.datalad.org/shub/raj76/singularity/genome-annotation/2018-03-04-73c71316-6d1c9fe6/6d1c9fe6d9cd923641d6c30139d75340.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/raj76/singularity/genome-annotation/2018-03-04-73c71316-6d1c9fe6/
recipe: https://datasets.datalad.org/shub/raj76/singularity/genome-annotation/2018-03-04-73c71316-6d1c9fe6/Singularity
collection: raj76/singularity
---

# raj76/singularity:genome-annotation

```bash
$ singularity pull shub://raj76/singularity:genome-annotation
```

## Singularity Recipe

```singularity
BootStrap: shub
From: raj76/singularity:biocontainers

%labels
Maintainer Raj Ayyampalayam
Version v1.0

%post
export LC_ALL=C
export DEBIAN_FRONTEND noninteractive
export PATH=$PATH:/opt/conda/bin
conda config --add channels defaults
conda config --add channels conda-forge
conda install perl-hash-merge
conda install perl-yaml
conda install perl-parallel-forkmanager
conda install perl-file-spec
conda install perl-file-which 
conda install perl-scalar-util-numeric
conda install -c thiesgehrmann perl-logger-simple
conda install maker=2.31.9

%environment
export LC_ALL=C
export DEBIAN_FRONTEND noninteractive
export PATH=$PATH:/opt/conda/bin
```

## Collection

 - Name: [raj76/singularity](https://github.com/raj76/singularity)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

