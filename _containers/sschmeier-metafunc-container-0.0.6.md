---
id: 12387
name: "sschmeier/metafunc-container"
branch: "master"
tag: "0.0.6"
commit: "bdde9021faaf7729721053ccf5228ef6b3061151"
version: "504e5efdc68bdffb3881a29a07d85f6f3d2d8cc0ddf8e422e816d24416882a2f"
build_date: "2020-03-15T21:06:03.898Z"
size_mb: 533.97265625
size: 559910912
sif: "https://datasets.datalad.org/shub/sschmeier/metafunc-container/0.0.6/2020-03-15-bdde9021-504e5efd/504e5efdc68bdffb3881a29a07d85f6f3d2d8cc0ddf8e422e816d24416882a2f.sif"
url: https://datasets.datalad.org/shub/sschmeier/metafunc-container/0.0.6/2020-03-15-bdde9021-504e5efd/
recipe: https://datasets.datalad.org/shub/sschmeier/metafunc-container/0.0.6/2020-03-15-bdde9021-504e5efd/Singularity
collection: sschmeier/metafunc-container
---

# sschmeier/metafunc-container:0.0.6

```bash
$ singularity pull shub://sschmeier/metafunc-container:0.0.6
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
   conda install --yes kaiju=1.7.3 taxonkit=0.3.0 sqlite=3.30.1 pandas goatools=0.9.9 bbmap=38.75 fastp=0.20.0 STAR=2.7.3a
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/metafunc-container](https://github.com/sschmeier/metafunc-container)
 - License: [MIT License](https://api.github.com/licenses/mit)

