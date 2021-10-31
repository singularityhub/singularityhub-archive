---
id: 10950
name: "sschmeier/simg-rnaseqvariants"
branch: "master"
tag: "latest"
commit: "d0cff53655300d72f3ff5d578a730a94f8650102"
version: "1f5f26c300666d0641c02f928ac6d5824285415b5f8efef83b0e1ef952b8c3a1"
build_date: "2019-11-04T20:28:25.217Z"
size_mb: 916.1953125
size: 960700416
sif: "https://datasets.datalad.org/shub/sschmeier/simg-rnaseqvariants/latest/2019-11-04-d0cff536-1f5f26c3/1f5f26c300666d0641c02f928ac6d5824285415b5f8efef83b0e1ef952b8c3a1.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/simg-rnaseqvariants/latest/2019-11-04-d0cff536-1f5f26c3/
recipe: https://datasets.datalad.org/shub/sschmeier/simg-rnaseqvariants/latest/2019-11-04-d0cff536-1f5f26c3/Singularity
collection: sschmeier/simg-rnaseqvariants
---

# sschmeier/simg-rnaseqvariants:latest

```bash
$ singularity pull shub://sschmeier/simg-rnaseqvariants:latest
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
  export PATH="/opt/conda/bin:$PATH"
  unset CONDA_DEFAULT_ENV
  export ANACONDA_HOME=/opt/conda


%post
   export PATH=/opt/conda/bin:$PATH
   #conda update --yes -q conda 
   echo "We add conda channels."
   conda config --add channels defaults
   conda config --add channels bioconda
   conda config --add channels conda-forge
   conda update -n base -c defaults conda
   echo "We install tools."
   conda install --yes star picard samtools tabix sambamba gatk4 freebayes snpeff snpsift bcftools multiqc
   conda clean --index-cache --tarballs --packages --yes
   conda list > /conda.txt
   touch /`date -u -Iseconds`


# 20190918
# star 2.7.2b
# picard 2.20.8
# samtools 1.9
# tabix 0.2.6
# sambamba 0.7.0
# gatk4 4.1.3
# freebayes 1.3.1
# snpeff 4.3.1
# snpsift 4.3.1
# bcftools 1.9
# multiqc 1.7
```

## Collection

 - Name: [sschmeier/simg-rnaseqvariants](https://github.com/sschmeier/simg-rnaseqvariants)
 - License: None

