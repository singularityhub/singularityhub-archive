---
id: 13839
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "nextnano"
commit: "1c0f177d99b1fa8c5a975dc6f5b15743e09acc6a"
version: "6ee7fe1745fb9f5b0de5dd0bed5e1d254fbe116af7f14025f5522e9dcbc881a1"
build_date: "2020-11-17T22:57:25.479Z"
size_mb: 742.91796875
size: 779005952
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/nextnano/2020-11-17-1c0f177d-6ee7fe17/6ee7fe1745fb9f5b0de5dd0bed5e1d254fbe116af7f14025f5522e9dcbc881a1.sif"
url: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/nextnano/2020-11-17-1c0f177d-6ee7fe17/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/nextnano/2020-11-17-1c0f177d-6ee7fe17/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:nextnano

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:nextnano
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:focal-20200729

%labels
MAINTAINER Thomas Green

%environment

%runscript
exec /bin/bash /bin/echo "Not supported"

%post
# Create some common mountpoints for systems without overlayfs
mkdir /scratch
mkdir /apps

# Update metadata on packages
apt-get update
# Install repo helper
apt-get install -y software-properties-common
apt-get install -y wget
apt-get install -y libgfortran5
# Run repo helper to install universe
add-apt-repository -y universe
# Install requested applications.  
# Worth checking which versions of Wine are available for each Ubuntu release.
# Seem to explicitly tell it to be non-interactive.
echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
dpkg --add-architecture i386
cd /tmp
wget -nc https://dl.winehq.org/wine-builds/winehq.key
apt-key add winehq.key
apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main'
apt-get update
apt-get install -y winehq-stable
apt-get install -y mono-complete
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

