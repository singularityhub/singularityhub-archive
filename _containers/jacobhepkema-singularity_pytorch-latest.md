---
id: 13555
name: "jacobhepkema/singularity_pytorch"
branch: "master"
tag: "latest"
commit: "d1b3cbdff59f6088bd227dbda0bebebe34d3120d"
version: "881aec7fc18867367eaf6c2cefb77d7d"
build_date: "2020-07-09T08:23:52.235Z"
size_mb: 7785.0
size: 4557815839
sif: "https://datasets.datalad.org/shub/jacobhepkema/singularity_pytorch/latest/2020-07-09-d1b3cbdf-881aec7f/881aec7fc18867367eaf6c2cefb77d7d.sif"
url: https://datasets.datalad.org/shub/jacobhepkema/singularity_pytorch/latest/2020-07-09-d1b3cbdf-881aec7f/
recipe: https://datasets.datalad.org/shub/jacobhepkema/singularity_pytorch/latest/2020-07-09-d1b3cbdf-881aec7f/Singularity
collection: jacobhepkema/singularity_pytorch
---

# jacobhepkema/singularity_pytorch:latest

```bash
$ singularity pull shub://jacobhepkema/singularity_pytorch:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.0-devel

# Inspired by https://github.com/natbutter/pytorch-singularity

# This file contains the dependencies
%files
  environment.yml
  
%labels
  Inspired by natbutter/pytorch-singularity
  Maintained by jacobhepkema

%post
  mkdir /project /scratch

  #Now install everything
  apt update && apt install -y apt-utils curl 

  curl -LO http://repo.continuum.io/miniconda/Miniconda3-4.5.12-Linux-x86_64.sh
  bash Miniconda3-4.5.12-Linux-x86_64.sh -p /miniconda -b
  rm Miniconda3-4.5.12-Linux-x86_64.sh
  PATH=/miniconda/bin:${PATH}
  
  apt-get install -y --no-install-recommends build-essential make zlib1g procps
  
  /miniconda/bin/conda update -y conda
  
  ENV_NAME=$(head -1 environment.yml | cut -d' ' -f2)
  echo ". /miniconda/etc/profile.d/conda.sh" >> $SINGULARITY_ENVIRONMENT
  echo "/miniconda/bin/conda activate $ENV_NAME" >> $SINGULARITY_ENVIRONMENT
  
  . /miniconda/etc/profile.d/conda.sh
  # create environment

  /miniconda/bin/conda config --set ssl_verify no
  /miniconda/bin/conda env create -f environment.yml -p /miniconda/envs/$ENV_NAME
  
  . /miniconda/etc/profile.d/conda.sh

%environment
  export PATH=/miniconda/bin:${PATH}

%runscript
  exec /miniconda/envs/$(head -n 1 environment.yml | cut -f 2 -d ' ')/bin/"$@"
```

## Collection

 - Name: [jacobhepkema/singularity_pytorch](https://github.com/jacobhepkema/singularity_pytorch)
 - License: None

