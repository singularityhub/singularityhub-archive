---
id: 7842
name: "JBCA-MachineLearning/GPUs"
branch: "master"
tag: "cuda10"
commit: "a00df5da1d3d8e8c1dd853be8a84957259842871"
version: "3dcfdfd6927cebada88060e6d63da539"
build_date: "2019-10-09T14:50:44.021Z"
size_mb: 8458
size: 4196528159
sif: "https://datasets.datalad.org/shub/JBCA-MachineLearning/GPUs/cuda10/2019-10-09-a00df5da-3dcfdfd6/3dcfdfd6927cebada88060e6d63da539.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/JBCA-MachineLearning/GPUs/cuda10/2019-10-09-a00df5da-3dcfdfd6/
recipe: https://datasets.datalad.org/shub/JBCA-MachineLearning/GPUs/cuda10/2019-10-09-a00df5da-3dcfdfd6/Singularity
collection: JBCA-MachineLearning/GPUs
---

# JBCA-MachineLearning/GPUs:cuda10

```bash
$ singularity pull shub://JBCA-MachineLearning/GPUs:cuda10
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
yum -y install cuda
yum clean expire-cache
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
alias start-tensorflow="source /tensorflow/bin/activate"


%runscript
echo "Starting Tensorflow virtual environment"
source /tensorflow/bin/activate
echo "Arguments received: $*"
exec python "$@"
```

## Collection

 - Name: [JBCA-MachineLearning/GPUs](https://github.com/JBCA-MachineLearning/GPUs)
 - License: None

