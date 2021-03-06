---
id: 8509
name: "DeepLearnPhysics/larcv2-singularity"
branch: "master"
tag: "hkmlworkshop"
commit: "548ae4d9bcc9e1e8b1b63fc178374b0e52af9335"
version: "714aad67ffd94e7a9160874b92aaf329"
build_date: "2019-04-19T22:33:47.274Z"
size_mb: 5329
size: 2696544287
sif: "https://datasets.datalad.org/shub/DeepLearnPhysics/larcv2-singularity/hkmlworkshop/2019-04-19-548ae4d9-714aad67/714aad67ffd94e7a9160874b92aaf329.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/DeepLearnPhysics/larcv2-singularity/hkmlworkshop/2019-04-19-548ae4d9-714aad67/
recipe: https://datasets.datalad.org/shub/DeepLearnPhysics/larcv2-singularity/hkmlworkshop/2019-04-19-548ae4d9-714aad67/Singularity
collection: DeepLearnPhysics/larcv2-singularity
---

# DeepLearnPhysics/larcv2-singularity:hkmlworkshop

```bash
$ singularity pull shub://DeepLearnPhysics/larcv2-singularity:hkmlworkshop
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

%help
Ubuntu16.04 with cuda9.0 cudnn7
ML/DL packages  : pytorch (1.0.0=dev20181015) sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python root root_numpy
                  plotly cufflinks osfclient
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm
Development kit : g++/gcc cython nvcc libqt4-dev python-dev
Utility kit     : git wget emacs vim openssh-client

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

%labels
Maintainer drinkingkazu
Version HKMLWorkshop

#------------
# Global installation
#------------
%environment
    # for system
    export XDG_RUNTIME_DIR=/tmp/$USER
    export CUDA_DEVICE_ORDER=PCI_BUS_ID
    # for ROOT
    export ROOTSYS=/usr/local/root
    export PATH=${ROOTSYS}/bin:${PATH}
    export LD_LIBRARY_PATH="${ROOTSYS}/lib:${LD_LIBRARY_PATH}"
    export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}
    export CUDA_DEVICE_ORDER=PCI_BUS_ID

%post
apt-get -y update
apt-get -y install zsh dpkg-dev g++ gcc binutils libqt4-dev git wget emacs vim openssh-client curl
apt-get -y install python-dev python-tk python-pip python-qt4 python-setuptools libsparsehash-dev python3-setuptools libhdf5-dev

# asciinema
apt-get install -y locales
locale-gen en_US.UTF-8
apt-get -y install software-properties-common python-software-properties
apt-add-repository -y ppa:zanchey/asciinema
apt-get -y update
apt-get -y install asciinema

# pip basics
pip --no-cache-dir --disable-pip-version-check install --upgrade pip==9.0.3 
pip --no-cache-dir --disable-pip-version-check install --upgrade setuptools 
pip --no-cache-dir --disable-pip-version-check install 'matplotlib<3.0' 
pip --no-cache-dir --disable-pip-version-check install 'ipython<6.0'    
pip --no-cache-dir --disable-pip-version-check install 'ipykernel<5.0'  
pip --no-cache-dir --disable-pip-version-check install future numpy wheel zmq six pygments pyyaml cython gputil psutil humanize 
pip --no-cache-dir --disable-pip-version-check install h5py tqdm scipy seaborn tables #root_numpy 
pip --no-cache-dir --disable-pip-version-check install pandas scikit-image scikit-learn Pillow opencv-python 
pip --no-cache-dir --disable-pip-version-check install jupyter notebook
pip --no-cache-dir --disable-pip-version-check install plotly cufflinks
pip --no-cache-dir --disable-pip-version-check install osfclient

pip --no-cache-dir --disable-pip-version-check install plotly cufflinks
pip --no-cache-dir --disable-pip-version-check install osfclient

# pytorch
pip --no-cache-dir --disable-pip-version-check install torch_nightly==1.0.0.dev20181015 -f https://download.pytorch.org/whl/nightly/cu90/torch_nightly.html
pip --no-cache-dir --disable-pip-version-check install torchvision
ldconfig /usr/local/cuda/lib64/stubs

# scn
pip --no-cache-dir --disable-pip-version-check install --extra-index-url https://test.pypi.org/simple scn-cuda9=="0.2.2018.1015"
```

## Collection

 - Name: [DeepLearnPhysics/larcv2-singularity](https://github.com/DeepLearnPhysics/larcv2-singularity)
 - License: None

