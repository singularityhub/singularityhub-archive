---
id: 3506
name: "ddnguyen2/Centos7"
branch: "master"
tag: "latest"
commit: "b70467b2344d71fab1d19332b3ebdc420541b3bc"
version: "7944ade9b99fef4f89ddef740dba8af6"
build_date: "2018-07-12T08:20:47.651Z"
size_mb: 473
size: 156885023
sif: "https://datasets.datalad.org/shub/ddnguyen2/Centos7/latest/2018-07-12-b70467b2-7944ade9/7944ade9b99fef4f89ddef740dba8af6.simg"
url: https://datasets.datalad.org/shub/ddnguyen2/Centos7/latest/2018-07-12-b70467b2-7944ade9/
recipe: https://datasets.datalad.org/shub/ddnguyen2/Centos7/latest/2018-07-12-b70467b2-7944ade9/Singularity
collection: ddnguyen2/Centos7
---

# ddnguyen2/Centos7:latest

```bash
$ singularity pull shub://ddnguyen2/Centos7:latest
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
yum -y install libXrender-devel
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

 - Name: [ddnguyen2/Centos7](https://github.com/ddnguyen2/Centos7)
 - License: None

