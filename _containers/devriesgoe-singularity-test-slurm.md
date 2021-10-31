---
id: 8792
name: "devriesgoe/singularity-test"
branch: "master"
tag: "slurm"
commit: "fc146b8d06fb15017e8a1ba8c6407d0837bc7a85"
version: "a28cefcf1eefc3256e3981e351f4b403"
build_date: "2019-05-28T04:27:34.482Z"
size_mb: 1064
size: 432422943
sif: "https://datasets.datalad.org/shub/devriesgoe/singularity-test/slurm/2019-05-28-fc146b8d-a28cefcf/a28cefcf1eefc3256e3981e351f4b403.simg"
url: https://datasets.datalad.org/shub/devriesgoe/singularity-test/slurm/2019-05-28-fc146b8d-a28cefcf/
recipe: https://datasets.datalad.org/shub/devriesgoe/singularity-test/slurm/2019-05-28-fc146b8d-a28cefcf/Singularity
collection: devriesgoe/singularity-test
---

# devriesgoe/singularity-test:slurm

```bash
$ singularity pull shub://devriesgoe/singularity-test:slurm
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

#export SINGULARITY_BINDPATH="/opt,/var/run/munge,/run/munge,/usr/lib64/libmunge.so.2,/usr/lib64/libmunge.so.2.0.0,/etc/profile.d/slurm.sh"

#echo 'slurmadmin:x:300:300::/opt/slurm/slurm:/bin/false' >> /etc/passwd
#echo 'slurmadmin:x:300:' >> /etc/group

%environment

XDG_RUNTIME_DIR=""
PYTHONPATH=${PYTHONPATH}:${HOME}/testenv/git/ProxPython:${HOME}/testenv/git/samsara/python
PATH=${PATH}:/opt/slurm/bin
MANPATH=$MANPATH:/opt/slurm/share/man
SINGULARITY_BINDPATH=/opt,/var/run/munge,/run/munge,/usr/lib64/libmunge.so.2,/usr/lib64/libmunge.so.2.0.0,/etc/profile.d/slurm.sh
echo "slurmadmin:x:300:300::/opt/slurm/slurm:/bin/false" >> /etc/passwd
echo "slurmadmin:x:300:" >> /etc/group
```

## Collection

 - Name: [devriesgoe/singularity-test](https://github.com/devriesgoe/singularity-test)
 - License: None

