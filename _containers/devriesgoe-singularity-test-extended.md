---
id: 8791
name: "devriesgoe/singularity-test"
branch: "master"
tag: "extended"
commit: "d279c818db7ab971ecd0ac85b39d4f484abc1451"
version: "2c6d455155c06f5aa565b3be69bb72b2"
build_date: "2019-05-02T19:59:06.661Z"
size_mb: 1061
size: 422404127
sif: "https://datasets.datalad.org/shub/devriesgoe/singularity-test/extended/2019-05-02-d279c818-2c6d4551/2c6d455155c06f5aa565b3be69bb72b2.simg"
url: https://datasets.datalad.org/shub/devriesgoe/singularity-test/extended/2019-05-02-d279c818-2c6d4551/
recipe: https://datasets.datalad.org/shub/devriesgoe/singularity-test/extended/2019-05-02-d279c818-2c6d4551/Singularity
collection: devriesgoe/singularity-test
---

# devriesgoe/singularity-test:extended

```bash
$ singularity pull shub://devriesgoe/singularity-test:extended
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

 - Name: [devriesgoe/singularity-test](https://github.com/devriesgoe/singularity-test)
 - License: None

