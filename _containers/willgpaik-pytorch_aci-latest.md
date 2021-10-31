---
id: 8061
name: "willgpaik/pytorch_aci"
branch: "master"
tag: "latest"
commit: "969e9251a85a221c2f4d7f26e454ff2eefe3820a"
version: "8800e4467d023a0eea0d9fd875f4cecd40ab2d849d7ea0c74861f50b2104ddbe"
build_date: "2020-06-05T04:10:21.853Z"
size_mb: 3133.0
size: 3331342336
sif: "https://datasets.datalad.org/shub/willgpaik/pytorch_aci/latest/2020-06-05-969e9251-8800e446/8800e4467d023a0eea0d9fd875f4cecd40ab2d849d7ea0c74861f50b2104ddbe.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/pytorch_aci/latest/2020-06-05-969e9251-8800e446/
recipe: https://datasets.datalad.org/shub/willgpaik/pytorch_aci/latest/2020-06-05-969e9251-8800e446/Singularity
collection: willgpaik/pytorch_aci
---

# willgpaik/pytorch_aci:latest

```bash
$ singularity pull shub://willgpaik/pytorch_aci:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: willgpaik/centos7_aci:latest


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
        torch-geometric \
        geometric \
        networkx \
        tensorboardx
```

## Collection

 - Name: [willgpaik/pytorch_aci](https://github.com/willgpaik/pytorch_aci)
 - License: None

