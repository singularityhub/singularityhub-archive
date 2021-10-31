---
id: 3920
name: "sschmeier/simg-solexaqa"
branch: "master"
tag: "latest"
commit: "c1e6a4cc85a2744ac2fd76573c68b7e223038780"
version: "3eeb0c03bbbb48f415ba7a950601a958"
build_date: "2019-11-05T06:19:37.331Z"
size_mb: 793
size: 290189343
sif: "https://datasets.datalad.org/shub/sschmeier/simg-solexaqa/latest/2019-11-05-c1e6a4cc-3eeb0c03/3eeb0c03bbbb48f415ba7a950601a958.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/simg-solexaqa/latest/2019-11-05-c1e6a4cc-3eeb0c03/
recipe: https://datasets.datalad.org/shub/sschmeier/simg-solexaqa/latest/2019-11-05-c1e6a4cc-3eeb0c03/Singularity
collection: sschmeier/simg-solexaqa
---

# sschmeier/simg-solexaqa:latest

```bash
$ singularity pull shub://sschmeier/simg-solexaqa:latest
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
  export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin"
  unset CONDA_DEFAULT_ENV
  export ANACONDA_HOME=/opt/conda
  export LANG=C.UTF-8
  export LC_ALL=C.UTF-8

%post
   export PATH=/opt/conda/bin:$PATH
   echo "We add conda channels."
   conda config --add channels defaults
   conda config --add channels conda-forge
   conda config --add channels bioconda
   echo "We install some utils."
   apt-get update --fix-missing && apt-get install -y apt-utils && apt-get install -y unzip && apt-get clean
   ## SolexaQA++
   echo "Download SolexaQA++ from https://svwh.dl.sourceforge.net/project/solexaqa/src/SolexaQA%2B%2B_v3.1.7.1.zip"
   curl -o solexaqa.zip https://svwh.dl.sourceforge.net/project/solexaqa/src/SolexaQA%2B%2B_v3.1.7.1.zip
   unzip solexaqa.zip 
   mv /Linux_x64/SolexaQA++ /usr/local/bin
   ## R
   echo "We install conda-based tools."
   conda install --yes r-base=3.5.1
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/simg-solexaqa](https://github.com/sschmeier/simg-solexaqa)
 - License: None

