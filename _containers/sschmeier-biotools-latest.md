---
id: 3109
name: "sschmeier/biotools"
branch: "master"
tag: "latest"
commit: "69ab5190225d31a6b7a251282c399822104abe37"
version: "feb2aa21447cb6b3684eacad17c30713"
build_date: "2021-04-07T18:39:15.946Z"
size_mb: 568
size: 207347743
sif: "https://datasets.datalad.org/shub/sschmeier/biotools/latest/2021-04-07-69ab5190-feb2aa21/feb2aa21447cb6b3684eacad17c30713.simg"
url: https://datasets.datalad.org/shub/sschmeier/biotools/latest/2021-04-07-69ab5190-feb2aa21/
recipe: https://datasets.datalad.org/shub/sschmeier/biotools/latest/2021-04-07-69ab5190-feb2aa21/Singularity
collection: sschmeier/biotools
---

# sschmeier/biotools:latest

```bash
$ singularity pull shub://sschmeier/biotools:latest
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
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/biotools](https://github.com/sschmeier/biotools)
 - License: None

