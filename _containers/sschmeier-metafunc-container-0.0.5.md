---
id: 12385
name: "sschmeier/metafunc-container"
branch: "master"
tag: "0.0.5"
commit: "789a9d5d00dd77c148a0125fb60ce591fb83e1a2"
version: "670efe92f3c9c348086a43068fbeca162eef6694f6e935004f66f8b43f1736a7"
build_date: "2020-02-27T02:06:56.578Z"
size_mb: 530.3515625
size: 556113920
sif: "https://datasets.datalad.org/shub/sschmeier/metafunc-container/0.0.5/2020-02-27-789a9d5d-670efe92/670efe92f3c9c348086a43068fbeca162eef6694f6e935004f66f8b43f1736a7.sif"
url: https://datasets.datalad.org/shub/sschmeier/metafunc-container/0.0.5/2020-02-27-789a9d5d-670efe92/
recipe: https://datasets.datalad.org/shub/sschmeier/metafunc-container/0.0.5/2020-02-27-789a9d5d-670efe92/Singularity
collection: sschmeier/metafunc-container
---

# sschmeier/metafunc-container:0.0.5

```bash
$ singularity pull shub://sschmeier/metafunc-container:0.0.5
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
   conda install --yes kaiju=1.7.3 taxonkit=0.3.0 sqlite=3.30.1 pandas goatools=0.9.9 bbmap=38.75 fastp=0.20.0
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/metafunc-container](https://github.com/sschmeier/metafunc-container)
 - License: [MIT License](https://api.github.com/licenses/mit)

