---
id: 7927
name: "sschmeier/simg-preprocess"
branch: "master"
tag: "201903"
commit: "4f69b5b582c44ef793da9072f8c287fb9bdc0c86"
version: "703a13100bc955268e098533d4197a38"
build_date: "2019-03-24T23:26:33.912Z"
size_mb: 1957
size: 697323551
sif: "https://datasets.datalad.org/shub/sschmeier/simg-preprocess/201903/2019-03-24-4f69b5b5-703a1310/703a13100bc955268e098533d4197a38.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/simg-preprocess/201903/2019-03-24-4f69b5b5-703a1310/
recipe: https://datasets.datalad.org/shub/sschmeier/simg-preprocess/201903/2019-03-24-4f69b5b5-703a1310/Singularity
collection: sschmeier/simg-preprocess
---

# sschmeier/simg-preprocess:201903

```bash
$ singularity pull shub://sschmeier/simg-preprocess:201903
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
   conda install --yes snakemake=5.4.3 atropos=1.1.21 bbmap=38.22 cutadapt=1.18 fastp=0.19.5 fastqc=0.11.7 flexbar multiqc=1.7 fastq-screen
   # Clean up
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/simg-preprocess](https://github.com/sschmeier/simg-preprocess)
 - License: None

