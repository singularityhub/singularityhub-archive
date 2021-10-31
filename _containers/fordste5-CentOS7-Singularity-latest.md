---
id: 454
name: "fordste5/CentOS7-Singularity"
branch: "master"
tag: "latest"
commit: "097716ca34b22d56c92199ad8346ead2feea8982"
version: "2b1570ac832e335e9e90557766e8917d"
build_date: "2020-03-22T17:30:35.390Z"
size_mb: 460
size: 147378207
sif: "https://datasets.datalad.org/shub/fordste5/CentOS7-Singularity/latest/2020-03-22-097716ca-2b1570ac/2b1570ac832e335e9e90557766e8917d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/fordste5/CentOS7-Singularity/latest/2020-03-22-097716ca-2b1570ac/
recipe: https://datasets.datalad.org/shub/fordste5/CentOS7-Singularity/latest/2020-03-22-097716ca-2b1570ac/Singularity
collection: fordste5/CentOS7-Singularity
---

# fordste5/CentOS7-Singularity:latest

```bash
$ singularity pull shub://fordste5/CentOS7-Singularity:latest
```

## Singularity Recipe

```singularity
################################################################################
# Basic bootstrap definition to build CentOS 7 container from Docker container
################################################################################

BootStrap: docker
From: centos:latest
 
################################################################################
# Copy any necessary files into the container
################################################################################
%files
./etc/profile.d/z_container_prompt.sh  /etc/profile.d/z_container_prompt.sh
./etc/profile.d/z_container_prompt.csh /etc/profile.d/z_container_prompt.csh
 
%post
################################################################################
# Make sure the umask is 0022
################################################################################
umask 0022

################################################################################
# Install additional login shells for users that need them
################################################################################
yum -y install tcsh ksh zsh

################################################################################
# Install additional packages
################################################################################
yum -y install vim

################################################################################
# Install PIP from EPEL and upgrade it to the latest version
################################################################################
yum -y install epel-release
yum -y install python34-pip python-pip
pip  install --upgrade pip
pip3 install --upgrade pip
pip  install --upgrade virtualenv

################################################################################
# Create directories to enable access to common HPCC mount points
################################################################################
mkdir /boot
mkdir /cvmfs
mkdir -p /mnt/home
mkdir -p /mnt/research
mkdir -p /mnt/dfs17
mkdir -p /mnt/ffs17
mkdir -p /mnt/local
mkdir -p /mnt/ls15
mkdir -p /opt/software

################################################################################
# Run the user's login shell, or a user specified command
################################################################################
%runscript
SHELL="$(getent passwd $USER | awk -F: '{print $NF}')"
SHELL=${SHELL:-/bin/bash}
if [[ "$@" == "" ]]; then 
  exec env -i TERM="$TERM" HOME="$HOME" $SHELL -l
else
  exec env -i TERM="$TERM" HOME="$HOME" $@
fi
```

## Collection

 - Name: [fordste5/CentOS7-Singularity](https://github.com/fordste5/CentOS7-Singularity)
 - License: None

