---
id: 11979
name: "avilab/singularity-cdhit"
branch: "master"
tag: "latest"
commit: "1908904aa35500faff5d1da470551e9bd740e7d8"
version: "d8c121e41c0daf4bb072b4e2ae9478ab"
build_date: "2021-03-13T19:52:37.693Z"
size_mb: 418.0
size: 137162783
sif: "https://datasets.datalad.org/shub/avilab/singularity-cdhit/latest/2021-03-13-1908904a-d8c121e4/d8c121e41c0daf4bb072b4e2ae9478ab.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/avilab/singularity-cdhit/latest/2021-03-13-1908904a-d8c121e4/
recipe: https://datasets.datalad.org/shub/avilab/singularity-cdhit/latest/2021-03-13-1908904a-d8c121e4/Singularity
collection: avilab/singularity-cdhit
---

# avilab/singularity-cdhit:latest

```bash
$ singularity pull shub://avilab/singularity-cdhit:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%labels
  Maintainer tpall

%post
apt-get update && apt-get -y install \
  wget \
  build-essential \
  git \
  zlib1g-dev \
  ncbi-blast+

git clone https://github.com/tpall/cdhit.git \
  && cd cdhit \
  && git checkout install/psi-cd-hit \
  && make \
  && make install \
  && cd cd-hit-auxtools \
  && make

## Clean up
apt-get clean \
  && rm -rf /var/lib/apt/lists/ 
cd / \
  && rm -rf cdhit

%environment
  export PATH=/usr/local/bin:$PATH
  export LC_ALL=C
```

## Collection

 - Name: [avilab/singularity-cdhit](https://github.com/avilab/singularity-cdhit)
 - License: [MIT License](https://api.github.com/licenses/mit)

