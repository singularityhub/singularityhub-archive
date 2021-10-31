---
id: 6164
name: "ISU-HPC/singularity_demo"
branch: "master"
tag: "3.8.6"
commit: "200f8b16e9b904470aa957531b8b36a4b6254bac"
version: "87038930cbc7f0527922bb33ff866dbc"
build_date: "2019-01-08T21:54:25.323Z"
size_mb: 1750
size: 809033759
sif: "https://datasets.datalad.org/shub/ISU-HPC/singularity_demo/3.8.6/2019-01-08-200f8b16-87038930/87038930cbc7f0527922bb33ff866dbc.simg"
url: https://datasets.datalad.org/shub/ISU-HPC/singularity_demo/3.8.6/2019-01-08-200f8b16-87038930/
recipe: https://datasets.datalad.org/shub/ISU-HPC/singularity_demo/3.8.6/2019-01-08-200f8b16-87038930/Singularity
collection: ISU-HPC/singularity_demo
---

# ISU-HPC/singularity_demo:3.8.6

```bash
$ singularity pull shub://ISU-HPC/singularity_demo:3.8.6
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%runscript
exec /opt/conda/bin/python "$@"

%labels
maintainer ynanyam@iastate.edu

%post
apt-get update && apt-get install -y git

# Dependncies
/opt/conda/bin/conda install -y numpy scikit-learn cython pandas

# Install Singularity Python
cd /opt
git clone https://www.github.com/singularityware/singularity-python
cd singularity-python
/opt/conda/bin/pip install setuptools
/opt/conda/bin/pip install -r requirements.txt
/opt/conda/bin/python setup.py install
```

## Collection

 - Name: [ISU-HPC/singularity_demo](https://github.com/ISU-HPC/singularity_demo)
 - License: None

