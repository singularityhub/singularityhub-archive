---
id: 3743
name: "jormelton/containerCLASSIC"
branch: "master"
tag: "latest"
commit: "87ae59a73e49a68bb188c3fab1a49894a816452b"
version: "bcd16e17f9ed8d38afd7b16ba0728215"
build_date: "2019-11-05T23:17:20.591Z"
size_mb: 634
size: 233447455
sif: "https://datasets.datalad.org/shub/jormelton/containerCLASSIC/latest/2019-11-05-87ae59a7-bcd16e17/bcd16e17f9ed8d38afd7b16ba0728215.simg"
url: https://datasets.datalad.org/shub/jormelton/containerCLASSIC/latest/2019-11-05-87ae59a7-bcd16e17/
recipe: https://datasets.datalad.org/shub/jormelton/containerCLASSIC/latest/2019-11-05-87ae59a7-bcd16e17/Singularity
collection: jormelton/containerCLASSIC
---

# jormelton/containerCLASSIC:latest

```bash
$ singularity pull shub://jormelton/containerCLASSIC:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:latest

%labels
MAINTAINER Joe Melton, ECCC

%environment
BASE_DIR=/code
export BASE_DIR

%runscript
cd /code/classctem
echo "The container is running!"

%post
mkdir -p /code
cd /code
apt update
apt install vim make libnetcdff-dev git gfortran netcdf-bin nano zlib1g mpich doxygen -y -f -m
```

## Collection

 - Name: [jormelton/containerCLASSIC](https://github.com/jormelton/containerCLASSIC)
 - License: None

