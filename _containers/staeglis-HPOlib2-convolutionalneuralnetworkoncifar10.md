---
id: 7869
name: "staeglis/HPOlib2"
branch: "container"
tag: "convolutionalneuralnetworkoncifar10"
commit: "753a663c08c07715673256b3efda21fb841cb1f2"
version: "b59a5fddef2939fbe14945b014c10eaa"
build_date: "2021-03-01T15:17:47.907Z"
size_mb: 5753
size: 3648921631
sif: "https://datasets.datalad.org/shub/staeglis/HPOlib2/convolutionalneuralnetworkoncifar10/2021-03-01-753a663c-b59a5fdd/b59a5fddef2939fbe14945b014c10eaa.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/staeglis/HPOlib2/convolutionalneuralnetworkoncifar10/2021-03-01-753a663c-b59a5fdd/
recipe: https://datasets.datalad.org/shub/staeglis/HPOlib2/convolutionalneuralnetworkoncifar10/2021-03-01-753a663c-b59a5fdd/Singularity
collection: staeglis/HPOlib2
---

# staeglis/HPOlib2:convolutionalneuralnetworkoncifar10

```bash
$ singularity pull shub://staeglis/HPOlib2:convolutionalneuralnetworkoncifar10
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

%labels
MAINTAINER Stefan Staeglich

%post
    apt update -y
    apt install git -y
    apt install python3-pip python-configparser cython3 -y
    pip3 install numpy scipy sklearn
    pip3 install git+https://github.com/automl/ConfigSpace.git@master
    pip3 install git+https://github.com/staeglis/HPOlib2@container
    pip3 install pyro4
    pip3 install https://download.pytorch.org/whl/cu100/torch-1.0.1.post2-cp36-cp36m-linux_x86_64.whl
    pip3 install torchvision

    mkdir /var/lib/hpolib/
    python3 /usr/local/lib/python3.6/dist-packages/hpolib/container/util/download_data.py ml.conv_net ConvolutionalNeuralNetworkOnCIFAR10
    chmod -R 777 /var/lib/hpolib/

%runscript
    python3 -s /usr/local/lib/python3.6/dist-packages/hpolib/container/server/abstract_benchmark.py ml.conv_net $@
```

## Collection

 - Name: [staeglis/HPOlib2](https://github.com/staeglis/HPOlib2)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

