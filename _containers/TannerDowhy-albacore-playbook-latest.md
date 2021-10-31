---
id: 4200
name: "TannerDowhy/albacore-playbook"
branch: "master"
tag: "latest"
commit: "8f36fce131d2dc66de7bcc95b68ad6584c39741f"
version: "52bf986d2dd6d8d7fddd485a31e35deb"
build_date: "2018-08-28T03:21:34.930Z"
size_mb: 1076
size: 451244063
sif: "https://datasets.datalad.org/shub/TannerDowhy/albacore-playbook/latest/2018-08-28-8f36fce1-52bf986d/52bf986d2dd6d8d7fddd485a31e35deb.simg"
url: https://datasets.datalad.org/shub/TannerDowhy/albacore-playbook/latest/2018-08-28-8f36fce1-52bf986d/
recipe: https://datasets.datalad.org/shub/TannerDowhy/albacore-playbook/latest/2018-08-28-8f36fce1-52bf986d/Singularity
collection: TannerDowhy/albacore-playbook
---

# TannerDowhy/albacore-playbook:latest

```bash
$ singularity pull shub://TannerDowhy/albacore-playbook:latest
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

    apt-get -y install wget apt-transport-https python3 libboost-dev python3-pip python3-numpy python3-h5py

    wget -O ont_albacore-2.3.1-cp35-cp35m-manylinux1_x86_64.whl https://mirror.oxfordnanoportal.com/software/analysis/ont_albacore-2.3.1-cp35-cp35m-manylinux1_x86_64.whl
    pip3 install ont_albacore-2.3.1-cp35-cp35m-manylinux1_x86_64.whl
```

## Collection

 - Name: [TannerDowhy/albacore-playbook](https://github.com/TannerDowhy/albacore-playbook)
 - License: None

