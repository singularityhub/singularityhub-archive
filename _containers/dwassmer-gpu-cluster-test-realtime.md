---
id: 7719
name: "dwassmer/gpu-cluster-test"
branch: "master"
tag: "realtime"
commit: "c660458e3ad90bab0a6f39ccaefa47cdf8152c72"
version: "1347ae637e67e0d2b5ec8e5dbd7bcc94"
build_date: "2019-03-14T08:11:52.264Z"
size_mb: 2010
size: 564305951
sif: "https://datasets.datalad.org/shub/dwassmer/gpu-cluster-test/realtime/2019-03-14-c660458e-1347ae63/1347ae637e67e0d2b5ec8e5dbd7bcc94.simg"
url: https://datasets.datalad.org/shub/dwassmer/gpu-cluster-test/realtime/2019-03-14-c660458e-1347ae63/
recipe: https://datasets.datalad.org/shub/dwassmer/gpu-cluster-test/realtime/2019-03-14-c660458e-1347ae63/Singularity
collection: dwassmer/gpu-cluster-test
---

# dwassmer/gpu-cluster-test:realtime

```bash
$ singularity pull shub://dwassmer/gpu-cluster-test:realtime
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
     /opt/conda/bin/conda install -c conda-forge -y -q dlib ipywebrtc
     /opt/conda/bin/conda install -c gilbertfrancois -y -q imutils
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

