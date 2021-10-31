---
id: 13957
name: "motroy/singularity-scagaire"
branch: "master"
tag: "latest"
commit: "c790e82f308d8b98c8f2bb5999d123203d1799ba"
version: "4c6b78eacc78b0ee05a9653ef8d5e03e"
build_date: "2020-08-17T10:39:56.997Z"
size_mb: 1873.0
size: 825761823
sif: "https://datasets.datalad.org/shub/motroy/singularity-scagaire/latest/2020-08-17-c790e82f-4c6b78ea/4c6b78eacc78b0ee05a9653ef8d5e03e.sif"
url: https://datasets.datalad.org/shub/motroy/singularity-scagaire/latest/2020-08-17-c790e82f-4c6b78ea/
recipe: https://datasets.datalad.org/shub/motroy/singularity-scagaire/latest/2020-08-17-c790e82f-4c6b78ea/Singularity
collection: motroy/singularity-scagaire
---

# motroy/singularity-scagaire:latest

```bash
$ singularity pull shub://motroy/singularity-scagaire:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: frolvlad/alpine-miniconda3:latest

%environment
export LC_ALL=C
export CONDARC=/.condarc
export PATH="/opt/conda/bin:/Software/scagaire/:/Software/scagaire/scagaire/:/Software/scagaire/scagaire/data/:$PATH"
export MPLBACKEND=TKAgg

%post
apk update && apk add git curl-dev wget less openssh-server parallel coreutils bash libx11 #py3-pip libcurl gcc musl-dev
/opt/conda/bin/conda config --file /.condarc --add channels defaults && /opt/conda/bin/conda config --file /.condarc --add channels conda-forge && /opt/conda/bin/conda config --file /.condarc --add channels bioconda
/opt/conda/bin/conda update -n base -c defaults conda
/opt/conda/bin/conda install -c conda-forge mamba
export PATH="/opt/conda/bin:$PATH"
mamba install -y -c bioconda mash abricate ncbi-genome-download
export MPLBACKEND=TKAgg
mkdir /Software && cd /Software
git clone https://github.com/quadram-institute-bioscience/scagaire.git
cd scagaire
python setup.py install
export PATH="/Software/scagaire/:/Software/scagaire/scagaire/:/Software/scagaire/scagaire/data/:$PATH"
```

## Collection

 - Name: [motroy/singularity-scagaire](https://github.com/motroy/singularity-scagaire)
 - License: [MIT License](https://api.github.com/licenses/mit)

