---
id: 11452
name: "atyryshkina/test"
branch: "master"
tag: "latest"
commit: "abc4e89ab8112f3b1bf0299f397fc4e4760ff683"
version: "4b94885226c7252638d02c84d946636b"
build_date: "2019-12-06T03:27:46.825Z"
size_mb: 4589.0
size: 1843367967
sif: "https://datasets.datalad.org/shub/atyryshkina/test/latest/2019-12-06-abc4e89a-4b948852/4b94885226c7252638d02c84d946636b.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/atyryshkina/test/latest/2019-12-06-abc4e89a-4b948852/
recipe: https://datasets.datalad.org/shub/atyryshkina/test/latest/2019-12-06-abc4e89a-4b948852/Singularity
collection: atyryshkina/test
---

# atyryshkina/test:latest

```bash
$ singularity pull shub://atyryshkina/test:latest
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
        xgboost \
        jupyterlab
```

## Collection

 - Name: [atyryshkina/test](https://github.com/atyryshkina/test)
 - License: None

