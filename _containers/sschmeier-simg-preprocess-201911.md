---
id: 11484
name: "sschmeier/simg-preprocess"
branch: "master"
tag: "201911"
commit: "86d5ac4e7d3191d7112647297f5846a1504aba09"
version: "47c2061613c79d79c67c939521723894eb930aeca2d8c8b6e0643a30d43797b8"
build_date: "2020-11-01T12:44:39.614Z"
size_mb: 656.68359375
size: 688582656
sif: "https://datasets.datalad.org/shub/sschmeier/simg-preprocess/201911/2020-11-01-86d5ac4e-47c20616/47c2061613c79d79c67c939521723894eb930aeca2d8c8b6e0643a30d43797b8.sif"
url: https://datasets.datalad.org/shub/sschmeier/simg-preprocess/201911/2020-11-01-86d5ac4e-47c20616/
recipe: https://datasets.datalad.org/shub/sschmeier/simg-preprocess/201911/2020-11-01-86d5ac4e-47c20616/Singularity
collection: sschmeier/simg-preprocess
---

# sschmeier/simg-preprocess:201911

```bash
$ singularity pull shub://sschmeier/simg-preprocess:201911
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%labels
   AUTHOR s.schmeier@protonmail.com

%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container
  export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
  unset CONDA_DEFAULT_ENV
  export ANACONDA_HOME=/opt/conda


%post
   export PATH=/opt/conda/bin:$PATH
   conda config --add channels defaults
   conda config --add channels bioconda
   conda config --add channels conda-forge
   conda update -n base -c defaults conda
   conda install --yes atropos=1.1.22 bbmap=38.71 cutadapt=2.6 fastp=0.20.0 fastqc=0.11.8 flexbar=3.5.0 multiqc=1.7 fastq-screen=0.13.0 seqtk=1.3
   # Clean up
   conda clean --index-cache --tarballs --packages --yes
   # build date
   touch /`date -u -Iseconds`
```

## Collection

 - Name: [sschmeier/simg-preprocess](https://github.com/sschmeier/simg-preprocess)
 - License: None

