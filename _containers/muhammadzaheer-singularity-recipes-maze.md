---
id: 5022
name: "muhammadzaheer/singularity-recipes"
branch: "master"
tag: "maze"
commit: "612adcb231908cd157404f441933cf2bbfc4b4f1"
version: "b1795e3c63d2ae275e1f73b7e13fc2fd"
build_date: "2018-09-28T07:34:31.787Z"
size_mb: 3524
size: 1547792415
sif: "https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/maze/2018-09-28-612adcb2-b1795e3c/b1795e3c63d2ae275e1f73b7e13fc2fd.simg"
url: https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/maze/2018-09-28-612adcb2-b1795e3c/
recipe: https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/maze/2018-09-28-612adcb2-b1795e3c/Singularity
collection: muhammadzaheer/singularity-recipes
---

# muhammadzaheer/singularity-recipes:maze

```bash
$ singularity pull shub://muhammadzaheer/singularity-recipes:maze
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: singularityhub/ubuntu:latest

%environment
    export PATH="/usr/local/miniconda3/bin:$PATH"

%post
    apt-get -y update
    apt-get -y install wget bzip2 parallel

    # Installing miniconda
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /usr/local/miniconda3
    rm Miniconda3-latest-Linux-x86_64.sh

    # Installing tensorflow
    /usr/local/miniconda3/bin/conda install -y -c conda-forge tensorflow
    
    # Installing tensorboardX
    /usr/local/miniconda3/bin/pip install tensorboardX
    
    # Installing PyTorch 
    /usr/local/miniconda3/bin/conda install -y pytorch-cpu torchvision-cpu -c pytorch

    # Installing Seaborn
    /usr/local/miniconda3/bin/conda install -y -c conda-forge matplotlib
    /usr/local/miniconda3/bin/conda install -y seaborn
    
    # Installing shapely
    /usr/local/miniconda3/bin/conda install -y shapely
```

## Collection

 - Name: [muhammadzaheer/singularity-recipes](https://github.com/muhammadzaheer/singularity-recipes)
 - License: None

