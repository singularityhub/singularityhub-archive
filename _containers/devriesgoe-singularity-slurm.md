---
id: 9363
name: "devriesgoe/singularity"
branch: "master"
tag: "slurm"
commit: "04d2d109df33a88f0d3077ff30eeb6f0d44a2269"
version: "62d7e7491c02282a4ba416c261ab1d9f"
build_date: "2019-05-28T04:27:35.867Z"
size_mb: 1064
size: 432422943
sif: "https://datasets.datalad.org/shub/devriesgoe/singularity/slurm/2019-05-28-04d2d109-62d7e749/62d7e7491c02282a4ba416c261ab1d9f.simg"
url: https://datasets.datalad.org/shub/devriesgoe/singularity/slurm/2019-05-28-04d2d109-62d7e749/
recipe: https://datasets.datalad.org/shub/devriesgoe/singularity/slurm/2019-05-28-04d2d109-62d7e749/Singularity
collection: devriesgoe/singularity
---

# devriesgoe/singularity:slurm

```bash
$ singularity pull shub://devriesgoe/singularity:slurm
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

PYTHONPATH=${PYTHONPATH}:${HOME}/testenv/git/ProxPython:${HOME}/testenv/git/samsara/python
PATH=${PATH}:/opt/slurm/bin
MANPATH=$MANPATH:/opt/slurm/share/man
SINGULARITY_BINDPATH=/opt,/var/run/munge,/run/munge,/usr/lib64/libmunge.so.2,/usr/lib64/libmunge.so.2.0.0,/etc/profile.d/slurm.sh
echo "slurmadmin:x:300:300::/opt/slurm/slurm:/bin/false" >> /etc/passwd
echo "slurmadmin:x:300:" >> /etc/group
```

## Collection

 - Name: [devriesgoe/singularity](https://github.com/devriesgoe/singularity)
 - License: None

