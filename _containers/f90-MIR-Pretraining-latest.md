---
id: 11980
name: "f90/MIR-Pretraining"
branch: "master"
tag: "latest"
commit: "93ff338c09e4ad16f6efe858fdd2a28d908ed666"
version: "44c9642f73b79129302ab839bc633cdf"
build_date: "2020-01-10T16:05:38.067Z"
size_mb: 6651.0
size: 4085882911
sif: "https://datasets.datalad.org/shub/f90/MIR-Pretraining/latest/2020-01-10-93ff338c-44c9642f/44c9642f73b79129302ab839bc633cdf.sif"
url: https://datasets.datalad.org/shub/f90/MIR-Pretraining/latest/2020-01-10-93ff338c-44c9642f/
recipe: https://datasets.datalad.org/shub/f90/MIR-Pretraining/latest/2020-01-10-93ff338c-44c9642f/Singularity
collection: f90/MIR-Pretraining
---

# f90/MIR-Pretraining:latest

```bash
$ singularity pull shub://f90/MIR-Pretraining:latest
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
    pip3 install future numpy librosa musdb museval h5py tqdm sortedcontainers
    pip3 install torch==1.3.0 torchvision==0.4.1 tensorboard torchaudio==0.3.2

%environment
    # Pipenv requires a certain terminal encoding.
    export LANG=C.UTF-8
    export LC_ALL=C.UTF-8
    # This configures Pipenv to store the packages in the current working
    # directory.
    export PIPENV_VENV_IN_PROJECT=1
```

## Collection

 - Name: [f90/MIR-Pretraining](https://github.com/f90/MIR-Pretraining)
 - License: None

