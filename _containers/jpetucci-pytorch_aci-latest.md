---
id: 11969
name: "jpetucci/pytorch_aci"
branch: "master"
tag: "latest"
commit: "528b9e3b4a8575be6012420ec99f36c06c674b1a"
version: "3fe4b124874b4e7196897acd82bd2bad"
build_date: "2020-09-03T14:04:46.512Z"
size_mb: 6539.0
size: 3320188959
sif: "https://datasets.datalad.org/shub/jpetucci/pytorch_aci/latest/2020-09-03-528b9e3b-3fe4b124/3fe4b124874b4e7196897acd82bd2bad.sif"
url: https://datasets.datalad.org/shub/jpetucci/pytorch_aci/latest/2020-09-03-528b9e3b-3fe4b124/
recipe: https://datasets.datalad.org/shub/jpetucci/pytorch_aci/latest/2020-09-03-528b9e3b-3fe4b124/Singularity
collection: jpetucci/pytorch_aci
---

# jpetucci/pytorch_aci:latest

```bash
$ singularity pull shub://jpetucci/pytorch_aci:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shub://willgpaik/centos7_aci:latest

%runscript
    exec python3 "$@"

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
        opencv-python \
	torchbiggraph
```

## Collection

 - Name: [jpetucci/pytorch_aci](https://github.com/jpetucci/pytorch_aci)
 - License: None

