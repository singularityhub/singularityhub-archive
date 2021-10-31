---
id: 3125
name: "sschmeier/biotools"
branch: "master"
tag: "01"
commit: "b44096ac7323ec8d8dfa5d50d0a76f9985633158"
version: "03d0fd84a36e504b153f5ba1e262e69f"
build_date: "2018-06-09T14:17:50.088Z"
size_mb: 1106
size: 414863391
sif: "https://datasets.datalad.org/shub/sschmeier/biotools/01/2018-06-09-b44096ac-03d0fd84/03d0fd84a36e504b153f5ba1e262e69f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/biotools/01/2018-06-09-b44096ac-03d0fd84/
recipe: https://datasets.datalad.org/shub/sschmeier/biotools/01/2018-06-09-b44096ac-03d0fd84/Singularity
collection: sschmeier/biotools
---

# sschmeier/biotools:01

```bash
$ singularity pull shub://sschmeier/biotools:01
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.4.10

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
   conda install --yes bwa=0.7.15
   conda install --yes sickle-trim=1.33
   conda install --yes subread=1.6.1
   conda install --yes samtools=1.8
   conda install --yes sra-tools=2.8.2=0
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/biotools](https://github.com/sschmeier/biotools)
 - License: None

