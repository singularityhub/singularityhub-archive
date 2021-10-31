---
id: 13139
name: "drewpolasky/pytorch_aci"
branch: "master"
tag: "latest"
commit: "eadce68c048ab8c39298d1d76d5098b4fc6ddbe6"
version: "f0266dd0c933a606880165c5c2fda11f"
build_date: "2020-05-27T15:50:28.266Z"
size_mb: 6573.0
size: 3302617119
sif: "https://datasets.datalad.org/shub/drewpolasky/pytorch_aci/latest/2020-05-27-eadce68c-f0266dd0/f0266dd0c933a606880165c5c2fda11f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/drewpolasky/pytorch_aci/latest/2020-05-27-eadce68c-f0266dd0/
recipe: https://datasets.datalad.org/shub/drewpolasky/pytorch_aci/latest/2020-05-27-eadce68c-f0266dd0/Singularity
collection: drewpolasky/pytorch_aci
---

# drewpolasky/pytorch_aci:latest

```bash
$ singularity pull shub://drewpolasky/pytorch_aci:latest
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

 - Name: [drewpolasky/pytorch_aci](https://github.com/drewpolasky/pytorch_aci)
 - License: None

