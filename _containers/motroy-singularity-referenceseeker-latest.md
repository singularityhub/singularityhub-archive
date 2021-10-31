---
id: 12409
name: "motroy/singularity-referenceseeker"
branch: "master"
tag: "latest"
commit: "387b47a033441504050d41ea75c640891f097643"
version: "b7fccfa1562b27b873ef14494728c553"
build_date: "2021-01-13T20:26:36.613Z"
size_mb: 541.0
size: 184840223
sif: "https://datasets.datalad.org/shub/motroy/singularity-referenceseeker/latest/2021-01-13-387b47a0-b7fccfa1/b7fccfa1562b27b873ef14494728c553.sif"
url: https://datasets.datalad.org/shub/motroy/singularity-referenceseeker/latest/2021-01-13-387b47a0-b7fccfa1/
recipe: https://datasets.datalad.org/shub/motroy/singularity-referenceseeker/latest/2021-01-13-387b47a0-b7fccfa1/Singularity
collection: motroy/singularity-referenceseeker
---

# motroy/singularity-referenceseeker:latest

```bash
$ singularity pull shub://motroy/singularity-referenceseeker:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: frolvlad/alpine-miniconda3:latest

%environment
export LC_ALL=C
export CONDARC=/.condarc

%post
apk update && apk add git curl wget less openssh-server parallel coreutils bash
/opt/conda/bin/conda config --file /.condarc --add channels defaults && /opt/conda/bin/conda config --file /.condarc --add channels conda-forge && /opt/conda/bin/conda config --file /.condarc --add channels bioconda
/opt/conda/bin/conda install -c conda-forge -c bioconda -c defaults referenceseeker
```

## Collection

 - Name: [motroy/singularity-referenceseeker](https://github.com/motroy/singularity-referenceseeker)
 - License: [MIT License](https://api.github.com/licenses/mit)

