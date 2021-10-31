---
id: 11683
name: "ecetter/hwsing"
branch: "master"
tag: "latest"
commit: "9efb875bbbf06159501d0dcecebbcf422f5c2577"
version: "31f441528eaaddbb93be928930a9a781"
build_date: "2019-11-22T19:18:47.356Z"
size_mb: 6361.0
size: 3266326559
sif: "https://datasets.datalad.org/shub/ecetter/hwsing/latest/2019-11-22-9efb875b-31f44152/31f441528eaaddbb93be928930a9a781.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ecetter/hwsing/latest/2019-11-22-9efb875b-31f44152/
recipe: https://datasets.datalad.org/shub/ecetter/hwsing/latest/2019-11-22-9efb875b-31f44152/Singularity
collection: ecetter/hwsing
---

# ecetter/hwsing:latest

```bash
$ singularity pull shub://ecetter/hwsing:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shub://willgpaik/centos7_aci:latest


%post
yum -y update

pip3.6 install --upgrade pip
pip install https://download.pytorch.org/whl/cpu/torch-1.3.0%2Bcpu-cp36-cp36m-linux_x86_64.whl
pip install torchvision \
        torchsummary \
        scipy \
        pandas \
        scikit-learn \
        jupyter \
        jupyterlab \
        spyder \
        ipython \
        matplotlib \
        seaborn \
        scikit-image \
        bokeh \
        plotly \
        pillow \
        opencv-python
```

## Collection

 - Name: [ecetter/hwsing](https://github.com/ecetter/hwsing)
 - License: None

