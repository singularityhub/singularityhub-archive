---
id: 7640
name: "TMCantwell/FAW"
branch: "master"
tag: "cuda9"
commit: "89277322a028fbb06e7955a280f610c483501b1b"
version: "6e01ffb25d6e23b0a423009a21191b02"
build_date: "2019-03-07T14:19:12.980Z"
size_mb: 9222
size: 4635861023
sif: "https://datasets.datalad.org/shub/TMCantwell/FAW/cuda9/2019-03-07-89277322-6e01ffb2/6e01ffb25d6e23b0a423009a21191b02.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TMCantwell/FAW/cuda9/2019-03-07-89277322-6e01ffb2/
recipe: https://datasets.datalad.org/shub/TMCantwell/FAW/cuda9/2019-03-07-89277322-6e01ffb2/Singularity
collection: TMCantwell/FAW
---

# TMCantwell/FAW:cuda9

```bash
$ singularity pull shub://TMCantwell/FAW:cuda9
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-centos7

%post
yum -y update
yum -y install yum-utils
yum -y groupinstall development
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum -y install nano
yum -y install build-essential curl git man vim autoconf libtool debootstrap squashfs-tools
yum -y install python36u
yum -y install python36u-pip
yum -y install python36u-devel
yum -y install opencv
yum -y install opencv-devel
yum -y install opencv-python
yum clean expire-cache
yum -y install cuda
#export PATH=/usr/local/cuda-10.1/bin${PATH:+:${PATH}}
#export LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64
#export LD_LIBRARY_PATH=/usr/local/cuda/lib64/:$LD_LIBRARY_PATH
#export LIBRARY_PATH=/usr/local/cuda/lib64/:$LIBRARY_PATH
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64
yum -y install epel-release
pip3.6 install -U virtualenv
virtualenv --system-site-packages /tensorflow
virtualenv --system-site-packages -p python3.6 /tensorflow
source /tensorflow/bin/activate
easy_install -U pip
pip3 install tensorflow-gpu==1.12.0
deactivate
yum -y install hdf5
yum -y install hdf5-devel
yum -y install h5py
yum -y install graphviz
source /tensorflow/bin/activate
pip install keras
pip install progressbar2
pip install numpy
pip install opencv-python
pip install Pillow
pip install matplotlib
pip install pillow
pip install h5py
pip install pandas
pip install matplotlib
pip install scikit-image
pip install scikit-learn
pip install scipy
pip install cython
pip install jupyter
pip install pandas
pip install git+https://github.com/qubvel/classification_models.git


%environment
#export PATH=/usr/local/cuda-10.1/bin${PATH:+:${PATH}}
#export LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64
#export LD_LIBRARY_PATH=/usr/local/cuda/lib64/:$LD_LIBRARY_PATH
#export LIBRARY_PATH=/usr/local/cuda/lib64/:$LIBRARY_PATH
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64
#export CUDA_HOME=/usr/local/cuda-10.1
alias start-tensorflow="source /tensorflow/bin/activate"


%runscript
echo "Starting Tensorflow virtual environment"
source /tensorflow/bin/activate
echo "Arguments received: $*"
exec python "$@"
```

## Collection

 - Name: [TMCantwell/FAW](https://github.com/TMCantwell/FAW)
 - License: None

