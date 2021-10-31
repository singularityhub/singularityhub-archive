---
id: 7794
name: "shelvia1039/Building_Image"
branch: "master"
tag: "jupyter"
commit: "4d8df7b99687bb40f9df5f7176ea89b03844a930"
version: "1571036e01bce8e956e24e4d8254c932"
build_date: "2019-03-15T09:03:37.594Z"
size_mb: 1503
size: 575434783
sif: "https://datasets.datalad.org/shub/shelvia1039/Building_Image/jupyter/2019-03-15-4d8df7b9-1571036e/1571036e01bce8e956e24e4d8254c932.simg"
url: https://datasets.datalad.org/shub/shelvia1039/Building_Image/jupyter/2019-03-15-4d8df7b9-1571036e/
recipe: https://datasets.datalad.org/shub/shelvia1039/Building_Image/jupyter/2019-03-15-4d8df7b9-1571036e/Singularity
collection: shelvia1039/Building_Image
---

# shelvia1039/Building_Image:jupyter

```bash
$ singularity pull shub://shelvia1039/Building_Image:jupyter
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%post
    # make mount points
    mkdir /scratch /data /secure /seq
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
    pip install jupyter ipykernel scipy numpy pandas matplotlib biopython jupyterlab seaborn
    pip3 install jupyter ipykernel scipy numpy pandas matplotlib biopython jupyterlab seaborn
    
    touch /usr/bin/nvidia-smi
```

## Collection

 - Name: [shelvia1039/Building_Image](https://github.com/shelvia1039/Building_Image)
 - License: None

