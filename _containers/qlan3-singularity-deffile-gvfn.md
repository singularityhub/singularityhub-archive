---
id: 10319
name: "qlan3/singularity-deffile"
branch: "master"
tag: "gvfn"
commit: "702d7ea2c45934041137f7216ee710055d8cefa6"
version: "44106e0717aa0dab6a33dcea41d84c3ab91722b6d16e55fa5efea26c65bcf122"
build_date: "2019-07-31T22:34:22.158Z"
size_mb: 1804.7421875
size: 1892409344
sif: "https://datasets.datalad.org/shub/qlan3/singularity-deffile/gvfn/2019-07-31-702d7ea2-44106e07/44106e0717aa0dab6a33dcea41d84c3ab91722b6d16e55fa5efea26c65bcf122.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/qlan3/singularity-deffile/gvfn/2019-07-31-702d7ea2-44106e07/
recipe: https://datasets.datalad.org/shub/qlan3/singularity-deffile/gvfn/2019-07-31-702d7ea2-44106e07/Singularity
collection: qlan3/singularity-deffile
---

# qlan3/singularity-deffile:gvfn

```bash
$ singularity pull shub://qlan3/singularity-deffile:gvfn
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
    export PATH="/usr/local/miniconda3/bin:$PATH"

%post
    apt-get update && apt-get -y upgrade
    
    # Install basic packages
    apt-get -y install vim wget bzip2 parallel git \
    libopenmpi-dev libsm6 libxrender-dev build-essential python-dev python-setuptools
    
    # Install miniconda
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /usr/local/miniconda3
    rm Miniconda3-latest-Linux-x86_64.sh

    # Install tensorflow
    /usr/local/miniconda3/bin/conda install -y -c conda-forge tensorflow
    
    # Install tensorboardX
    /usr/local/miniconda3/bin/pip install tensorboardX
    
    # Install PyTorch 
    /usr/local/miniconda3/bin/conda install -y pytorch-cpu torchvision-cpu -c pytorch

    # Install PyTorch text and spacy
    /usr/local/miniconda3/bin/pip install torchtext
    /usr/local/miniconda3/bin/pip install spacy
    /usr/local/miniconda3/bin/python -m spacy download en

    # Install seaborn pyarrow tqdm pandas psutil opencv-python
    /usr/local/miniconda3/bin/conda install -y -c conda-forge matplotlib
    /usr/local/miniconda3/bin/conda install -y seaborn
    /usr/local/miniconda3/bin/pip install pyarrow
    /usr/local/miniconda3/bin/conda install -y tqdm
    /usr/local/miniconda3/bin/conda install -y pandas
    /usr/local/miniconda3/bin/conda install -y -c anaconda psutil
```

## Collection

 - Name: [qlan3/singularity-deffile](https://github.com/qlan3/singularity-deffile)
 - License: [MIT License](https://api.github.com/licenses/mit)

