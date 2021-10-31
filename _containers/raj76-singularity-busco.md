---
id: 1926
name: "raj76/singularity"
branch: "master"
tag: "busco"
commit: "73c71316350ac3b008fe32d951a45dad83e56d8a"
version: "c908fce0f29735b7b1461892583381e3"
build_date: "2018-03-04T02:27:33.647Z"
size_mb: 2100
size: 847249439
sif: "https://datasets.datalad.org/shub/raj76/singularity/busco/2018-03-04-73c71316-c908fce0/c908fce0f29735b7b1461892583381e3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/raj76/singularity/busco/2018-03-04-73c71316-c908fce0/
recipe: https://datasets.datalad.org/shub/raj76/singularity/busco/2018-03-04-73c71316-c908fce0/Singularity
collection: raj76/singularity
---

# raj76/singularity:busco

```bash
$ singularity pull shub://raj76/singularity:busco
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
conda install busco

%environment
export LC_ALL=C
export DEBIAN_FRONTEND noninteractive
export PATH=$PATH:/opt/conda/bin
```

## Collection

 - Name: [raj76/singularity](https://github.com/raj76/singularity)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

