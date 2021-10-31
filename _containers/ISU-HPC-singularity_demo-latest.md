---
id: 6163
name: "ISU-HPC/singularity_demo"
branch: "master"
tag: "latest"
commit: "4bac8f32fb8973a97a8705e8bba967d13f755337"
version: "f67c81dda1bae79000f3f2fe55fd4619"
build_date: "2019-01-08T21:54:25.330Z"
size_mb: 1750
size: 809033759
sif: "https://datasets.datalad.org/shub/ISU-HPC/singularity_demo/latest/2019-01-08-4bac8f32-f67c81dd/f67c81dda1bae79000f3f2fe55fd4619.simg"
url: https://datasets.datalad.org/shub/ISU-HPC/singularity_demo/latest/2019-01-08-4bac8f32-f67c81dd/
recipe: https://datasets.datalad.org/shub/ISU-HPC/singularity_demo/latest/2019-01-08-4bac8f32-f67c81dd/Singularity
collection: ISU-HPC/singularity_demo
---

# ISU-HPC/singularity_demo:latest

```bash
$ singularity pull shub://ISU-HPC/singularity_demo:latest
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

