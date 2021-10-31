---
id: 12556
name: "sschmeier/metafunc-container"
branch: "master"
tag: "0.0.7"
commit: "1def6be43406a70924eae7a2135d0c1f39bd3d34"
version: "b0e3fded261e78223517fb6659b4a70386e6ab9f301632304b01c49bd6a9573f"
build_date: "2020-03-26T23:14:08.117Z"
size_mb: 564.27734375
size: 591687680
sif: "https://datasets.datalad.org/shub/sschmeier/metafunc-container/0.0.7/2020-03-26-1def6be4-b0e3fded/b0e3fded261e78223517fb6659b4a70386e6ab9f301632304b01c49bd6a9573f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/metafunc-container/0.0.7/2020-03-26-1def6be4-b0e3fded/
recipe: https://datasets.datalad.org/shub/sschmeier/metafunc-container/0.0.7/2020-03-26-1def6be4-b0e3fded/Singularity
collection: sschmeier/metafunc-container
---

# sschmeier/metafunc-container:0.0.7

```bash
$ singularity pull shub://sschmeier/metafunc-container:0.0.7
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
   conda install --yes kaiju=1.7.3 taxonkit=0.3.0 sqlite=3.30.1 pandas goatools=0.9.9 bbmap=38.75 fastp=0.20.0 STAR=2.7.3a subread=2.0.0
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/metafunc-container](https://github.com/sschmeier/metafunc-container)
 - License: [MIT License](https://api.github.com/licenses/mit)

