---
id: 12617
name: "sschmeier/metafunc-container"
branch: "master"
tag: "0.0.8"
commit: "87896ab311528ed7ec2553a956e5477ebb99b6b6"
version: "709139a3e57f6c9362d1f235a973b05e57fe831e14b83387bdd05aaef8f3603e"
build_date: "2020-08-31T03:22:17.979Z"
size_mb: 564.18359375
size: 591589376
sif: "https://datasets.datalad.org/shub/sschmeier/metafunc-container/0.0.8/2020-08-31-87896ab3-709139a3/709139a3e57f6c9362d1f235a973b05e57fe831e14b83387bdd05aaef8f3603e.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/metafunc-container/0.0.8/2020-08-31-87896ab3-709139a3/
recipe: https://datasets.datalad.org/shub/sschmeier/metafunc-container/0.0.8/2020-08-31-87896ab3-709139a3/Singularity
collection: sschmeier/metafunc-container
---

# sschmeier/metafunc-container:0.0.8

```bash
$ singularity pull shub://sschmeier/metafunc-container:0.0.8
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%labels
   AUTHOR s.schmeier@pm.me

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
   conda config --add channels bioconda
   conda config --add channels conda-forge
   echo "We install tools."
   conda install --yes kaiju=1.7.3 taxonkit=0.3.0 sqlite=3.30.1 pandas goatools=0.9.9 bbmap=38.75 fastp=0.20.0 STAR=2.7.3a subread=2.0.0 scipy numpy
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/metafunc-container](https://github.com/sschmeier/metafunc-container)
 - License: [MIT License](https://api.github.com/licenses/mit)

