---
id: 15748
name: "martinobertoni/BBBpredictor"
branch: "main"
tag: "latest"
commit: "14e641c332071f2aee45fddb09e65ab03c926264"
version: "9aa127d603a320cd746afad5ad8d811f"
build_date: "2021-04-14T16:25:50.350Z"
size_mb: 4505.0
size: 2137473055
sif: "https://datasets.datalad.org/shub/martinobertoni/BBBpredictor/latest/2021-04-14-14e641c3-9aa127d6/9aa127d603a320cd746afad5ad8d811f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/martinobertoni/BBBpredictor/latest/2021-04-14-14e641c3-9aa127d6/
recipe: https://datasets.datalad.org/shub/martinobertoni/BBBpredictor/latest/2021-04-14-14e641c3-9aa127d6/Singularity
collection: martinobertoni/BBBpredictor
---

# martinobertoni/BBBpredictor:latest

```bash
$ singularity pull shub://martinobertoni/BBBpredictor:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:8

%labels
    Author: Nicolas Soler
    Date: 27 Nov. 2020

%environment
    # PATHS
    export PATH=/opt/miniconda3/bin:$PATH
    . /opt/miniconda3/etc/profile.d/conda.sh
    conda activate sign

%post
    # bind paths
    
    # update yum
    yum update -y

    # basic packages
    yum install -y gcc \
                   gcc-c++ \
                   gcc-gfortran \
                   cmake \
                   make \
                   git \
                   wget \
                   curl \
                   which \
                   vim \
                   bzip2 \
                   bzip2-devel \
                   file \
                   libXrender \
                   libXext \


    # conda
    mkdir -p /opt/miniconda3
    cd /opt/miniconda3 
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh -p /opt/miniconda3 -b -f
    rm Miniconda3-latest-Linux-x86_64.sh
    export PATH=/opt/miniconda3/bin:$PATH

    # create and activate conda enviroment
    #conda init bash
    conda update conda -y
    conda create --no-default-packages -n sign -y python=3.7 tensorflow=1.14.0
    source activate sign
    conda install -y -c conda-forge rdkit
    conda install -y joblib


    # The signaturizer package
    pip install signaturizer==1.1.7

    # utility packages
    conda install -y numpy
    conda install -y -c anaconda scikit-learn=0.20.3        # Machine learning library

    pip install wget                              # download library

%files
    ./run_BBB_predictor.py /opt
    ./rf_from_signZ_paper_full.joblib /opt
    ./NNmodels /opt
%runscript
    python /opt/run_BBB_predictor.py "$@"
```

## Collection

 - Name: [martinobertoni/BBBpredictor](https://github.com/martinobertoni/BBBpredictor)
 - License: [MIT License](https://api.github.com/licenses/mit)

