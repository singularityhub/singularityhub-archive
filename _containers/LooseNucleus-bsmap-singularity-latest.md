---
id: 5855
name: "LooseNucleus/bsmap-singularity"
branch: "master"
tag: "latest"
commit: "19bfe44a305f533fe994af60b0137b7b867defc2"
version: "db55b5c21f128d8900f367a885fc8f72"
build_date: "2019-01-03T04:17:35.561Z"
size_mb: 668
size: 279797791
sif: "https://datasets.datalad.org/shub/LooseNucleus/bsmap-singularity/latest/2019-01-03-19bfe44a-db55b5c2/db55b5c21f128d8900f367a885fc8f72.simg"
url: https://datasets.datalad.org/shub/LooseNucleus/bsmap-singularity/latest/2019-01-03-19bfe44a-db55b5c2/
recipe: https://datasets.datalad.org/shub/LooseNucleus/bsmap-singularity/latest/2019-01-03-19bfe44a-db55b5c2/Singularity
collection: LooseNucleus/bsmap-singularity
---

# LooseNucleus/bsmap-singularity:latest

```bash
$ singularity pull shub://LooseNucleus/bsmap-singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%post
 
    echo "deb http://nova.clouds.archive.ubuntu.com/ubuntu/ xenial-backports main restricted universe multiverse" | tee -a /etc/apt/sources.list
    echo "deb http://nova.clouds.archive.ubuntu.com/ubuntu/ xenial main restricted" | tee -a /etc/apt/sources.list
    echo "deb http://nova.clouds.archive.ubuntu.com/ubuntu/ xenial multiverse" | tee -a /etc/apt/sources.list
    echo "deb http://nova.clouds.archive.ubuntu.com/ubuntu/ xenial universe" | tee -a /etc/apt/sources.list
    echo "deb http://nova.clouds.archive.ubuntu.com/ubuntu/ xenial-updates main restricted" | tee -a /etc/apt/sources.list
    echo "deb http://nova.clouds.archive.ubuntu.com/ubuntu/ xenial-updates multiverse" | tee -a /etc/apt/sources.list
    echo "deb http://nova.clouds.archive.ubuntu.com/ubuntu/ xenial-updates universe" | tee -a /etc/apt/sources.list
    echo "deb http://security.ubuntu.com/ubuntu xenial-security main restricted" | tee -a /etc/apt/sources.list
    echo "deb http://security.ubuntu.com/ubuntu xenial-security multiverse" | tee -a /etc/apt/sources.list
    echo "deb http://security.ubuntu.com/ubuntu xenial-security universe" | tee -a /etc/apt/sources.list
    echo "deb-src http://nova.clouds.archive.ubuntu.com/ubuntu/ xenial-backports main restricted universe multiverse" | tee -a /etc/apt/sources.list
    echo "deb-src http://nova.clouds.archive.ubuntu.com/ubuntu/ xenial main restricted" | tee -a /etc/apt/sources.list
    echo "deb-src http://nova.clouds.archive.ubuntu.com/ubuntu/ xenial multiverse" | tee -a /etc/apt/sources.list
    echo "deb-src http://nova.clouds.archive.ubuntu.com/ubuntu/ xenial universe" | tee -a /etc/apt/sources.list
    echo "deb-src http://nova.clouds.archive.ubuntu.com/ubuntu/ xenial-updates main restricted" | tee -a /etc/apt/sources.list
    echo "deb-src http://nova.clouds.archive.ubuntu.com/ubuntu/ xenial-updates multiverse" | tee -a /etc/apt/sources.list
    echo "deb-src http://nova.clouds.archive.ubuntu.com/ubuntu/ xenial-updates universe" | tee -a /etc/apt/sources.list
    echo "deb-src http://security.ubuntu.com/ubuntu xenial-security main restricted" | tee -a /etc/apt/sources.list
    echo "deb-src http://security.ubuntu.com/ubuntu xenial-security multiverse" | tee -a /etc/apt/sources.list
    echo "deb-src http://security.ubuntu.com/ubuntu xenial-security universe" | tee -a /etc/apt/sources.list
 
    apt-get -y update
    apt-get install -y curl wget tar gzip gcc build-essential zlib1g-dev python-minimal
    wget -O bsmap-2.90.tgz http://lilab.research.bcm.edu/dldcc-web/lilab/yxi/bsmap/bsmap-2.90.tgz
    mkdir software
    tar -xvzf bsmap-2.90.tgz
    cp -R bsmap-2.90/ software/bsmap-2.90
    cd software/bsmap-2.90
    make
    make install
     
% environment 
  export PATH=/software/bsmap-2.90:$PATH
```

## Collection

 - Name: [LooseNucleus/bsmap-singularity](https://github.com/LooseNucleus/bsmap-singularity)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

