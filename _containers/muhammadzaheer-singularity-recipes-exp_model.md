---
id: 6848
name: "muhammadzaheer/singularity-recipes"
branch: "master"
tag: "exp_model"
commit: "f1c43d512a2ffd2c4c17bab552b798a572e145b3"
version: "8dede0ceb88e8d9d69c2ef0b961358cc"
build_date: "2019-02-04T09:08:22.084Z"
size_mb: 3973
size: 1812160543
sif: "https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/exp_model/2019-02-04-f1c43d51-8dede0ce/8dede0ceb88e8d9d69c2ef0b961358cc.simg"
url: https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/exp_model/2019-02-04-f1c43d51-8dede0ce/
recipe: https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/exp_model/2019-02-04-f1c43d51-8dede0ce/Singularity
collection: muhammadzaheer/singularity-recipes
---

# muhammadzaheer/singularity-recipes:exp_model

```bash
$ singularity pull shub://muhammadzaheer/singularity-recipes:exp_model
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

    # Installing shapely
    /usr/local/miniconda3/bin/conda install -y shapely

    git clone https://github.com/pybox2d/pybox2d
    cd pybox2d
    /usr/local/miniconda3/bin/python setup.py build
    /usr/local/miniconda3/bin/python setup.py install

    # Installing PyTorch
    /usr/local/miniconda3/bin/conda install -y pytorch-cpu torchvision-cpu -c pytorch

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
```

## Collection

 - Name: [muhammadzaheer/singularity-recipes](https://github.com/muhammadzaheer/singularity-recipes)
 - License: None

