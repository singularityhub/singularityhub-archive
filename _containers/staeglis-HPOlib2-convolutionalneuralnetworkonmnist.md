---
id: 5844
name: "staeglis/HPOlib2"
branch: "container"
tag: "convolutionalneuralnetworkonmnist"
commit: "0fa42062f648ae34eead6ddab863adae463a8bde"
version: "a7603e6c8336bc76bc51a552d7885473"
build_date: "2019-03-15T14:57:58.473Z"
size_mb: 5413
size: 3308302367
sif: "https://datasets.datalad.org/shub/staeglis/HPOlib2/convolutionalneuralnetworkonmnist/2019-03-15-0fa42062-a7603e6c/a7603e6c8336bc76bc51a552d7885473.simg"
url: https://datasets.datalad.org/shub/staeglis/HPOlib2/convolutionalneuralnetworkonmnist/2019-03-15-0fa42062-a7603e6c/
recipe: https://datasets.datalad.org/shub/staeglis/HPOlib2/convolutionalneuralnetworkonmnist/2019-03-15-0fa42062-a7603e6c/Singularity
collection: staeglis/HPOlib2
---

# staeglis/HPOlib2:convolutionalneuralnetworkonmnist

```bash
$ singularity pull shub://staeglis/HPOlib2:convolutionalneuralnetworkonmnist
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

%environment
    export CUDA_ROOT=/usr/local/cuda 
    export LD_LIBRARY_PATH=${CUDA_ROOT}/lib64:$LD_LIBRARY_PATH 
    export LIBRARY_PATH=${CUDA_ROOT}/lib64:$LIBRARY_PATH
    PATH=${CUDA_ROOT}/bin:${PATH}
    export PATH

%runscript
    python3 -s /usr/local/lib/python3.6/dist-packages/hpolib/container/server/abstract_benchmark.py ml.conv_net $@
```

## Collection

 - Name: [staeglis/HPOlib2](https://github.com/staeglis/HPOlib2)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

