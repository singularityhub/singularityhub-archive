---
id: 14611
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "openfoam7"
commit: "345844dfa8959db91dfde73268014b038676392f"
version: "8ac391e28869ba76d2bd0dd64450e3bf65d60f2e49389cd40c0b9a0feee232aa"
build_date: "2020-10-15T13:18:20.998Z"
size_mb: 786.24609375
size: 824438784
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/openfoam7/2020-10-15-345844df-8ac391e2/8ac391e28869ba76d2bd0dd64450e3bf65d60f2e49389cd40c0b9a0feee232aa.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/SupercomputingWales/singularity_hub/openfoam7/2020-10-15-345844df-8ac391e2/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/openfoam7/2020-10-15-345844df-8ac391e2/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:openfoam7

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:openfoam7
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:focal-20200925

%labels
MAINTAINER Thomas Green

%environment

%runscript
exec /bin/bash /bin/echo "Not supported"

%post

export DEBIAN_FRONTEND=noninteractive
# Turn on debugging
set -x

# Create some common mountpoints for systems without overlayfs
mkdir /scratch
mkdir /apps

# Install Git
apt-get update
apt-get install -y git wget software-properties-common

cd /tmp
# Might be useful for visualisation.
wget https://netix.dl.sourceforge.net/project/virtualgl/2.6.4/virtualgl_2.6.4_amd64.deb
apt install -y ./virtualgl_2.6.4_amd64.deb

# OpenFOAM repo
wget -O - https://dl.openfoam.org/gpg.key | apt-key add -
add-apt-repository universe
add-apt-repository http://dl.openfoam.org/ubuntu
apt-get update
apt-get install -y openfoam7

# Due to strange use of kernel feature need to strip ABI info
# See: https://askubuntu.com/questions/1034313/ubuntu-18-4-libqt5core-so-5-cannot-open-shared-object-file-no-such-file-or-dir
strip --remove-section=.note.ABI-tag /lib/x86_64-linux-gnu/libQt5Core.so.5.12.8
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

