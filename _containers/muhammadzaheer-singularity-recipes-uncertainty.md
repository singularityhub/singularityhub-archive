---
id: 4732
name: "muhammadzaheer/singularity-recipes"
branch: "master"
tag: "uncertainty"
commit: "4ea891c9b45d67a727b47e76532b522291e5029f"
version: "20231ba177acff0244cdf41f465e8ae5"
build_date: "2018-09-28T07:34:31.779Z"
size_mb: 3509
size: 1542942751
sif: "https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/uncertainty/2018-09-28-4ea891c9-20231ba1/20231ba177acff0244cdf41f465e8ae5.simg"
url: https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/uncertainty/2018-09-28-4ea891c9-20231ba1/
recipe: https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/uncertainty/2018-09-28-4ea891c9-20231ba1/Singularity
collection: muhammadzaheer/singularity-recipes
---

# muhammadzaheer/singularity-recipes:uncertainty

```bash
$ singularity pull shub://muhammadzaheer/singularity-recipes:uncertainty
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
```

## Collection

 - Name: [muhammadzaheer/singularity-recipes](https://github.com/muhammadzaheer/singularity-recipes)
 - License: None

