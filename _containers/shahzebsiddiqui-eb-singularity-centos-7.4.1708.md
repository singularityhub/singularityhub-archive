---
id: 1569
name: "shahzebsiddiqui/eb-singularity"
branch: "eb_images"
tag: "centos-7.4.1708"
commit: "1014270887f18faf75574eda57369b91a7b97a3a"
version: "fa5012f4615c2a2b34e2d30c915f8f6a"
build_date: "2018-02-15T11:57:05.815Z"
size_mb: 718
size: 226074655
sif: "https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/centos-7.4.1708/2018-02-15-10142708-fa5012f4/fa5012f4615c2a2b34e2d30c915f8f6a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/shahzebsiddiqui/eb-singularity/centos-7.4.1708/2018-02-15-10142708-fa5012f4/
recipe: https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/centos-7.4.1708/2018-02-15-10142708-fa5012f4/Singularity
collection: shahzebsiddiqui/eb-singularity
---

# shahzebsiddiqui/eb-singularity:centos-7.4.1708

```bash
$ singularity pull shub://shahzebsiddiqui/eb-singularity:centos-7.4.1708
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7.4.1708

%help
EasyBuild is a software build and installation framework
written in Python that allows you to install software in a structured,
repeatable and robust way.

%post
     yum update -y
     yum groupinstall -y "Development Tools"
     yum install -y which wget
     yum install -y epel-release
     yum install -y python-pip python-devel  Lmod

     # need this for --package to work to generate RPM
     # yum install ruby ruby-devel rubygems -y &&
     # gem install fpm &&

     pip install --upgrade pip
     pip install setuptools
     pip install easybuild

     # need this for git integration with eb
     #pip install GitPython python-graph-dot graphviz keyring keyrings.alt

     mkdir -p /app/modules/
     mkdir -p /app/software
     mkdir -p /scratch/tmp
     useradd easybuild
     chown easybuild:easybuild -R /app
     chown easybuild:easybuild -R /scratch

%labels
MAINTAINER  Shahzeb Siddiqui
```

## Collection

 - Name: [shahzebsiddiqui/eb-singularity](https://github.com/shahzebsiddiqui/eb-singularity)
 - License: None

