---
id: 7108
name: "devriesgoe/singularity-test"
branch: "master"
tag: "latest"
commit: "4254e602bdf74c8dbba2764db0e4c1031dc39236"
version: "39655cbef4f8cb06a5bcf04cdeaa37e4"
build_date: "2019-05-21T17:53:19.125Z"
size_mb: 993
size: 406433823
sif: "https://datasets.datalad.org/shub/devriesgoe/singularity-test/latest/2019-05-21-4254e602-39655cbe/39655cbef4f8cb06a5bcf04cdeaa37e4.simg"
url: https://datasets.datalad.org/shub/devriesgoe/singularity-test/latest/2019-05-21-4254e602-39655cbe/
recipe: https://datasets.datalad.org/shub/devriesgoe/singularity-test/latest/2019-05-21-4254e602-39655cbe/Singularity
collection: devriesgoe/singularity-test
---

# devriesgoe/singularity-test:latest

```bash
$ singularity pull shub://devriesgoe/singularity-test:latest
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
PYTHONPATH="${PYTHONPATH}:${HOME}/testenv/git/ProxPython:${HOME}/testenv/git/samsara/python"
PATH=${PATH}:/opt/slurm/bin
MANPATH=$MANPATH:/opt/slurm/share/man
```

## Collection

 - Name: [devriesgoe/singularity-test](https://github.com/devriesgoe/singularity-test)
 - License: None

