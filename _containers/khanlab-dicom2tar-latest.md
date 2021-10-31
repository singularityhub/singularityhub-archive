---
id: 3737
name: "khanlab/dicom2tar"
branch: "master"
tag: "latest"
commit: "7b40b504afe60d6b11ecc22b3edc53a8da8db523"
version: "f807c2c3ee5b628359910480c8661ab5"
build_date: "2021-04-13T16:52:56.678Z"
size_mb: 285
size: 121319455
sif: "https://datasets.datalad.org/shub/khanlab/dicom2tar/latest/2021-04-13-7b40b504-f807c2c3/f807c2c3ee5b628359910480c8661ab5.simg"
url: https://datasets.datalad.org/shub/khanlab/dicom2tar/latest/2021-04-13-7b40b504-f807c2c3/
recipe: https://datasets.datalad.org/shub/khanlab/dicom2tar/latest/2021-04-13-7b40b504-f807c2c3/Singularity
collection: khanlab/dicom2tar
---

# khanlab/dicom2tar:latest

```bash
$ singularity pull shub://khanlab/dicom2tar:latest
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

 - Name: [khanlab/dicom2tar](https://github.com/khanlab/dicom2tar)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

