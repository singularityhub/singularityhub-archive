---
id: 3460
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "mpb_bionic"
commit: "65260268c98ae5cf021292b277d1906f7ead1114"
version: "0c68950f7fbe0251e9bbba1315998a76"
build_date: "2018-07-10T16:54:20.993Z"
size_mb: 296
size: 121032735
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/mpb_bionic/2018-07-10-65260268-0c68950f/0c68950f7fbe0251e9bbba1315998a76.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/SupercomputingWales/singularity_hub/mpb_bionic/2018-07-10-65260268-0c68950f/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/mpb_bionic/2018-07-10-65260268-0c68950f/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:mpb_bionic

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:mpb_bionic
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:bionic-20180526

%labels
MAINTAINER Thomas Green

%environment

%runscript
exec /bin/bash /bin/echo "Not supported"

%post
# Create some common mountpoints for systems without overlayfs
mkdir /scratch 
mkdir /software
# Update metadata on packages
apt-get update
# Install repo helper
apt-get install -y software-properties-common
# Run repo helper to install universe
add-apt-repository -y universe
# Install requested applications.
apt-get install -y meep
apt-get install -y meep-mpi-default
apt-get install -y mpb h5utils
apt-get install -y mpb-mpi
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

