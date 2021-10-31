---
id: 3399
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "fluidity_openmpi"
commit: "fb4b14f33436a9c5525c185d6b32459a0489160d"
version: "1f775c0abd6e71a4091a1e3ed9cca7ed"
build_date: "2018-07-03T14:55:06.982Z"
size_mb: 2008
size: 745459743
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/fluidity_openmpi/2018-07-03-fb4b14f3-1f775c0a/1f775c0abd6e71a4091a1e3ed9cca7ed.simg"
url: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/fluidity_openmpi/2018-07-03-fb4b14f3-1f775c0a/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/fluidity_openmpi/2018-07-03-fb4b14f3-1f775c0a/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:fluidity_openmpi

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:fluidity_openmpi
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
yum-config-manager -y --add-repo http://fluidityproject.github.com/yum/fluidity-rhel7.repo
yum -y groupinstall "Base"
yum -y install python
yum -y install fluidity
yum -y install fluidity-dev
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

