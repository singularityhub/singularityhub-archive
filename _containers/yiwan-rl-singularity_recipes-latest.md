---
id: 15707
name: "yiwan-rl/singularity_recipes"
branch: "master"
tag: "latest"
commit: "c0154692f869689ee71d2ae0fd8aff66c8c9a119"
version: "b416e27f73a6fc46568a7e97df11001d"
build_date: "2021-03-15T22:01:33.055Z"
size_mb: 4318.0
size: 1947906079
sif: "https://datasets.datalad.org/shub/yiwan-rl/singularity_recipes/latest/2021-03-15-c0154692-b416e27f/b416e27f73a6fc46568a7e97df11001d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/yiwan-rl/singularity_recipes/latest/2021-03-15-c0154692-b416e27f/
recipe: https://datasets.datalad.org/shub/yiwan-rl/singularity_recipes/latest/2021-03-15-c0154692-b416e27f/Singularity
collection: yiwan-rl/singularity_recipes
---

# yiwan-rl/singularity_recipes:latest

```bash
$ singularity pull shub://yiwan-rl/singularity_recipes:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
    export PATH="/usr/local/miniconda3/bin:$PATH"

%post
    apt-get -y update
    apt-get -y install wget bzip2 parallel git libopenmpi-dev libsm6 libxrender-dev build-essential python-dev swig python-pygame python-setuptools

    # Installing miniconda
    wget https://repo.continuum.io/miniconda/Miniconda3-py37_4.9.2-Linux-x86_64.sh
    bash Miniconda3-py37_4.9.2-Linux-x86_64.sh -b -p /usr/local/miniconda3

    # Installing tensorflow
    /usr/local/miniconda3/bin/conda install -y -c conda-forge tensorflow

    # Installing tensorboardX
    /usr/local/miniconda3/bin/pip install tensorboardX

    # Installing shapely
    /usr/local/miniconda3/bin/conda install -y shapely

    git clone https://github.com/pybox2d/pybox2d
    cd pybox2d
    /usr/local/miniconda3/bin/python setup.py build
    /usr/local/miniconda3/bin/python setup.py install

    # Installing PyTorch
    /usr/local/miniconda3/bin/conda install pytorch-cpu==1.1.0 torchvision-cpu==0.3.0 cpuonly -c pytorch

    # Installing Seaborn
    /usr/local/miniconda3/bin/conda install -y -c conda-forge matplotlib
    /usr/local/miniconda3/bin/conda install -y seaborn

    cd /home
    git clone https://github.com/openai/baselines.git
    cd baselines
    git reset --hard 8e56dd
    /usr/local/miniconda3/bin/pip install -e .

    # Installing Pygame
    /usr/local/miniconda3/bin/pip install pygame

    # Installing PLE
    cd /home
    git clone https://github.com/ntasfi/PyGame-Learning-Environment
    cd PyGame-Learning-Environment
    /usr/local/miniconda3/bin/pip install -e .

    # Installing MinAtar
    cd /home
    git clone https://github.com/kenjyoung/MinAtar.git
    cd MinAtar
    /usr/local/miniconda3/bin/python setup.py install

    # Install gym_pygame
    cd /home
    git clone https://github.com/qlan3/gym-games.git
    cd gym-games
    /usr/local/miniconda3/bin/pip install -e .

    # Installing AlphaEx 
    cd /home
    git clone https://github.com/AmiiThinks/AlphaEx.git
    cd AlphaEx 
    /usr/local/miniconda3/bin/pip install -e .
```

## Collection

 - Name: [yiwan-rl/singularity_recipes](https://github.com/yiwan-rl/singularity_recipes)
 - License: None

