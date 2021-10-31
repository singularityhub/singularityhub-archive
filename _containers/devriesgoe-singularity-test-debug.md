---
id: 9199
name: "devriesgoe/singularity-test"
branch: "master"
tag: "debug"
commit: "01c9a47776937066020ff2fecf92efe7aee7c152"
version: "bb21868f9cc663caa93d9484db97717d"
build_date: "2019-05-21T17:53:19.142Z"
size_mb: 1029
size: 421724191
sif: "https://datasets.datalad.org/shub/devriesgoe/singularity-test/debug/2019-05-21-01c9a477-bb21868f/bb21868f9cc663caa93d9484db97717d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/devriesgoe/singularity-test/debug/2019-05-21-01c9a477-bb21868f/
recipe: https://datasets.datalad.org/shub/devriesgoe/singularity-test/debug/2019-05-21-01c9a477-bb21868f/Singularity
collection: devriesgoe/singularity-test
---

# devriesgoe/singularity-test:debug

```bash
$ singularity pull shub://devriesgoe/singularity-test:debug
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
apt-get -y install git

pip3 install jupyter
pip3 install numpy scipy matplotlib
pip3 install ipyparallel
pip3 install dask[complete] distributed --upgrade

ipcluster nbextension enable

%environment

PYTHONPATH="${PYTHONPATH}:${HOME}/testenv/git/ProxPython:${HOME}/testenv/git/samsara/python"
```

## Collection

 - Name: [devriesgoe/singularity-test](https://github.com/devriesgoe/singularity-test)
 - License: None

