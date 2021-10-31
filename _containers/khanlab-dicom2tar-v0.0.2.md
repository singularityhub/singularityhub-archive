---
id: 1710
name: "khanlab/dicom2tar"
branch: "master"
tag: "v0.0.2"
commit: "7a8338ed09a478e5205a2ae58c7e42d5966d1ed5"
version: "a019a66ab360cc17b734f103f7a41607"
build_date: "2018-07-27T19:34:59.320Z"
size_mb: 335
size: 148439071
sif: "https://datasets.datalad.org/shub/khanlab/dicom2tar/v0.0.2/2018-07-27-7a8338ed-a019a66a/a019a66ab360cc17b734f103f7a41607.simg"
url: https://datasets.datalad.org/shub/khanlab/dicom2tar/v0.0.2/2018-07-27-7a8338ed-a019a66a/
recipe: https://datasets.datalad.org/shub/khanlab/dicom2tar/v0.0.2/2018-07-27-7a8338ed-a019a66a/Singularity
collection: khanlab/dicom2tar
---

# khanlab/dicom2tar:v0.0.2

```bash
$ singularity pull shub://khanlab/dicom2tar:v0.0.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial

%files
dicom2tar.py
DicomSorter.py
sort_rules.py

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

pip install -U pip setuptools

git clone https://www.github.com/pydicom/pydicom.git
cd pydicom
git checkout 1314e86e3a96d0c226a03fb21136c0ff3c3ce7d3  #commit from Feb 1 2018
python setup.py install


%runscript 
exec /dicom2tar.py $@
```

## Collection

 - Name: [khanlab/dicom2tar](https://github.com/khanlab/dicom2tar)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

