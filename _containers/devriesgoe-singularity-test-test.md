---
id: 7110
name: "devriesgoe/singularity-test"
branch: "master"
tag: "test"
commit: "cded2a708a48d4bcfe106848ba7da49f532fadbb"
version: "69fa0e6bded5c7596d7c168b84f3e440"
build_date: "2019-05-21T17:53:19.136Z"
size_mb: 1066
size: 433090591
sif: "https://datasets.datalad.org/shub/devriesgoe/singularity-test/test/2019-05-21-cded2a70-69fa0e6b/69fa0e6bded5c7596d7c168b84f3e440.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/devriesgoe/singularity-test/test/2019-05-21-cded2a70-69fa0e6b/
recipe: https://datasets.datalad.org/shub/devriesgoe/singularity-test/test/2019-05-21-cded2a70-69fa0e6b/Singularity
collection: devriesgoe/singularity-test
---

# devriesgoe/singularity-test:test

```bash
$ singularity pull shub://devriesgoe/singularity-test:test
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
pip3 install pandas seaborn

ipcluster nbextension enable

%environment

XDG_RUNTIME_DIR=""
PYTHONPATH="${PYTHONPATH}:${HOME}/testenv/git/ProxPython:${HOME}/testenv/git/samsara/python"
PATH="${PATH}:/opt/slurm/bin"
MANPATH="${MANPATH}:/opt/slurm/share/man"
```

## Collection

 - Name: [devriesgoe/singularity-test](https://github.com/devriesgoe/singularity-test)
 - License: None

