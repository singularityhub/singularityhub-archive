---
id: 8020
name: "muhammadzaheer/singularity-recipes"
branch: "master"
tag: "selectivedynagpu"
commit: "4672cb71be82648094b7e46fd1da0660a6c803fd"
version: "881cd19327f3216c63577aac64713802"
build_date: "2019-10-22T22:24:04.622Z"
size_mb: 6127
size: 3446775839
sif: "https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/selectivedynagpu/2019-10-22-4672cb71-881cd193/881cd19327f3216c63577aac64713802.simg"
url: https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/selectivedynagpu/2019-10-22-4672cb71-881cd193/
recipe: https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/selectivedynagpu/2019-10-22-4672cb71-881cd193/Singularity
collection: muhammadzaheer/singularity-recipes
---

# muhammadzaheer/singularity-recipes:selectivedynagpu

```bash
$ singularity pull shub://muhammadzaheer/singularity-recipes:selectivedynagpu
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
    /usr/local/miniconda3/bin/conda install -y pytorch torchvision cudatoolkit=10.0 -c pytorch

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

