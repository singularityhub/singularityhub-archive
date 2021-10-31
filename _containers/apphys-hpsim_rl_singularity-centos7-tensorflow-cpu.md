---
id: 5616
name: "apphys/hpsim_rl_singularity"
branch: "master"
tag: "centos7-tensorflow-cpu"
commit: "c4a049b7dc728756ae801d2914ee7ec2ff771bad"
version: "a5543c42edb1ce9ad717ae6e80768628"
build_date: "2018-11-16T01:38:15.810Z"
size_mb: 5083
size: 2386853919
sif: "https://datasets.datalad.org/shub/apphys/hpsim_rl_singularity/centos7-tensorflow-cpu/2018-11-16-c4a049b7-a5543c42/a5543c42edb1ce9ad717ae6e80768628.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/apphys/hpsim_rl_singularity/centos7-tensorflow-cpu/2018-11-16-c4a049b7-a5543c42/
recipe: https://datasets.datalad.org/shub/apphys/hpsim_rl_singularity/centos7-tensorflow-cpu/2018-11-16-c4a049b7-a5543c42/Singularity
collection: apphys/hpsim_rl_singularity
---

# apphys/hpsim_rl_singularity:centos7-tensorflow-cpu

```bash
$ singularity pull shub://apphys/hpsim_rl_singularity:centos7-tensorflow-cpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-centos7

%help
Centos7 with cuda9.0 cudnn7
ML/DL packages  : tensorflow keras sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm 
Development kit : g++/gcc cython nvcc libqt4-dev python-dev
Utility kit     : git wget emacs vim openssh-client

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

%labels
Maintainer coreyjadams
Version centos7-tf1.11.0-torch0.4.1

#------------
# Global installation
#------------
%environment
    
    # for system
    export CUDA_DEVICE_ORDER=PCI_BUS_ID


%post
    
    # yum basics
    yum update -y
    yum groupinstall -y "Development Tools"
    yum install -y epel-release
    yum install -y wget emacs vim 
    yum install -y PyQt4 PyQt4-devel
    yum install -y emacs vim openssh-clients zip 
    yum install -y python-devel python-pip  python-setuptools
    yum install -y hdf5
    yum install -y tkinter


    # pip basics
    pip --no-cache-dir --disable-pip-version-check install --upgrade setuptools 
    pip --no-cache-dir --disable-pip-version-check install 'matplotlib<3.0' # for python2.7
    pip --no-cache-dir --disable-pip-version-check install 'ipython<6.0'    # for python2.7
    pip --no-cache-dir --disable-pip-version-check install 'ipykernel<5.0'  # for python2.7
    pip --no-cache-dir --disable-pip-version-check install numpy wheel zmq six pygments pyyaml cython gputil psutil humanize h5py tqdm scipy seaborn tables
    pip --no-cache-dir --disable-pip-version-check install  pandas scikit-image scikit-learn Pillow opencv-python
    pip --no-cache-dir --disable-pip-version-check install jupyter notebook

    # tensorflow
    pip --no-cache-dir --disable-pip-version-check install --upgrade tensorflow==1.12.0
    pip --no-cache-dir --disable-pip-version-check install tensorboard

    # torch
    pip --no-cache-dir --disable-pip-version-check install torch==0.4.1
    pip --no-cache-dir --disable-pip-version-check install torchvision==0.2.1
```

## Collection

 - Name: [apphys/hpsim_rl_singularity](https://github.com/apphys/hpsim_rl_singularity)
 - License: None

