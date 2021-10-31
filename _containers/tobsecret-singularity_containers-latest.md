---
id: 9665
name: "tobsecret/singularity_containers"
branch: "master"
tag: "latest"
commit: "77745d0c51c0155b1b4127b8aa664d19061982b4"
version: "7390be6b2a1c94238d4945fe6a8fe41d"
build_date: "2019-06-07T11:19:42.482Z"
size_mb: 3199
size: 1526845471
sif: "https://datasets.datalad.org/shub/tobsecret/singularity_containers/latest/2019-06-07-77745d0c-7390be6b/7390be6b2a1c94238d4945fe6a8fe41d.simg"
url: https://datasets.datalad.org/shub/tobsecret/singularity_containers/latest/2019-06-07-77745d0c-7390be6b/
recipe: https://datasets.datalad.org/shub/tobsecret/singularity_containers/latest/2019-06-07-77745d0c-7390be6b/Singularity
collection: tobsecret/singularity_containers
---

# tobsecret/singularity_containers:latest

```bash
$ singularity pull shub://tobsecret/singularity_containers:latest
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
conda install --yes bioconda::bioconductor-signer=1.8.0 conda-forge::dask=1.2.2 bioconda::tabix=0.2.6 bioconda::bioconductor-somaticsignatures=2.18.0
```

## Collection

 - Name: [tobsecret/singularity_containers](https://github.com/tobsecret/singularity_containers)
 - License: None

