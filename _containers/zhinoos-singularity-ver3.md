---
id: 13064
name: "zhinoos/singularity"
branch: "master"
tag: "ver3"
commit: "165fe982ff8efd4ecd6d4bdb24159a88399fdbd1"
version: "d2686c587930c04e592d3e82083233e9c4bed3b3f891f089817a97649b184655"
build_date: "2020-05-19T12:11:49.578Z"
size_mb: 2062.6875
size: 2162884608
sif: "https://datasets.datalad.org/shub/zhinoos/singularity/ver3/2020-05-19-165fe982-d2686c58/d2686c587930c04e592d3e82083233e9c4bed3b3f891f089817a97649b184655.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/zhinoos/singularity/ver3/2020-05-19-165fe982-d2686c58/
recipe: https://datasets.datalad.org/shub/zhinoos/singularity/ver3/2020-05-19-165fe982-d2686c58/Singularity
collection: zhinoos/singularity
---

# zhinoos/singularity:ver3

```bash
$ singularity pull shub://zhinoos/singularity:ver3
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

%post
    # Downloads the latest package lists (important).
    apt-get update -y
    # Runs apt-get while ensuring that there are no user prompts that would
    # cause the build process to hang.
    # python3-tk is required by matplotlib.
    # python3-dev is needed to require some packages.
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        python3 \
        python3-tk \
        python3-pip \
        python3-distutils\
        python3-dev
    # Reduce the size of the image by deleting the package lists we downloaded,
    # which are useless now.
    rm -rf /var/lib/apt/lists/*
    # Install Pipenv.
    pip3 install setuptools
    pip3 install pipenv

%environment
    # Pipenv requires a certain terminal encoding.
    export LANG=C.UTF-8
    export LC_ALL=C.UTF-8
    # This configures Pipenv to store the packages in the current working
    # directory.
    export PIPENV_VENV_IN_PROJECT=1
```

## Collection

 - Name: [zhinoos/singularity](https://github.com/zhinoos/singularity)
 - License: None

