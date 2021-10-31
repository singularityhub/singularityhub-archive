---
id: 1165
name: "TakahisaShiratori/openfoam"
branch: "master"
tag: "4"
commit: "55d4c5cbd2c9c373fa7771ccbb1e289601ac1b99"
version: "f4458c13a27b2474c203a31073802fae"
build_date: "2021-04-16T09:05:06.445Z"
size_mb: 1576
size: 533680159
sif: "https://datasets.datalad.org/shub/TakahisaShiratori/openfoam/4/2021-04-16-55d4c5cb-f4458c13/f4458c13a27b2474c203a31073802fae.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TakahisaShiratori/openfoam/4/2021-04-16-55d4c5cb-f4458c13/
recipe: https://datasets.datalad.org/shub/TakahisaShiratori/openfoam/4/2021-04-16-55d4c5cb-f4458c13/Singularity
collection: TakahisaShiratori/openfoam
---

# TakahisaShiratori/openfoam:4

```bash
$ singularity pull shub://TakahisaShiratori/openfoam:4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:14.04

%post
    apt-get -y update
    apt-get -y upgrade
    apt-get -y install apt-file
    apt-get -y install software-properties-common
    apt-get -y install wget
    apt-get -y install apt-transport-https
    add-apt-repository http://dl.openfoam.org/ubuntu
    sh -c "wget -O - http://dl.openfoam.org/gpg.key | apt-key add -"
    apt-get -y update
    apt-get -y install openfoam4
    # sed -ie '$ a \. /opt/openfoam4/etc/bashrc' /root/.bashrc
    echo '. /opt/openfoam4/etc/bashrc' >>$SINGULARITY_ENVIRONMENT

%runscript
    simpleFoam
```

## Collection

 - Name: [TakahisaShiratori/openfoam](https://github.com/TakahisaShiratori/openfoam)
 - License: None

