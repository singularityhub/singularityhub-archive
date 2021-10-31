---
id: 2986
name: "RyanAshbaugh/ubuntu-leaves-17.04"
branch: "master"
tag: "latest"
commit: "93596f36fa9ed58169aefff8af3c277094a46bb3"
version: "e2e644b391a8dfcece0bc266824a0b9c"
build_date: "2021-03-31T13:30:26.670Z"
size_mb: 95
size: 37011487
sif: "https://datasets.datalad.org/shub/RyanAshbaugh/ubuntu-leaves-17.04/latest/2021-03-31-93596f36-e2e644b3/e2e644b391a8dfcece0bc266824a0b9c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/RyanAshbaugh/ubuntu-leaves-17.04/latest/2021-03-31-93596f36-e2e644b3/
recipe: https://datasets.datalad.org/shub/RyanAshbaugh/ubuntu-leaves-17.04/latest/2021-03-31-93596f36-e2e644b3/Singularity
collection: RyanAshbaugh/ubuntu-leaves-17.04
---

# RyanAshbaugh/ubuntu-leaves-17.04:latest

```bash
$ singularity pull shub://RyanAshbaugh/ubuntu-leaves-17.04:latest
```

## Singularity Recipe

```singularity
################################################################################
# Basic bootstrap definition to build CentOS 7 container from Docker container
################################################################################

BootStrap: docker
From: ubuntu:16.04
 
################################################################################
# Copy any necessary files into the container
################################################################################
%files
#./etc/profile.d/z_container_prompt.sh  /etc/profile.d/z_container_prompt.sh
#./etc/profile.d/z_container_prompt.csh /etc/profile.d/z_container_prompt.csh
 
%post
################################################################################
# Make sure the umask is 0022
################################################################################
umask 0022

################################################################################
# Install additional login shells for users that need them
################################################################################
# yum -y install tcsh ksh zsh

################################################################################
# Install additional packages
################################################################################
# apt-get install vim
# apt-get install git

################################################################################
# Install torch and torch dependencies
################################################################################
# git clone https://github.com/torch/distro.git ~/torch --recursive
# cd ~/torch
# bash -y install-deps
# cd
# git clone https://github.com/deepmind/torch-hdf5
# sudo apt-get install libhdf5-serial-dev hdf5-tools
# luarocks make hdf5-0-0.rockspec LIBHDF5_LIBDIR="/usr/lib/x86_64-linux-gnu/"
# luarocks install qtlua

################################################################################
# Install PIP from EPEL and upgrade it to the latest version
################################################################################
# sudo apt-get -y install epel-release
# sudo apt-get -y install python3-pip python-pip
# sudo apt-get -y install python3-tk
# pip  install --upgrade pip
# pip3 install --upgrade pip
# pip  install --upgrade virtualenv

################################################################################
# Create directories to enable access to common HPCC mount points
################################################################################
# mkdir /boot
# mkdir /cvmfs
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

 - Name: [RyanAshbaugh/ubuntu-leaves-17.04](https://github.com/RyanAshbaugh/ubuntu-leaves-17.04)
 - License: None

