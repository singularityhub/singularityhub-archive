---
id: 7588
name: "TMCantwell/FAW"
branch: "master"
tag: "cuda101"
commit: "d50db85672551275f33334d31a610d82eade1dde"
version: "fd1ca6f582ca84c281961e3c43bb85cb"
build_date: "2020-08-05T13:01:00.499Z"
size_mb: 8427
size: 4169449503
sif: "https://datasets.datalad.org/shub/TMCantwell/FAW/cuda101/2020-08-05-d50db856-fd1ca6f5/fd1ca6f582ca84c281961e3c43bb85cb.simg"
url: https://datasets.datalad.org/shub/TMCantwell/FAW/cuda101/2020-08-05-d50db856-fd1ca6f5/
recipe: https://datasets.datalad.org/shub/TMCantwell/FAW/cuda101/2020-08-05-d50db856-fd1ca6f5/Singularity
collection: TMCantwell/FAW
---

# TMCantwell/FAW:cuda101

```bash
$ singularity pull shub://TMCantwell/FAW:cuda101
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:10.0-cudnn7-runtime-centos7

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
pip3 install tensorflow-gpu==1.13.1
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

