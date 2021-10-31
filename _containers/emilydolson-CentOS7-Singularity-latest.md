---
id: 429
name: "emilydolson/CentOS7-Singularity"
branch: "master"
tag: "latest"
commit: "8ac16dc0e5c1f61aecc68c8f878c4df09de055a4"
version: "f985a5c44f34f15f8bfb8f93b3ca46b4"
build_date: "2019-11-15T01:22:52.256Z"
size_mb: 461
size: 147378207
sif: "https://datasets.datalad.org/shub/emilydolson/CentOS7-Singularity/latest/2019-11-15-8ac16dc0-f985a5c4/f985a5c44f34f15f8bfb8f93b3ca46b4.simg"
url: https://datasets.datalad.org/shub/emilydolson/CentOS7-Singularity/latest/2019-11-15-8ac16dc0-f985a5c4/
recipe: https://datasets.datalad.org/shub/emilydolson/CentOS7-Singularity/latest/2019-11-15-8ac16dc0-f985a5c4/Singularity
collection: emilydolson/CentOS7-Singularity
---

# emilydolson/CentOS7-Singularity:latest

```bash
$ singularity pull shub://emilydolson/CentOS7-Singularity:latest
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

 - Name: [emilydolson/CentOS7-Singularity](https://github.com/emilydolson/CentOS7-Singularity)
 - License: None

