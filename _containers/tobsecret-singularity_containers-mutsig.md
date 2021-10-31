---
id: 9767
name: "tobsecret/singularity_containers"
branch: "master"
tag: "mutsig"
commit: "ecb1ce893f5d7aaf4f1c8c6bceec1dfc55b510d5"
version: "99edd24f65baf633ba87f0bf5e34e540"
build_date: "2019-06-25T05:49:30.491Z"
size_mb: 3215
size: 1531506719
sif: "https://datasets.datalad.org/shub/tobsecret/singularity_containers/mutsig/2019-06-25-ecb1ce89-99edd24f/99edd24f65baf633ba87f0bf5e34e540.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/tobsecret/singularity_containers/mutsig/2019-06-25-ecb1ce89-99edd24f/
recipe: https://datasets.datalad.org/shub/tobsecret/singularity_containers/mutsig/2019-06-25-ecb1ce89-99edd24f/Singularity
collection: tobsecret/singularity_containers
---

# tobsecret/singularity_containers:mutsig

```bash
$ singularity pull shub://tobsecret/singularity_containers:mutsig
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.6.14

%labels
AUTHOR tobi.schraink@gmail.com

%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container
export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
unset CONDA_DEFAULT_ENV
export ANACONDA_HOME=/opt/conda

%post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This is going to be executed after the base container has been downloaded
export PATH=/opt/conda/bin:$PATH
conda install --yes bioconda::bioconductor-signer=1.8.0 conda-forge::dask=1.2.2 bioconda::tabix=0.2.6 bioconda::bioconductor-somaticsignatures=2.18.0 r::r-argparse=1.1.1 bioconda::samtools=1.9
```

## Collection

 - Name: [tobsecret/singularity_containers](https://github.com/tobsecret/singularity_containers)
 - License: None

