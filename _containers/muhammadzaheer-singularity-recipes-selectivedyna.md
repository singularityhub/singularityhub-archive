---
id: 7955
name: "muhammadzaheer/singularity-recipes"
branch: "master"
tag: "selectivedyna"
commit: "83eab3a03d218ec0940a371702073535f23d92ae"
version: "9a0989a7fd59fc2d18dc660babccc770"
build_date: "2019-03-26T08:08:44.249Z"
size_mb: 4119
size: 1879371807
sif: "https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/selectivedyna/2019-03-26-83eab3a0-9a0989a7/9a0989a7fd59fc2d18dc660babccc770.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/muhammadzaheer/singularity-recipes/selectivedyna/2019-03-26-83eab3a0-9a0989a7/
recipe: https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/selectivedyna/2019-03-26-83eab3a0-9a0989a7/Singularity
collection: muhammadzaheer/singularity-recipes
---

# muhammadzaheer/singularity-recipes:selectivedyna

```bash
$ singularity pull shub://muhammadzaheer/singularity-recipes:selectivedyna
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

    # Installing MinAtar
    cd /home
    git clone https://github.com/kenjyoung/MinAtar.git
    cd MinAtar
    /usr/local/miniconda3/bin/python setup.py install
```

## Collection

 - Name: [muhammadzaheer/singularity-recipes](https://github.com/muhammadzaheer/singularity-recipes)
 - License: None

