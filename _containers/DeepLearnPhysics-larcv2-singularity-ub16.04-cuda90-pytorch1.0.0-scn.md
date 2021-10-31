---
id: 8318
name: "DeepLearnPhysics/larcv2-singularity"
branch: "master"
tag: "ub16.04-cuda90-pytorch1.0.0-scn"
commit: "38ab6ef451a6392a9b04f3093ad6712bd989b900"
version: "bfe58a5206b78637847c6afbdc0a67c3"
build_date: "2019-04-10T11:51:45.694Z"
size_mb: 5358
size: 2702577695
sif: "https://datasets.datalad.org/shub/DeepLearnPhysics/larcv2-singularity/ub16.04-cuda90-pytorch1.0.0-scn/2019-04-10-38ab6ef4-bfe58a52/bfe58a5206b78637847c6afbdc0a67c3.simg"
url: https://datasets.datalad.org/shub/DeepLearnPhysics/larcv2-singularity/ub16.04-cuda90-pytorch1.0.0-scn/2019-04-10-38ab6ef4-bfe58a52/
recipe: https://datasets.datalad.org/shub/DeepLearnPhysics/larcv2-singularity/ub16.04-cuda90-pytorch1.0.0-scn/2019-04-10-38ab6ef4-bfe58a52/Singularity
collection: DeepLearnPhysics/larcv2-singularity
---

# DeepLearnPhysics/larcv2-singularity:ub16.04-cuda90-pytorch1.0.0-scn

```bash
$ singularity pull shub://DeepLearnPhysics/larcv2-singularity:ub16.04-cuda90-pytorch1.0.0-scn
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

%help
Ubuntu16.04 with cuda10.0 cudnn7
ML/DL packages  : pytorch (1.0.0=dev20181215) sc-learn
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
Version ub16.04-cuda100-pytorchdev20181215

#------------
# Global installation
#------------
%environment
    # for system
    export XDG_RUNTIME_DIR=/tmp/$USER
    export CUDA_DEVICE_ORDER=PCI_BUS_ID
    # for ROOT
    #export ROOTSYS=/usr/local/root
    #export PATH=${ROOTSYS}/bin:${PATH}
    #export LD_LIBRARY_PATH="${ROOTSYS}/lib:${LD_LIBRARY_PATH}"
    #export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}

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

# ROOT
#wget https://root.cern.ch/download/root_v6.14.04.Linux-ubuntu16-x86_64-gcc5.4.tar.gz 
#tar -xzf root_v6.14.04.Linux-ubuntu16-x86_64-gcc5.4.tar.gz 
#rm root_v6.14.04.Linux-ubuntu16-x86_64-gcc5.4.tar.gz 
#mv root /usr/local/root 
#export ROOTSYS=/usr/local/root 
#export PATH=${ROOTSYS}/bin:${PATH} 
#export LD_LIBRARY_PATH=${ROOTSYS}/lib:${LD_LIBRARY_PATH}
#export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}

# pip basics
pip --no-cache-dir --disable-pip-version-check install --upgrade pip==9.0.3 
pip --no-cache-dir --disable-pip-version-check install --upgrade
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

# larcv
mkdir -p /app

# pytorch
#pip --no-cache-dir --disable-pip-version-check install https://download.pytorch.org/whl/cu90/torch-1.0.1.post2-cp27-cp27mu-linux_x86_64.whl
pip --no-cache-dir --disable-pip-version-check install torch torchvision

#pip --no-cache-dir --disable-pip-version-check install https://download.pytorch.org/whl/cu100/torch-1.0.1.post2-cp27-cp27mu-linux_x86_64.whl
#pip --no-cache-dir --disable-pip-version-check install torchvision

# scn
#pip --no-cache-dir --disable-pip-version-check install --extra-index-url https://test.pypi.org/simple scn-cuda10=="0.2.2018.1218"
cd /app
git clone https://github.com/facebookresearch/SparseConvNet
cd SparseConvNet
git checkout dcd1428dcc769d175734260764eeadf160593335
python setup.py install
```

## Collection

 - Name: [DeepLearnPhysics/larcv2-singularity](https://github.com/DeepLearnPhysics/larcv2-singularity)
 - License: None

