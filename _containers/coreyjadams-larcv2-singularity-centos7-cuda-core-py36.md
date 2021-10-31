---
id: 6520
name: "coreyjadams/larcv2-singularity"
branch: "centos"
tag: "centos7-cuda-core-py36"
commit: "2770ca0cbd7ba270e39a54a378ea6a06e433b8db"
version: "e1fa1971d9b7f99dedab43cacc4abaef"
build_date: "2019-01-24T23:41:06.099Z"
size_mb: 4615
size: 2350620703
sif: "https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-core-py36/2019-01-24-2770ca0c-e1fa1971/e1fa1971d9b7f99dedab43cacc4abaef.simg"
url: https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-core-py36/2019-01-24-2770ca0c-e1fa1971/
recipe: https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-core-py36/2019-01-24-2770ca0c-e1fa1971/Singularity
collection: coreyjadams/larcv2-singularity
---

# coreyjadams/larcv2-singularity:centos7-cuda-core-py36

```bash
$ singularity pull shub://coreyjadams/larcv2-singularity:centos7-cuda-core-py36
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-centos7

%help
Centos7 with cuda9.0 cudnn7, and basic development tools (python 3.6)
ML/DL packages  : sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm 
Development kit : g++/gcc cython nvcc python3-dev
Utility kit     : git wget emacs vim openssh-client

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

%labels
Maintainer coreyjadams
Version centos7-cuda-core-py36

#------------
# Global installation
#------------
%environment
    
    # for system
    export CUDA_DEVICE_ORDER=PCI_BUS_ID

    # Add cupti to the path for profiling:
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64

    source scl_source enable devtoolset-4
    source scl_source enable rh-python36


%post
    
    # yum basics
    yum update -y
    yum groupinstall -y "Development Tools"
    # Install gcc, python36,etc:
    yum install -y centos-release-scl
    yum install -y epel-release
    yum install -y devtoolset-4

    # Python36
    yum install -y rh-python36-python-devel rh-python36-python-pip rh-python36-python-setuptools


    # Common development tools:
    yum install -y wget emacs vim cmake3
    yum install -y emacs vim openssh-clients zip 
    yum install -y hdf5

    # pip basics
    # Need to enable pip3 with scl
    scl enable rh-python36 bash

    pip3 --no-cache-dir --disable-pip-version-check install --upgrade setuptools 
    pip3 --no-cache-dir --disable-pip-version-check install future
    pip3 --no-cache-dir --disable-pip-version-check install 'matplotlib' 
    pip3 --no-cache-dir --disable-pip-version-check install 'ipython'    
    pip3 --no-cache-dir --disable-pip-version-check install 'ipykernel'  
    pip3 --no-cache-dir --disable-pip-version-check install numpy wheel zmq six pygments pyyaml cython gputil psutil humanize h5py tqdm scipy seaborn tables
    pip3 --no-cache-dir --disable-pip-version-check install  pandas scikit-image scikit-learn Pillow opencv-python
    pip3 --no-cache-dir --disable-pip-version-check install jupyter notebook
```

## Collection

 - Name: [coreyjadams/larcv2-singularity](https://github.com/coreyjadams/larcv2-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

