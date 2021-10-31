---
id: 7717
name: "dwassmer/gpu-cluster-test"
branch: "master"
tag: "notebook"
commit: "7702ca5f17cbdc0bdb2f35b20f4060a44a79acb1"
version: "1cb55bfbef07439fbb4b7d4fb3609513"
build_date: "2019-03-12T15:09:01.771Z"
size_mb: 2512
size: 775245855
sif: "https://datasets.datalad.org/shub/dwassmer/gpu-cluster-test/notebook/2019-03-12-7702ca5f-1cb55bfb/1cb55bfbef07439fbb4b7d4fb3609513.simg"
url: https://datasets.datalad.org/shub/dwassmer/gpu-cluster-test/notebook/2019-03-12-7702ca5f-1cb55bfb/
recipe: https://datasets.datalad.org/shub/dwassmer/gpu-cluster-test/notebook/2019-03-12-7702ca5f-1cb55bfb/Singularity
collection: dwassmer/gpu-cluster-test
---

# dwassmer/gpu-cluster-test:notebook

```bash
$ singularity pull shub://dwassmer/gpu-cluster-test:notebook
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
     # install special packages
     /opt/conda/bin/conda install -c conda-forge -y -q ipywebrtc
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

