---
id: 5684
name: "muhammadzaheer/singularity-recipes"
branch: "master"
tag: "deeprl"
commit: "d678dd88c376aad3306c60c67f4bc6d97483f49f"
version: "900548a3ecda9421188805554bb73373"
build_date: "2018-11-24T04:49:42.379Z"
size_mb: 4351
size: 1972510751
sif: "https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/deeprl/2018-11-24-d678dd88-900548a3/900548a3ecda9421188805554bb73373.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/muhammadzaheer/singularity-recipes/deeprl/2018-11-24-d678dd88-900548a3/
recipe: https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/deeprl/2018-11-24-d678dd88-900548a3/Singularity
collection: muhammadzaheer/singularity-recipes
---

# muhammadzaheer/singularity-recipes:deeprl

```bash
$ singularity pull shub://muhammadzaheer/singularity-recipes:deeprl
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: singularityhub/ubuntu:latest

%environment
    export PATH="/usr/local/miniconda3/bin:$PATH"

%post
    apt-get -y update
    apt-get -y install wget bzip2 parallel git libopenmpi-dev libsm6 libxrender-dev build-essential python-dev swig python-pygame python-setuptools

    # Installing miniconda
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /usr/local/miniconda3
    rm Miniconda3-latest-Linux-x86_64.sh

    # Installing tensorflow
    /usr/local/miniconda3/bin/conda install -y -c conda-forge tensorflow
    
    # Installing tensorboardX
    /usr/local/miniconda3/bin/pip install tensorboardX
    
    # Installing PyTorch 
    /usr/local/miniconda3/bin/conda install -y pytorch-cpu torchvision-cpu -c pytorch

    # Installing Seaborn
    /usr/local/miniconda3/bin/conda install -y -c conda-forge matplotlib
    /usr/local/miniconda3/bin/conda install -y seaborn
    
    # Installing shapely
    /usr/local/miniconda3/bin/conda install -y shapely

    cd /home
    git clone https://github.com/openai/baselines.git
    cd baselines
    git reset --hard 8e56dd
    /usr/local/miniconda3/bin/pip install -e .

    git clone https://github.com/pybox2d/pybox2d
    cd pybox2d
    /usr/local/miniconda3/bin/python setup.py build
    /usr/local/miniconda3/bin/python setup.py install
```

## Collection

 - Name: [muhammadzaheer/singularity-recipes](https://github.com/muhammadzaheer/singularity-recipes)
 - License: None

