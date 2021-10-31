---
id: 14010
name: "photocyte/shournal_singularity"
branch: "master"
tag: "latest"
commit: "91c098465e157639d66114e136cc6d155f6e47a8"
version: "a11bc35e9ab37d1c38be63f128e1b936"
build_date: "2020-08-20T19:05:52.112Z"
size_mb: 161.0
size: 58347551
sif: "https://datasets.datalad.org/shub/photocyte/shournal_singularity/latest/2020-08-20-91c09846-a11bc35e/a11bc35e9ab37d1c38be63f128e1b936.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/photocyte/shournal_singularity/latest/2020-08-20-91c09846-a11bc35e/
recipe: https://datasets.datalad.org/shub/photocyte/shournal_singularity/latest/2020-08-20-91c09846-a11bc35e/Singularity
collection: photocyte/shournal_singularity
---

# photocyte/shournal_singularity:latest

```bash
$ singularity pull shub://photocyte/shournal_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
MAINTAINER Timothy R. Fallon 

%files

%environment

%post
    PACKAGE_VER="2.3"
    PACKAGE_NAME="shournal_${PACKAGE_VER}_amd64.deb"
    BUILD_PACKAGES="wget apt-utils apt-transport-https htop"
    DEBIAN_FRONTEND=noninteractive

    apt-get update
    apt-get install --yes $BUILD_PACKAGES
    apt-get install --yes locales
    locale-gen "en_US.UTF-8"
    dpkg-reconfigure locales
    
    ### For shournal
    cd /tmp
    wget -q https://github.com/tycho-kirchner/shournal/releases/download/v${PACKAGE_VER}/${PACKAGE_NAME}
    dpkg -I ${PACKAGE_NAME} ##Print some information about the package dependencies
    apt-get install -y -f /tmp/${PACKAGE_NAME}
    ###
    
    chown root /usr/bin/shournal-run
    chmod u+s /usr/bin/shournal-run      
  
    ### Cleanup
    rm -f *.deb
    apt-get autoremove --purge --yes
    apt-get clean
    rm -rf /var/lib/apt/lists/*
    
%runscript
```

## Collection

 - Name: [photocyte/shournal_singularity](https://github.com/photocyte/shournal_singularity)
 - License: None

