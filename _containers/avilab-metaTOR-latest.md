---
id: 6477
name: "avilab/metaTOR"
branch: "master"
tag: "latest"
commit: "3db1b6766166685aad0aaac5b8eb58628d773a0a"
version: "1944d3820e12df60193b953f2259bd53"
build_date: "2019-01-24T13:55:00.989Z"
size_mb: 1124
size: 426565663
sif: "https://datasets.datalad.org/shub/avilab/metaTOR/latest/2019-01-24-3db1b676-1944d382/1944d3820e12df60193b953f2259bd53.simg"
url: https://datasets.datalad.org/shub/avilab/metaTOR/latest/2019-01-24-3db1b676-1944d382/
recipe: https://datasets.datalad.org/shub/avilab/metaTOR/latest/2019-01-24-3db1b676-1944d382/Singularity
collection: avilab/metaTOR
---

# avilab/metaTOR:latest

```bash
$ singularity pull shub://avilab/metaTOR:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
  Maintainer tpall

%post
  # Get dependencies
  apt-get update
  apt-get install -y --no-install-recommends \
  git \
  python \
  python-pip \
  python3-setuptools \
  python3 \
  python3-dev \
  python3-pip \
  python3-virtualenv \
  bowtie2 \
  samtools \
  hmmer \
  prodigal \
  libfreetype6-dev \
  libpng-dev \
  pkg-config \
  wget \
  pigz
  
  mkdir -p /tools
  cd /tools
  
  # Fetching louvain
  mkdir -p /tools/louvain
  wget -q https://lip6.github.io/Louvain-BinaryBuild/louvain_linux.tar.gz -O /tools/louvain/louvain.tar.gz
  cd /tools/louvain
  tar -xzf louvain.tar.gz
  chmod +x /tools/louvain/*
  rm -f /tools/louvain/louvain.tar.gz
  
  # Fetching HMMs
  mkdir -p /HMM_databases
  cd /HMM_databases
  wget -q http://dl.pasteur.fr/fop/LItxiFe9/hmm_databases.tgz
  tar -xzf /HMM_databases/hmm_databases.tgz
  rm -f /HMM_databases/hmm_databases.tar.gz
  cd /
  
  # Add tools to path during runtime
  echo 'export PATH=$PATH:/tools:/tools/louvain:/HMM_databases' >>$SINGULARITY_ENVIRONMENT
  
  # Install metator and requests
  pip3 install requests metator

  # Clean up
  rm -rf /var/lib/apt/lists/*

%runscript
  exec metator "$@"
```

## Collection

 - Name: [avilab/metaTOR](https://github.com/avilab/metaTOR)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

