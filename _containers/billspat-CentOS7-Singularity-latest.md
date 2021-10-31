---
id: 892
name: "billspat/CentOS7-Singularity"
branch: "testing"
tag: "latest"
commit: "9e331689e2d69a6a9c1bf8a9f569af019452a8f0"
version: "9bec187dfd5e0790b424ca4f6eec1c57"
build_date: "2017-11-21T18:32:11.777Z"
size_mb: 1168
size: 479764511
sif: "https://datasets.datalad.org/shub/billspat/CentOS7-Singularity/latest/2017-11-21-9e331689-9bec187d/9bec187dfd5e0790b424ca4f6eec1c57.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/billspat/CentOS7-Singularity/latest/2017-11-21-9e331689-9bec187d/
recipe: https://datasets.datalad.org/shub/billspat/CentOS7-Singularity/latest/2017-11-21-9e331689-9bec187d/Singularity
collection: billspat/CentOS7-Singularity
---

# billspat/CentOS7-Singularity:latest

```bash
$ singularity pull shub://billspat/CentOS7-Singularity:latest
```

## Singularity Recipe

```singularity
################################################################################
# DRAFT CentOS 7 based Singularity container for MSU ICER Analytics
################################################################################

BootStrap: docker
From: centos:latest
 
################################################################################
# Copy any necessary files into the container
# These are simple scripts that set prompt
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
# Python3 : Install PIP from EPEL and upgrade it to the latest version
################################################################################
yum -y install epel-release
yum -y install python34-pip python-pip
pip  install --upgrade pip
pip3 install --upgrade pip
pip  install --upgrade virtualenv

################################################################################
# R : (latest) 
################################################################################
yum -y install R

################################################################################
# Create directories to enable access to common MSU HPCC mount points
################################################################################
mkdir /boot
mkdir /cvmfs
mkdir -p /mnt/home
mkdir -p /mnt/research
# mkdir -p /mnt/dfs17
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

 - Name: [billspat/CentOS7-Singularity](https://github.com/billspat/CentOS7-Singularity)
 - License: None

