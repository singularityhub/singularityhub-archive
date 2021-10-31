---
id: 3398
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "fluidity_mpich"
commit: "fb4b14f33436a9c5525c185d6b32459a0489160d"
version: "f58205271e27b7e7a232934f4d578249"
build_date: "2020-06-12T22:01:17.250Z"
size_mb: 1991
size: 739954719
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/fluidity_mpich/2020-06-12-fb4b14f3-f5820527/f58205271e27b7e7a232934f4d578249.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/SupercomputingWales/singularity_hub/fluidity_mpich/2020-06-12-fb4b14f3-f5820527/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/fluidity_mpich/2020-06-12-fb4b14f3-f5820527/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:fluidity_mpich

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:fluidity_mpich
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:centos:centos7.4.1708

%labels
MAINTAINER Thomas Green

%environment

%runscript
exec /bin/bash /bin/echo "Not supported"

%post  
yum -y install -y yum-utils
yum-config-manager -y --add-repo http://fluidityproject.github.com/yum/fluidity-rhel7-mpich.repo
yum -y groupinstall "Base"
yum -y install python
yum -y install fluidity
yum -y install fluidity-dev
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

