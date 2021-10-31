---
id: 6822
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "deeplabcut_cpu"
commit: "1d4dd57819816a53e50fcbb7d30d11345e1e9152"
version: "5c596545a0063d07cb04f190b5c50d22"
build_date: "2021-04-18T20:04:20.946Z"
size_mb: 6346
size: 3125821471
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/deeplabcut_cpu/2021-04-18-1d4dd578-5c596545/5c596545a0063d07cb04f190b5c50d22.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/SupercomputingWales/singularity_hub/deeplabcut_cpu/2021-04-18-1d4dd578-5c596545/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/deeplabcut_cpu/2021-04-18-1d4dd578-5c596545/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:deeplabcut_cpu

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:deeplabcut_cpu
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:bethgelab/deeplearning:cuda9.0-cudnn7

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
apt-get update

# Install requested applications.
apt-get -y install ffmpeg
apt-get -y install python-wxgtk3.0
apt-get -y install python3-tk

# Install from pip
pip3 install --upgrade pip

pip3 install tensorflow==1.8

pip3 install deeplabcut

pip install ipywidgets

pip3 install ipywidgets

pip3 install seaborn

pip3 install https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-16.04/wxPython-4.0.3-cp36-cp36m-linux_x86_64.whl
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

