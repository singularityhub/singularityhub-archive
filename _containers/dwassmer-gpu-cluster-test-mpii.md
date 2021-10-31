---
id: 7715
name: "dwassmer/gpu-cluster-test"
branch: "master"
tag: "mpii"
commit: "a3f8d0ad31b615a52b563eaa89b037708bf5296f"
version: "020fddb99ecec2c55a570deb881415a1"
build_date: "2019-03-16T19:00:01.419Z"
size_mb: 3927
size: 1611714591
sif: "https://datasets.datalad.org/shub/dwassmer/gpu-cluster-test/mpii/2019-03-16-a3f8d0ad-020fddb9/020fddb99ecec2c55a570deb881415a1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dwassmer/gpu-cluster-test/mpii/2019-03-16-a3f8d0ad-020fddb9/
recipe: https://datasets.datalad.org/shub/dwassmer/gpu-cluster-test/mpii/2019-03-16-a3f8d0ad-020fddb9/Singularity
collection: dwassmer/gpu-cluster-test
---

# dwassmer/gpu-cluster-test:mpii

```bash
$ singularity pull shub://dwassmer/gpu-cluster-test:mpii
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
     /opt/conda/bin/conda install -c conda-forge -y -q ipywebrtc psutil
     /opt/conda/bin/conda install -c pytorch -y -q pytorch torchvision
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

