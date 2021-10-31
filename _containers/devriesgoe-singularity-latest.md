---
id: 9366
name: "devriesgoe/singularity"
branch: "master"
tag: "latest"
commit: "5c17fdeaae1d0f7ad2f083fe02cf8e71f6342fd0"
version: "5190f921f9e2b254535343ddd913166d"
build_date: "2019-05-28T04:27:35.873Z"
size_mb: 993
size: 406462495
sif: "https://datasets.datalad.org/shub/devriesgoe/singularity/latest/2019-05-28-5c17fdea-5190f921/5190f921f9e2b254535343ddd913166d.simg"
url: https://datasets.datalad.org/shub/devriesgoe/singularity/latest/2019-05-28-5c17fdea-5190f921/
recipe: https://datasets.datalad.org/shub/devriesgoe/singularity/latest/2019-05-28-5c17fdea-5190f921/Singularity
collection: devriesgoe/singularity
---

# devriesgoe/singularity:latest

```bash
$ singularity pull shub://devriesgoe/singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%help

Test container for dask environment using ipyparallel


%post

apt-get -y update
apt-get -y install python3-pip net-tools
apt-get -y install graphviz libgraphviz-dev

pip3 install jupyter
pip3 install numpy scipy matplotlib
pip3 install ipyparallel
pip3 install dask[complete] distributed --upgrade

ipcluster nbextension enable

%environment

XDG_RUNTIME_DIR=""
PATH=${PATH}:${LSF_BINDIR}
```

## Collection

 - Name: [devriesgoe/singularity](https://github.com/devriesgoe/singularity)
 - License: None

