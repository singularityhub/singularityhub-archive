---
id: 15850
name: "dpmerrell/pynbs-singularity"
branch: "main"
tag: "latest"
commit: "8f085b43e5b81932b04a5404abb07a8a925abf89"
version: "9f45ebf6e20913f46461935032294507"
build_date: "2021-04-02T20:14:59.157Z"
size_mb: 2412.0
size: 846020639
sif: "https://datasets.datalad.org/shub/dpmerrell/pynbs-singularity/latest/2021-04-02-8f085b43-9f45ebf6/9f45ebf6e20913f46461935032294507.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dpmerrell/pynbs-singularity/latest/2021-04-02-8f085b43-9f45ebf6/
recipe: https://datasets.datalad.org/shub/dpmerrell/pynbs-singularity/latest/2021-04-02-8f085b43-9f45ebf6/Singularity
collection: dpmerrell/pynbs-singularity
---

# dpmerrell/pynbs-singularity:latest

```bash
$ singularity pull shub://dpmerrell/pynbs-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda

%labels
AUTHOR dmerrell@cs.wisc.edu 

# I took some inspiration from this webpage:
# https://reproducibility.sschmeier.com/container/index.html#building-your-own-singularity-container-locally

############################################
%files
    run_pyNBS.py /run_pyNBS.py

############################################
%environment
# This sets global environment variables for anything run within the container
export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
export MKL_NUM_THREADS=4
export NUMEXPR_NUM_THREADS=4
export OMP_NUM_THREADS=4

unset CONDA_DEFAULT_ENV
export ANACONDA_HOME=/opt/conda


############################################
%post
# This is going to be executed after the base container has been downloaded
export PATH=/opt/conda/bin:$PATH
conda config --add channels defaults
conda config --add channels conda-forge
conda config --add channels bioconda

# Install dependencies (OLD versions of packages)
conda install --yes -c anaconda mkl-service=1.1.2
conda install --yes networkx=2.0
conda install --yes numpy=1.11.0
conda install --yes scipy=0.17.1
conda install --yes pandas=0.19.0
conda install --yes scikit-learn=0.17.1
conda install --yes seaborn=0.7.1
conda install --yes -c conda-forge lifelines

# Get the pyNBS source code
git clone https://github.com/idekerlab/pyNBS
cd pyNBS

# Install PyNBS
python setup.py install

conda clean --index-cache --tarballs --packages --yes

############################################
%runscript
    exec python /run_pyNBS.py "$@"
```

## Collection

 - Name: [dpmerrell/pynbs-singularity](https://github.com/dpmerrell/pynbs-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

