---
id: 10951
name: "sschmeier/simg-rnaseqvariants2"
branch: "master"
tag: "latest"
commit: "27f58be5ca73306fa5baecb0868aab835fb59a49"
version: "7f8fb5def04bb860f15e9240b3a7ed5c970d5c8ca3d1e972e69e718c4616ec93"
build_date: "2019-11-04T20:23:35.606Z"
size_mb: 162.92578125
size: 170840064
sif: "https://datasets.datalad.org/shub/sschmeier/simg-rnaseqvariants2/latest/2019-11-04-27f58be5-7f8fb5de/7f8fb5def04bb860f15e9240b3a7ed5c970d5c8ca3d1e972e69e718c4616ec93.sif"
url: https://datasets.datalad.org/shub/sschmeier/simg-rnaseqvariants2/latest/2019-11-04-27f58be5-7f8fb5de/
recipe: https://datasets.datalad.org/shub/sschmeier/simg-rnaseqvariants2/latest/2019-11-04-27f58be5-7f8fb5de/Singularity
collection: sschmeier/simg-rnaseqvariants2
---

# sschmeier/simg-rnaseqvariants2:latest

```bash
$ singularity pull shub://sschmeier/simg-rnaseqvariants2:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda2

%labels
   AUTHOR s.schmeier@protonmail.com

%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container
  export PATH="/opt/conda/bin:$PATH"
  unset CONDA_DEFAULT_ENV
  export ANACONDA_HOME=/opt/conda
  #export LANG=en_US.UTF-8
  #export LC_ALL=en_US.UTF-8
  #export LANGUAGE=en_US.UTF-8

%post
   # CONDA
   export PATH=/opt/conda/bin:$PATH
   #conda update --yes -q conda 
   echo "We add conda channels."
   conda config --add channels defaults
   conda config --add channels bioconda
   conda config --add channels conda-forge
   conda config --add channels aroth85
   conda update -n base -c defaults conda
   echo "We install tools."
   conda install --yes opossum platypus-variant
   conda clean --index-cache --tarballs --packages --yes
   conda list > /conda.txt
   touch /`date -u -Iseconds`
```

## Collection

 - Name: [sschmeier/simg-rnaseqvariants2](https://github.com/sschmeier/simg-rnaseqvariants2)
 - License: None

