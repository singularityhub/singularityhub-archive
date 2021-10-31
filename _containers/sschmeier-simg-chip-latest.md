---
id: 3204
name: "sschmeier/simg-chip"
branch: "master"
tag: "latest"
commit: "2a1d537054b5d5481b81a2a811949c88e96fa2d1"
version: "ceadcb882a3b5b291ee7e1427f11b8ab"
build_date: "2018-06-19T10:43:42.492Z"
size_mb: 2227
size: 732024863
sif: "https://datasets.datalad.org/shub/sschmeier/simg-chip/latest/2018-06-19-2a1d5370-ceadcb88/ceadcb882a3b5b291ee7e1427f11b8ab.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/simg-chip/latest/2018-06-19-2a1d5370-ceadcb88/
recipe: https://datasets.datalad.org/shub/sschmeier/simg-chip/latest/2018-06-19-2a1d5370-ceadcb88/Singularity
collection: sschmeier/simg-chip
---

# sschmeier/simg-chip:latest

```bash
$ singularity pull shub://sschmeier/simg-chip:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.5.4

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
   echo "We add conda channels and install tools."
   conda config --add channels defaults
   conda config --add channels conda-forge
   conda config --add channels bioconda
   conda install --yes colorama=0.3.9
   conda install --yes snakemake=5.1.4
   conda install --yes bedtools=2.27.1
   conda install --yes scipy=1.1
   conda install --yes mysql=5.7.20
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/simg-chip](https://github.com/sschmeier/simg-chip)
 - License: None

