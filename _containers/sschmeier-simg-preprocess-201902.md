---
id: 7370
name: "sschmeier/simg-preprocess"
branch: "master"
tag: "201902"
commit: "0f78919f97c92c3ade75c75958b49491e21525a7"
version: "bdca9d51e73d1bef04216f2bddfd84b2"
build_date: "2019-02-22T21:13:26.474Z"
size_mb: 2564
size: 923623455
sif: "https://datasets.datalad.org/shub/sschmeier/simg-preprocess/201902/2019-02-22-0f78919f-bdca9d51/bdca9d51e73d1bef04216f2bddfd84b2.simg"
url: https://datasets.datalad.org/shub/sschmeier/simg-preprocess/201902/2019-02-22-0f78919f-bdca9d51/
recipe: https://datasets.datalad.org/shub/sschmeier/simg-preprocess/201902/2019-02-22-0f78919f-bdca9d51/Singularity
collection: sschmeier/simg-preprocess
---

# sschmeier/simg-preprocess:201902

```bash
$ singularity pull shub://sschmeier/simg-preprocess:201902
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.5.12

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
   conda install --yes snakemake=5.4.2 atropos=1.1.21 bbmap=38.22 cutadapt=1.18 fastp=0.19.5 fastqc=0.11.7 flexbar=3.3.0 multiqc=1.7 
   # Clean up
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/simg-preprocess](https://github.com/sschmeier/simg-preprocess)
 - License: None

