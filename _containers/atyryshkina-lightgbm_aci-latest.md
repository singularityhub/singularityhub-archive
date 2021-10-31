---
id: 11615
name: "atyryshkina/lightgbm_aci"
branch: "master"
tag: "latest"
commit: "e9b65d1bf8c9b137ef862588360adfaab8b3bb95"
version: "75fba00cb3f6d078e20f94a264b292f2"
build_date: "2019-12-10T19:31:35.952Z"
size_mb: 4490.0
size: 1812197407
sif: "https://datasets.datalad.org/shub/atyryshkina/lightgbm_aci/latest/2019-12-10-e9b65d1b-75fba00c/75fba00cb3f6d078e20f94a264b292f2.sif"
url: https://datasets.datalad.org/shub/atyryshkina/lightgbm_aci/latest/2019-12-10-e9b65d1b-75fba00c/
recipe: https://datasets.datalad.org/shub/atyryshkina/lightgbm_aci/latest/2019-12-10-e9b65d1b-75fba00c/Singularity
collection: atyryshkina/lightgbm_aci
---

# atyryshkina/lightgbm_aci:latest

```bash
$ singularity pull shub://atyryshkina/lightgbm_aci:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: shub://willgpaik/centos7_aci:latest

%post
yum -y update


pip3.6 install --upgrade pip
pip install numpy \
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
        lightgbm \
        hyperopt \
        xgboost
```

## Collection

 - Name: [atyryshkina/lightgbm_aci](https://github.com/atyryshkina/lightgbm_aci)
 - License: None

