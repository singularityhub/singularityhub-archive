---
id: 9178
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "fpocket"
commit: "050506573c0e8e40d9a5dc3f297bfb6da4916d87"
version: "846827bdbb868c8e1f83b802a539fec3"
build_date: "2019-05-28T14:10:13.857Z"
size_mb: 1618
size: 494911519
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/fpocket/2019-05-28-05050657-846827bd/846827bdbb868c8e1f83b802a539fec3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/SupercomputingWales/singularity_hub/fpocket/2019-05-28-05050657-846827bd/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/fpocket/2019-05-28-05050657-846827bd/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:fpocket

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:fpocket
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
yum -y install yum-utils
yum -y install epel-release
yum -y groupinstall "Base"
yum -y groupinstall "Development Tools"

#Install dependency
yum -y install netcdf-devel

#Install software
cd /tmp
git clone https://github.com/Discngine/fpocket.git
cd fpocket
make 
make install
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

