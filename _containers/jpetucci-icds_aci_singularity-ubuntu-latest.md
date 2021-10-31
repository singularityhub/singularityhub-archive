---
id: 13218
name: "jpetucci/icds_aci_singularity-ubuntu"
branch: "master"
tag: "latest"
commit: "6af157f89cc428865ee376a216c1636cb659399e"
version: "7c99a5fb9b1097926192aec17ff815408c18ade4e1c5a3ce3fc3e5d728f30d7d"
build_date: "2020-06-04T15:50:44.527Z"
size_mb: 1350.83984375
size: 1416458240
sif: "https://datasets.datalad.org/shub/jpetucci/icds_aci_singularity-ubuntu/latest/2020-06-04-6af157f8-7c99a5fb/7c99a5fb9b1097926192aec17ff815408c18ade4e1c5a3ce3fc3e5d728f30d7d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/jpetucci/icds_aci_singularity-ubuntu/latest/2020-06-04-6af157f8-7c99a5fb/
recipe: https://datasets.datalad.org/shub/jpetucci/icds_aci_singularity-ubuntu/latest/2020-06-04-6af157f8-7c99a5fb/Singularity
collection: jpetucci/icds_aci_singularity-ubuntu
---

# jpetucci/icds_aci_singularity-ubuntu:latest

```bash
$ singularity pull shub://jpetucci/icds_aci_singularity-ubuntu:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:xenial

%post


apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        lsb-release \
        curl \
        libfreetype6-dev \
        libpng12-dev \
        libzmq3-dev \
        module-init-tools \
        openjdk-8-jdk \
        pkg-config \
        python \
        python-dev \
        python-numpy \
        rsync \
        unzip \
        vim \
        wget 

apt-get update -y
apt-get upgrade -y
apt-get dist-upgrade -y
apt-get install build-essential -y
apt-get install ubuntu-gnome-desktop -y
apt-get install gnome-shell -y    
apt-get install language-pack-en-base -y
dpkg-reconfigure locales
apt-get install xorg -y
apt-get install xorg-dev -y
apt-get install mesa-utils -y
apt-get install -y flex bison cmake zlib1g-dev libboost-system-dev libboost-thread-dev libopenmpi-dev openmpi-bin gnuplot libreadline-dev libncurses-dev libxt-dev libscotch-dev libptscotch-dev
apt-get install libvtk6-dev -y
```

## Collection

 - Name: [jpetucci/icds_aci_singularity-ubuntu](https://github.com/jpetucci/icds_aci_singularity-ubuntu)
 - License: None

