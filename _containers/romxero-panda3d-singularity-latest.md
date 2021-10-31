---
id: 15514
name: "romxero/panda3d-singularity"
branch: "main"
tag: "latest"
commit: "de9b12c055aef7194a845c76eee8f29572207b50"
version: "02de389cba8af7ad4cfc64592f68506b"
build_date: "2021-02-17T06:04:58.537Z"
size_mb: 2364.0
size: 822386719
sif: "https://datasets.datalad.org/shub/romxero/panda3d-singularity/latest/2021-02-17-de9b12c0-02de389c/02de389cba8af7ad4cfc64592f68506b.sif"
url: https://datasets.datalad.org/shub/romxero/panda3d-singularity/latest/2021-02-17-de9b12c0-02de389c/
recipe: https://datasets.datalad.org/shub/romxero/panda3d-singularity/latest/2021-02-17-de9b12c0-02de389c/Singularity
collection: romxero/panda3d-singularity
---

# romxero/panda3d-singularity:latest

```bash
$ singularity pull shub://romxero/panda3d-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
Author "Randall Cab White - rcwhite@stanford.edu"

#########
#%setup
#########
#########

#Downlaod packages
%post
  apt-get -ym update
  ln -fs /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
  apt-get install -y tzdata
  dpkg-reconfigure --frontend noninteractive tzdata

export DEBIAN_FRONTEND=noninteractive
apt-get -ym install keyboard-configuration

  apt-get -ymq install libsdl2-image-2.0-0 libsdl2-image-dev gcc yasm \
wget curl gnupg2 jq sed gawk util-linux libsdl-dev \
git cmake build-essential parallel libjpeg-dev libsdl-image* \
rsync perl ssh openssl coreutils emscripten libpng-dev \
build-essential pkg-config fakeroot python3-dev libpng-dev libjpeg-dev libtiff-dev zlib1g-dev \
libssl-dev libx11-dev libgl1-mesa-dev libxrandr-dev libxxf86dga-dev libxcursor-dev bison flex \
libfreetype6-dev libvorbis-dev libeigen3-dev libopenal-dev libode-dev libbullet-dev \
nvidia-cg-toolkit libgtk2.0-dev libassimp-dev libopenexr-dev libavcodec57 \
libavformat57 libavutil55 libopusfile0 libsquish0 libswresample2 libswscale4 \
tigervnc-standalone-server tigervnc-viewer tigervnc-xorg-extension fluxbox	coreutils bash-builtins procps xterm \
codelite codelite-plugins geany geany-plugin-gproject firefox locales


#grabbing building libbpg
mkdir /panda3d
cd /panda3d
wget https://www.panda3d.org/download/panda3d-1.10.8/panda3d1.10_1.10.8~bionic_amd64.deb

dpkg -i ./panda3d1.10_1.10.8~bionic_amd64.deb


rm panda3d1.10_1.10.8~bionic_amd64.deb


locale-gen en_US en_US.UTF-8
dpkg-reconfigure locales 

%environment
  export IMAGE_NAME="panda3d container"
#  export LC_ALL="en_US.UTF-8"
  export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$PATH
%runscript


#
```

## Collection

 - Name: [romxero/panda3d-singularity](https://github.com/romxero/panda3d-singularity)
 - License: None

