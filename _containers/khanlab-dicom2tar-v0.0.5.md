---
id: 3732
name: "khanlab/dicom2tar"
branch: "master"
tag: "v0.0.5"
commit: "741bfe01e83000e7be1eb3eeaa444eaddcd2f4d2"
version: "dd66305677e49159bf8cb6199ad80c17"
build_date: "2021-01-18T18:23:53.273Z"
size_mb: 296
size: 130215967
sif: "https://datasets.datalad.org/shub/khanlab/dicom2tar/v0.0.5/2021-01-18-741bfe01-dd663056/dd66305677e49159bf8cb6199ad80c17.simg"
url: https://datasets.datalad.org/shub/khanlab/dicom2tar/v0.0.5/2021-01-18-741bfe01-dd663056/
recipe: https://datasets.datalad.org/shub/khanlab/dicom2tar/v0.0.5/2021-01-18-741bfe01-dd663056/Singularity
collection: khanlab/dicom2tar
---

# khanlab/dicom2tar:v0.0.5

```bash
$ singularity pull shub://khanlab/dicom2tar:v0.0.5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial

#------------------------------------
%setup
#------------------------------------

mkdir -p $SINGULARITY_ROOTFS/apps

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
    python-pip \
    rsync \
    openssh-client

sudo pip install --upgrade pip
sudo pip install --upgrade setuptools
sudo pip install dicom2tar

#dicomunwrap, will install pydicom
cd /apps
git clone https://gitlab.com/cfmm/DicomRaw
cd DicomRaw
sudo pip install -r requirements.txt
%environment
export PATH=/apps/DicomRaw/bin:$PATH

%runscript 
exec dicom2tar "$@"
```

## Collection

 - Name: [khanlab/dicom2tar](https://github.com/khanlab/dicom2tar)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

