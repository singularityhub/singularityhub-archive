---
id: 10489
name: "tkolisnik/singularity-for-crc-ml"
branch: "master"
tag: "latest"
commit: "2a64f635b0fa61ae47a96b1b84e6f0c0f9354c13"
version: "690044f83ee0a778042857e58d630963"
build_date: "2019-08-06T06:33:22.895Z"
size_mb: 1984.0
size: 636063775
sif: "https://datasets.datalad.org/shub/tkolisnik/singularity-for-crc-ml/latest/2019-08-06-2a64f635-690044f8/690044f83ee0a778042857e58d630963.sif"
url: https://datasets.datalad.org/shub/tkolisnik/singularity-for-crc-ml/latest/2019-08-06-2a64f635-690044f8/
recipe: https://datasets.datalad.org/shub/tkolisnik/singularity-for-crc-ml/latest/2019-08-06-2a64f635-690044f8/Singularity
collection: tkolisnik/singularity-for-crc-ml
---

# tkolisnik/singularity-for-crc-ml:latest

```bash
$ singularity pull shub://tkolisnik/singularity-for-crc-ml:latest
```

## Singularity Recipe

```singularity
#August 5 2019
# Filename: Singularity
Bootstrap: docker
From: continuumio/miniconda3:4.6.14

%labels
   AUTHOR tkolisnik@gmail.com
   
############################################################################
# This sets global environment variables for anything run within the container
############################################################################

%environment
  export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
  unset CONDA_DEFAULT_ENV
  export ANACONDA_HOME=/opt/conda

################################
# Additional packages to install 
################################

%post
   export PATH=/opt/conda/bin:$PATH
   echo "Add conda channels."
   conda config --add channels defaults
   conda config --add channels conda-forge
   conda install --yes scikit-learn scipy matplotlib pandas numpy rpy2 libgfortran
   conda update libgfortran --force
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [tkolisnik/singularity-for-crc-ml](https://github.com/tkolisnik/singularity-for-crc-ml)
 - License: None

