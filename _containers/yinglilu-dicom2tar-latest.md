---
id: 3731
name: "yinglilu/dicom2tar"
branch: "master"
tag: "latest"
commit: "8f2bd1f4b2e405b5f251d208f69178edbdf1bf8b"
version: "957b6e4a61bbf1a882139a934839d65b"
build_date: "2018-07-27T19:35:01.357Z"
size_mb: 280
size: 121663519
sif: "https://datasets.datalad.org/shub/yinglilu/dicom2tar/latest/2018-07-27-8f2bd1f4-957b6e4a/957b6e4a61bbf1a882139a934839d65b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/yinglilu/dicom2tar/latest/2018-07-27-8f2bd1f4-957b6e4a/
recipe: https://datasets.datalad.org/shub/yinglilu/dicom2tar/latest/2018-07-27-8f2bd1f4-957b6e4a/Singularity
collection: yinglilu/dicom2tar
---

# yinglilu/dicom2tar:latest

```bash
$ singularity pull shub://yinglilu/dicom2tar:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial

#ver:0.1.1

#------------------------------------
%setup
#------------------------------------

#------------------------------------
%post
#------------------------------------

export DEBIAN_FRONTEND=noninteractive
apt-get update && apt-get install -y --no-install-recommends apt-utils \
    sudo \
    git \
    wget \
    curl \
    zip \
    unzip \
    python2.7 \
    python-pip
    
sudo pip install --upgrade pip setuptools
sudo pip install dicom2tar

%runscript 
exec dicom2tar "$@"
```

## Collection

 - Name: [yinglilu/dicom2tar](https://github.com/yinglilu/dicom2tar)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

