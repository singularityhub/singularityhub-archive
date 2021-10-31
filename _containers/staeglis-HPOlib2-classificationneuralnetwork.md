---
id: 6295
name: "staeglis/HPOlib2"
branch: "container"
tag: "classificationneuralnetwork"
commit: "83e83de39b2afc473e166dd6582b03364e86ae3c"
version: "283757b06d5c434d0a81724eafdf554d"
build_date: "2019-01-18T10:30:21.765Z"
size_mb: 2970
size: 1690988575
sif: "https://datasets.datalad.org/shub/staeglis/HPOlib2/classificationneuralnetwork/2019-01-18-83e83de3-283757b0/283757b06d5c434d0a81724eafdf554d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/staeglis/HPOlib2/classificationneuralnetwork/2019-01-18-83e83de3-283757b0/
recipe: https://datasets.datalad.org/shub/staeglis/HPOlib2/classificationneuralnetwork/2019-01-18-83e83de3-283757b0/Singularity
collection: staeglis/HPOlib2
---

# staeglis/HPOlib2:classificationneuralnetwork

```bash
$ singularity pull shub://staeglis/HPOlib2:classificationneuralnetwork
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
MAINTAINER Stefan Staeglich

%post
    apt update -y
    apt install git -y
    apt install python3-pip python3-numpy python-configparser cython3 -y
    pip3 install git+https://github.com/automl/ConfigSpace.git@master
    apt install python3-scipy python3-sklearn -y
    pip3 install git+https://github.com/staeglis/HPOlib2@container
    pip3 install pyro4
    pip3 install tensorflow
    pip3 install torch torchvision

%runscript
    python3 -s /usr/local/lib/python3.6/dist-packages/hpolib/container/server/abstract_benchmark.py ml.fcnet_classification $@
```

## Collection

 - Name: [staeglis/HPOlib2](https://github.com/staeglis/HPOlib2)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

