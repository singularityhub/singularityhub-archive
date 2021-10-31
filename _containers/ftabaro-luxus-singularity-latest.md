---
id: 12847
name: "ftabaro/luxus-singularity"
branch: "master"
tag: "latest"
commit: "7b5a4d2083bdc81f6f6e91e6e78b66fdeb0230a0"
version: "7b6b27f6402091f6d5e868cd26702d91"
build_date: "2020-05-04T10:40:09.461Z"
size_mb: 2055.0
size: 517443615
sif: "https://datasets.datalad.org/shub/ftabaro/luxus-singularity/latest/2020-05-04-7b5a4d20-7b6b27f6/7b6b27f6402091f6d5e868cd26702d91.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ftabaro/luxus-singularity/latest/2020-05-04-7b5a4d20-7b6b27f6/
recipe: https://datasets.datalad.org/shub/ftabaro/luxus-singularity/latest/2020-05-04-7b5a4d20-7b6b27f6/Singularity
collection: ftabaro/luxus-singularity
---

# ftabaro/luxus-singularity:latest

```bash
$ singularity pull shub://ftabaro/luxus-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

%help
  This is a LuxUS container based on CentOS 7. 

  Documentation: https://github.com/hallav/LuxUS

  Usage:
    singularity run --app prepare luxus.sif [options]  # run prepare_data_for_luxus.py 
    singularity run --app luxus luxus.sif [options]    # run run_luxus.py

%labels
  Author francesco.tabaro@tuni.fi
  Version 0.1

%post
  umask 002 && \
  PACKAGES=/packages && \
  mkdir $PACKAGES && \
  cd $PACKAGES && \
  yum makecache && \
  yum groupinstall -y 'Development Tools' && \
  yum install -y epel-release && \
  yum install -y python-devel python-pip && \
  pip install numpy==1.14.5 scipy==1.1.0 kiwisolver==1.1.0 matplotlib==2.2.2 pystan==2.17.1.0 && \
  curl -LO https://github.com/stan-dev/cmdstan/releases/download/v2.12.0/cmdstan-2.12.0.tar.gz && \
  tar xf cmdstan-2.12.0.tar.gz && \
  rm cmdstan-2.12.0.tar.gz && \
  cd cmdstan-2.12.0 && \
  make build && \
  git clone https://github.com/hallav/LuxUS.git $PACKAGES/luxus

%environment
  export PACKAGES=/packages
  export PATH="$PATH:$PACKAGES/cmdstan-2.12.0/bin"
  export PYTHONPATH=$PACKAGES/luxus/scripts

#########
## APPS 
#########

%apprun luxus
  exec python $PACKAGES/luxus/scripts/run_luxus.py $@

%apprun prepare
  exec python $PACKAGES/luxus/scripts/prepare_data_for_luxus.py $@
```

## Collection

 - Name: [ftabaro/luxus-singularity](https://github.com/ftabaro/luxus-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

