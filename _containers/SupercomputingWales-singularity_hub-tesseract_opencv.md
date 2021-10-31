---
id: 8393
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "tesseract_opencv"
commit: "b5cb5b87b7ac1d83a26788a14d869e3ad9729435"
version: "62652d817edc908b1f0b8d6c6407b276"
build_date: "2019-04-13T15:18:57.597Z"
size_mb: 1651
size: 737423391
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/tesseract_opencv/2019-04-13-b5cb5b87-62652d81/62652d817edc908b1f0b8d6c6407b276.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/SupercomputingWales/singularity_hub/tesseract_opencv/2019-04-13-b5cb5b87-62652d81/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/tesseract_opencv/2019-04-13-b5cb5b87-62652d81/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:tesseract_opencv

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:tesseract_opencv
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:valian/docker-python-opencv-ffmpeg:py3

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
# Run repo helper to install universe
add-apt-repository -y universe
add-apt-repository -y ppa:alex-p/tesseract-ocr
apt-get update
apt-get install -y tesseract-ocr-all

# Install requested applications.
pip3 install pillow
pip3 install pytesseract
pip3 install imutils
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

