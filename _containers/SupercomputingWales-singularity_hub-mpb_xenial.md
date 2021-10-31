---
id: 3461
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "mpb_xenial"
commit: "65260268c98ae5cf021292b277d1906f7ead1114"
version: "5abc1036dff11e29886af0cedf37f55b"
build_date: "2020-10-05T08:43:29.962Z"
size_mb: 308
size: 127602719
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/mpb_xenial/2020-10-05-65260268-5abc1036/5abc1036dff11e29886af0cedf37f55b.simg"
url: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/mpb_xenial/2020-10-05-65260268-5abc1036/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/mpb_xenial/2020-10-05-65260268-5abc1036/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:mpb_xenial

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:mpb_xenial
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:xenial-20180525

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

