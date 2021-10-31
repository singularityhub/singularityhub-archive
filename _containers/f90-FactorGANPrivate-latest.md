---
id: 11345
name: "f90/FactorGANPrivate"
branch: "master"
tag: "latest"
commit: "a8856c75992c9e2d3e639a82240f1d1f3c1ad5c6"
version: "36fffa489dac94700365f34a0fa52e9c"
build_date: "2019-10-24T12:23:26.741Z"
size_mb: 6679.0
size: 4118331423
sif: "https://datasets.datalad.org/shub/f90/FactorGANPrivate/latest/2019-10-24-a8856c75-36fffa48/36fffa489dac94700365f34a0fa52e9c.sif"
url: https://datasets.datalad.org/shub/f90/FactorGANPrivate/latest/2019-10-24-a8856c75-36fffa48/
recipe: https://datasets.datalad.org/shub/f90/FactorGANPrivate/latest/2019-10-24-a8856c75-36fffa48/Singularity
collection: f90/FactorGANPrivate
---

# f90/FactorGANPrivate:latest

```bash
$ singularity pull shub://f90/FactorGANPrivate:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

%post
    # Create extra folders that JADE HPC can bind to
    # mkdir /tmp # This already exists
    mkdir /local_scratch
    mkdir /raid
    mkdir /raid/local_scratch

    # Downloads the latest package lists (important).
    apt-get update -y
    # Runs apt-get while ensuring that there are no user prompts that would
    # cause the build process to hang.
    # python3-tk is required by matplotlib.
    # python3-dev is needed to require some packages.
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        python3 \
        python3-tk \
        python3-pip \
        python3-dev \
        libsndfile1 \
        libsndfile1-dev \
        ffmpeg \
        git
    # Reduce the size of the image by deleting the package lists we downloaded,
    # which are useless now.
    rm -rf /var/lib/apt/lists/*

    # Install Pipenv.
    pip3 install pipenv

    # Install Python modules.
    pip3 install future
    pip3 install numpy
    pip3 install librosa
    pip3 install musdb
    pip3 install museval
    pip3 install h5py
    pip3 install tqdm
    pip3 install sortedcontainers
    pip3 install torch==1.3.0 torchvision==0.4.1 tensorboard
    pip3 install imageio
    pip3 install seaborn
    pip3 install pandas
    pip3 install matplotlib

%environment
    # Pipenv requires a certain terminal encoding.
    export LANG=C.UTF-8
    export LC_ALL=C.UTF-8
    # This configures Pipenv to store the packages in the current working
    # directory.
    export PIPENV_VENV_IN_PROJECT=1
```

## Collection

 - Name: [f90/FactorGANPrivate](https://github.com/f90/FactorGANPrivate)
 - License: None

