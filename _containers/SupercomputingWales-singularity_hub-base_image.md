---
id: 3553
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "base_image"
commit: "7f10e4df70b0ef91cfa22702a5cab0d63de40086"
version: "55b14fe57db358758261e4280dc4b786"
build_date: "2021-01-15T11:22:35.666Z"
size_mb: 756
size: 340279327
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/base_image/2021-01-15-7f10e4df-55b14fe5/55b14fe57db358758261e4280dc4b786.simg"
url: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/base_image/2021-01-15-7f10e4df-55b14fe5/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/base_image/2021-01-15-7f10e4df-55b14fe5/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:base_image

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:base_image
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
mkdir /scratch
mkdir /software
yum -y install -y yum-utils
yum -y groupinstall "Base"
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

