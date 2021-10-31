---
id: 9364
name: "devriesgoe/singularity"
branch: "master"
tag: "extended"
commit: "d279c818db7ab971ecd0ac85b39d4f484abc1451"
version: "086b7f7ba2ea59b0b3554dd6ba7a8f1c"
build_date: "2019-05-28T04:27:35.878Z"
size_mb: 1064
size: 432422943
sif: "https://datasets.datalad.org/shub/devriesgoe/singularity/extended/2019-05-28-d279c818-086b7f7b/086b7f7ba2ea59b0b3554dd6ba7a8f1c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/devriesgoe/singularity/extended/2019-05-28-d279c818-086b7f7b/
recipe: https://datasets.datalad.org/shub/devriesgoe/singularity/extended/2019-05-28-d279c818-086b7f7b/Singularity
collection: devriesgoe/singularity
---

# devriesgoe/singularity:extended

```bash
$ singularity pull shub://devriesgoe/singularity:extended
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
apt-get -y install libpython3.6-dev

apt-get -y install nano
apt-get -y install vim
apt-get -y install git

pip3 install jupyter
pip3 install numpy scipy matplotlib
pip3 install ipyparallel
pip3 install dask[complete] distributed --upgrade

ipcluster nbextension enable

%environment

XDG_RUNTIME_DIR=""
PATH=${PATH}:${LSF_BINDIR}
#PYTHONPATH="${PYTHONPATH}:${HOME}/testenv/git/ProxPython:${HOME}/testenv/git/samsara/python
```

## Collection

 - Name: [devriesgoe/singularity](https://github.com/devriesgoe/singularity)
 - License: None

