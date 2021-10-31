---
id: 6155
name: "johnfrx/globus-container"
branch: "master"
tag: "latest"
commit: "cdd990e5985160505d713c4614ed664ac668d8c6"
version: "7c5fdca1bd59cd0ccf7ba6380d0232e3"
build_date: "2020-01-16T03:48:31.847Z"
size_mb: 415
size: 147017759
sif: "https://datasets.datalad.org/shub/johnfrx/globus-container/latest/2020-01-16-cdd990e5-7c5fdca1/7c5fdca1bd59cd0ccf7ba6380d0232e3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/johnfrx/globus-container/latest/2020-01-16-cdd990e5-7c5fdca1/
recipe: https://datasets.datalad.org/shub/johnfrx/globus-container/latest/2020-01-16-cdd990e5-7c5fdca1/Singularity
collection: johnfrx/globus-container
---

# johnfrx/globus-container:latest

```bash
$ singularity pull shub://johnfrx/globus-container:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest

%runscript
    exec echo "Centos7 image for use with globus"


%post
    #echo "The post section is where you can install, and configure your container."
    #
    yum -y update && yum -y install epel-release openssl openssl-dev
    yum -y install git wget bzip2 aria2
    yum -y install tmux atop dstat
    yum -y install yum-utils
    #
    # Install the globus repo
    mkdir -p /etc/pki/rpm-gpg
    mkdir -p /data
    mkdir -p /seq
    mkdir -p /secure
    mkdir -p /scratch
    wget https://downloads.globus.org/toolkit/gt6/stable/repo/rpm/RPM-GPG-KEY-Globus -O /etc/pki/rpm-gpg/RPM-GPG-KEY-Globus
    yum-config-manager --add-repo https://downloads.globus.org/toolkit/gt6/stable/repo/rpm/globus-toolkit-6-stable-el7.repo
    yum-config-manager --enable Globus-Toolkit-6-el7
    yum install -y globus-gridftp
```

## Collection

 - Name: [johnfrx/globus-container](https://github.com/johnfrx/globus-container)
 - License: None

