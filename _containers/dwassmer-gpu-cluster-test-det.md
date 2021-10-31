---
id: 8664
name: "dwassmer/gpu-cluster-test"
branch: "master"
tag: "det"
commit: "12c6d2c278fcc846b305fd18ed7c97cccbcbcecf"
version: "2b1af8ccbd44b095e1622cc483f9803e"
build_date: "2019-05-01T22:22:27.816Z"
size_mb: 5101
size: 1990877215
sif: "https://datasets.datalad.org/shub/dwassmer/gpu-cluster-test/det/2019-05-01-12c6d2c2-2b1af8cc/2b1af8ccbd44b095e1622cc483f9803e.simg"
url: https://datasets.datalad.org/shub/dwassmer/gpu-cluster-test/det/2019-05-01-12c6d2c2-2b1af8cc/
recipe: https://datasets.datalad.org/shub/dwassmer/gpu-cluster-test/det/2019-05-01-12c6d2c2-2b1af8cc/Singularity
collection: dwassmer/gpu-cluster-test
---

# dwassmer/gpu-cluster-test:det

```bash
$ singularity pull shub://dwassmer/gpu-cluster-test:det
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
     # Install basic package
     /opt/conda/bin/conda install -c conda-forge -y -q pip matplotlib tqdm jupyter cython scipy numpy pandas tensorflow
     # install special packages 
     /opt/conda/bin/conda install -c conda-forge opencv pillow
     /opt/conda/bin/conda install -c conda-forge dlib 
     /opt/conda/bin/pip install -q imutils mss
     /opt/conda/bin/conda install -c pytorch -y -q pytorch torchvision
     # Update pip
     /opt/conda/bin/pip install -U pip -q
     apt-get update
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

