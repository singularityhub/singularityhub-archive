---
id: 5570
name: "ucr-singularity/accelerator-project"
branch: "master"
tag: "latest"
commit: "c5b5427b561cc093831ca261f32e4122d0089f6f"
version: "6bc48ca625e8a6035373bf8374d38cc4"
build_date: "2018-11-17T04:47:35.434Z"
size_mb: 842
size: 299630623
sif: "https://datasets.datalad.org/shub/ucr-singularity/accelerator-project/latest/2018-11-17-c5b5427b-6bc48ca6/6bc48ca625e8a6035373bf8374d38cc4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ucr-singularity/accelerator-project/latest/2018-11-17-c5b5427b-6bc48ca6/
recipe: https://datasets.datalad.org/shub/ucr-singularity/accelerator-project/latest/2018-11-17-c5b5427b-6bc48ca6/Singularity
collection: ucr-singularity/accelerator-project
---

# ucr-singularity/accelerator-project:latest

```bash
$ singularity pull shub://ucr-singularity/accelerator-project:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%post

# Make sure packages are up to date
apt-get update

# These are NOT interactive upgrades or installs - no questions
export DEBIAN_FRONTEND=noninteractive 
apt-get -y upgrade

# Utility and support packages
apt-get install -y screen terminator tmux vim wget 
apt-get install -y aptitude build-essential cmake g++ gfortran git \
    pkg-config python-pip python-dev software-properties-common

apt-get -y install curl libcurl4-gnutls-dev
apt-get -y install libcurl3-gnutls-dev
apt-get -y install liboauth0 liboauth-dev
apt-get -y install libjsoncpp-dev

# A test
apt-get -y install vim-gnome

# Another test
```

## Collection

 - Name: [ucr-singularity/accelerator-project](https://github.com/ucr-singularity/accelerator-project)
 - License: None

