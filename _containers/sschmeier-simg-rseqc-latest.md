---
id: 5648
name: "sschmeier/simg-rseqc"
branch: "master"
tag: "latest"
commit: "e751f93da3a00efc817f383fdf1b9185035fc77b"
version: "94bc05d296611bb63bca45acff03f9dca8a89422ee161e629c59c96e0b06c65d"
build_date: "2019-11-05T06:26:45.291Z"
size_mb: 431.75
size: 452722688
sif: "https://datasets.datalad.org/shub/sschmeier/simg-rseqc/latest/2019-11-05-e751f93d-94bc05d2/94bc05d296611bb63bca45acff03f9dca8a89422ee161e629c59c96e0b06c65d.sif"
url: https://datasets.datalad.org/shub/sschmeier/simg-rseqc/latest/2019-11-05-e751f93d-94bc05d2/
recipe: https://datasets.datalad.org/shub/sschmeier/simg-rseqc/latest/2019-11-05-e751f93d-94bc05d2/Singularity
collection: sschmeier/simg-rseqc
---

# sschmeier/simg-rseqc:latest

```bash
$ singularity pull shub://sschmeier/simg-rseqc:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda2:4.5.11

%labels
   AUTHOR schmeier@tuta.io

%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container
  export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
  unset CONDA_DEFAULT_ENV
  export ANACONDA_HOME=/opt/conda


%post
   export PATH=/opt/conda/bin:$PATH
   echo "We add conda channels."
   conda config --add channels defaults
   conda config --add channels conda-forge
   conda config --add channels bioconda
   echo "We install tools."
   conda install --yes rseqc=2.6.4
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/simg-rseqc](https://github.com/sschmeier/simg-rseqc)
 - License: None

