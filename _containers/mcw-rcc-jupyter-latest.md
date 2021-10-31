---
id: 4720
name: "mcw-rcc/jupyter"
branch: "master"
tag: "latest"
commit: "a791a1e246b820f54084f598dfee78af3c5ca961"
version: "9d4424de52ced407a95054f64581924f"
build_date: "2021-01-27T22:30:31.668Z"
size_mb: 1474
size: 555294751
sif: "https://datasets.datalad.org/shub/mcw-rcc/jupyter/latest/2021-01-27-a791a1e2-9d4424de/9d4424de52ced407a95054f64581924f.simg"
url: https://datasets.datalad.org/shub/mcw-rcc/jupyter/latest/2021-01-27-a791a1e2-9d4424de/
recipe: https://datasets.datalad.org/shub/mcw-rcc/jupyter/latest/2021-01-27-a791a1e2-9d4424de/Singularity
collection: mcw-rcc/jupyter
---

# mcw-rcc/jupyter:latest

```bash
$ singularity pull shub://mcw-rcc/jupyter:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%help
    This container runs a Jupyter Notebook on a compute node.

%labels
    Maintainer Matthew Flister

%post
    # make mount points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts
    # install deps
    apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-dev \
        python3-pip \
        python3-setuptools \
        python \
        python-dev \
        python-pip \
        python-setuptools \
        build-essential \
        gcc-multilib
    apt-get clean
    #install python pkgs
    pip install --no-cache-dir --upgrade pip==9.0.3
    pip3 install --no-cache-dir --upgrade pip==9.0.3
    pip install jupyter ipykernel scipy numpy pandas matplotlib biopython jupyterlab
    pip3 install jupyter ipykernel scipy numpy pandas matplotlib biopython jupyterlab
```

## Collection

 - Name: [mcw-rcc/jupyter](https://github.com/mcw-rcc/jupyter)
 - License: [MIT License](https://api.github.com/licenses/mit)

