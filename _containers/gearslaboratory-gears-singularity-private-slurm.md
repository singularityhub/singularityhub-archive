---
id: 2908
name: "gearslaboratory/gears-singularity-private"
branch: "master"
tag: "slurm"
commit: "889e55f0f93bddc2398dcdbde7213846b71ea4ab"
version: "6ec98bea78ff743bb81621a33c914a90"
build_date: "2018-05-23T17:28:03.967Z"
size_mb: None
size: 601972767
sif: "https://datasets.datalad.org/shub/gearslaboratory/gears-singularity-private/slurm/2018-05-23-889e55f0-6ec98bea/6ec98bea78ff743bb81621a33c914a90.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/gearslaboratory/gears-singularity-private/slurm/2018-05-23-889e55f0-6ec98bea/
recipe: https://datasets.datalad.org/shub/gearslaboratory/gears-singularity-private/slurm/2018-05-23-889e55f0-6ec98bea/Singularity
collection: gearslaboratory/gears-singularity-private
---

# gearslaboratory/gears-singularity-private:slurm

```bash
$ singularity pull shub://gearslaboratory/gears-singularity-private:slurm
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: bash

### GEARS Lab SLURM submitter for Pronghorn.  

%post
  locale-gen en_US.UTF-8
  sed -i 's/main/main restricted universe/g' /etc/apt/sources.list
  echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a /etc/apt/sources.list
  gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
  gpg -a --export E084DAB9 | apt-key add -
  apt-get update

  # Install R, openmpi, misc. utilities:
  apt-get install -y libopenblas-dev r-base-core r-base-dev libcurl4-openssl-dev libopenmpi-dev openmpi-bin openmpi-common openmpi-doc openssh-client openssh-server libssh-dev wget vim git nano git cmake gfortran g++ curl wget python autoconf bzip2 libtool libtool-bin libxml2-dev 

  alias squeue="ssh $USER@$HOSTNAME squeue"
```

## Collection

 - Name: [gearslaboratory/gears-singularity-private](https://github.com/gearslaboratory/gears-singularity-private)
 - License: None

