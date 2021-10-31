---
id: 3509
name: "ddnguyen2/Centos7"
branch: "master"
tag: "conda"
commit: "a7429c4fec5f818795837ce74718b2aeac3682d2"
version: "e689ef440df0f66958b78344492157ba"
build_date: "2018-07-12T08:20:47.644Z"
size_mb: 4333
size: 2184863775
sif: "https://datasets.datalad.org/shub/ddnguyen2/Centos7/conda/2018-07-12-a7429c4f-e689ef44/e689ef440df0f66958b78344492157ba.simg"
url: https://datasets.datalad.org/shub/ddnguyen2/Centos7/conda/2018-07-12-a7429c4f-e689ef44/
recipe: https://datasets.datalad.org/shub/ddnguyen2/Centos7/conda/2018-07-12-a7429c4f-e689ef44/Singularity
collection: ddnguyen2/Centos7
---

# ddnguyen2/Centos7:conda

```bash
$ singularity pull shub://ddnguyen2/Centos7:conda
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
yum -y install wget
yum -y install bzip2
wget https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
bash Anaconda3-5.1.0-Linux-x86_64.sh -f -b -p /home/anaconda
export PATH="/home/anaconda/bin:$PATH"
################################################################################
# Install PIP from EPEL and upgrade it to the latest version
################################################################################
yum -y install epel-release
# yum -y install python34-pip python-pip
# pip  install --upgrade pip
# pip3 install --upgrade pip
# pip  install --upgrade virtualenv
conda update -y conda
pip install --upgrade tensorflow
pip install keras
conda update -y conda
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

