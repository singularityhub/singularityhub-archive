---
id: 9717
name: "qlan3/singularity-deffile"
branch: "master"
tag: "explorer"
commit: "702d7ea2c45934041137f7216ee710055d8cefa6"
version: "641154ec2dbd6f7d41ed3c44f2c491f7d72bf08035f8314bff8291908432444f"
build_date: "2019-08-04T16:49:57.177Z"
size_mb: 1955.71484375
size: 2050715648
sif: "https://datasets.datalad.org/shub/qlan3/singularity-deffile/explorer/2019-08-04-702d7ea2-641154ec/641154ec2dbd6f7d41ed3c44f2c491f7d72bf08035f8314bff8291908432444f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/qlan3/singularity-deffile/explorer/2019-08-04-702d7ea2-641154ec/
recipe: https://datasets.datalad.org/shub/qlan3/singularity-deffile/explorer/2019-08-04-702d7ea2-641154ec/Singularity
collection: qlan3/singularity-deffile
---

# qlan3/singularity-deffile:explorer

```bash
$ singularity pull shub://qlan3/singularity-deffile:explorer
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
    
    # Install gym dependency
    apt-get -y install python-pyglet python3-opengl zlib1g-dev libjpeg-dev patchelf \
    cmake swig libboost-all-dev libsdl2-dev libosmesa6-dev xvfb ffmpeg

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

    # Install seaborn pyarrow tqdm pandas psutil opencv-python
    /usr/local/miniconda3/bin/conda install -y -c conda-forge matplotlib
    /usr/local/miniconda3/bin/conda install -y seaborn
    /usr/local/miniconda3/bin/pip install pyarrow
    /usr/local/miniconda3/bin/conda install -y tqdm
    /usr/local/miniconda3/bin/conda install -y pandas
    /usr/local/miniconda3/bin/conda install -y -c anaconda psutil
    /usr/local/miniconda3/bin/pip install opencv-python

    # Install Gym
    /usr/local/miniconda3/bin/pip install 'gym[classic_control, box2d, atari]'

    # Install PLE
    /usr/local/miniconda3/bin/pip install git+https://github.com/ntasfi/PyGame-Learning-Environment.git

    # Install PyGame
    apt-get -y install python-pygame
    /usr/local/miniconda3/bin/pip install pygame

    # Install MinAtar
    /usr/local/miniconda3/bin/pip install git+https://github.com/kenjyoung/MinAtar.git

    # Install Gym Games
    /usr/local/miniconda3/bin/pip install git+https://github.com/qlan3/gym-games.git
```

## Collection

 - Name: [qlan3/singularity-deffile](https://github.com/qlan3/singularity-deffile)
 - License: [MIT License](https://api.github.com/licenses/mit)

