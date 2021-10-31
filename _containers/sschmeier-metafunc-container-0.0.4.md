---
id: 12123
name: "sschmeier/metafunc-container"
branch: "master"
tag: "0.0.4"
commit: "63635d598ad16c2dbe5773325259146e9943d065"
version: "3fcc1141376e7fcbcff8220f39e94b5551690d091da14e97d44ead9dff3325c3"
build_date: "2020-08-31T20:54:29.317Z"
size_mb: 528.26953125
size: 553930752
sif: "https://datasets.datalad.org/shub/sschmeier/metafunc-container/0.0.4/2020-08-31-63635d59-3fcc1141/3fcc1141376e7fcbcff8220f39e94b5551690d091da14e97d44ead9dff3325c3.sif"
url: https://datasets.datalad.org/shub/sschmeier/metafunc-container/0.0.4/2020-08-31-63635d59-3fcc1141/
recipe: https://datasets.datalad.org/shub/sschmeier/metafunc-container/0.0.4/2020-08-31-63635d59-3fcc1141/Singularity
collection: sschmeier/metafunc-container
---

# sschmeier/metafunc-container:0.0.4

```bash
$ singularity pull shub://sschmeier/metafunc-container:0.0.4
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
   conda install --yes kaiju=1.7.3 taxonkit=0.3.0 sqlite=3.30.1 pandas goatools=0.9.9 bbmap=38.75
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/metafunc-container](https://github.com/sschmeier/metafunc-container)
 - License: [MIT License](https://api.github.com/licenses/mit)

