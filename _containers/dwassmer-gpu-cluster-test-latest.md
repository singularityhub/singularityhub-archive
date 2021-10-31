---
id: 7658
name: "dwassmer/gpu-cluster-test"
branch: "master"
tag: "latest"
commit: "34b13c84f0f0d148d44004732adf9d6051e104f2"
version: "419012eaf8e7c09c2c8969b2f8bf777a"
build_date: "2019-03-11T14:27:19.767Z"
size_mb: 1755
size: 505155615
sif: "https://datasets.datalad.org/shub/dwassmer/gpu-cluster-test/latest/2019-03-11-34b13c84-419012ea/419012eaf8e7c09c2c8969b2f8bf777a.simg"
url: https://datasets.datalad.org/shub/dwassmer/gpu-cluster-test/latest/2019-03-11-34b13c84-419012ea/
recipe: https://datasets.datalad.org/shub/dwassmer/gpu-cluster-test/latest/2019-03-11-34b13c84-419012ea/Singularity
collection: dwassmer/gpu-cluster-test
---

# dwassmer/gpu-cluster-test:latest

```bash
$ singularity pull shub://dwassmer/gpu-cluster-test:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/miniconda3

%labels
   Maintainer Daniel Wassmer & Tobias Schlatter
   Version v0.1
   
%environment
     conda=/opt/conda/bin/conda
     pip=/opt/conda/bin/pip
     python3=/opt/conda/bin/python
     export conda pip python3
     
%runscript
     echo "Running scripts..."

%post
     
     # Update conda packages
     /opt/conda/bin/conda update --all -y --quiet
     # Install basic packages
     /opt/conda/bin/conda install -c conda-forge -y -q pip matplotlib tqdm jupyter cython scipy numpy pandas tensorflow
     # Update pip
     /opt/conda/bin/pip install -U pip -q
     # Clean up
     /opt/conda/bin/conda clean --all -y --quiet
     apt-get autoremove -y
     apt-get clean

%test  
     echo "Testing python..."
     /opt/conda/bin/python -V
```

## Collection

 - Name: [dwassmer/gpu-cluster-test](https://github.com/dwassmer/gpu-cluster-test)
 - License: None

