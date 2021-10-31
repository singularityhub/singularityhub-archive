---
id: 5693
name: "TMCantwell/AENEAS-use-case-Image-based-Object-Detection-Classification"
branch: "master"
tag: "usecase4"
commit: "7b12732e3a5d17dec72a89d1bc54d67f66d5de19"
version: "f55b9e8c819895beec0d5b30720cec60"
build_date: "2019-04-02T15:49:00.332Z"
size_mb: 10048
size: 5107855391
sif: "https://datasets.datalad.org/shub/TMCantwell/AENEAS-use-case-Image-based-Object-Detection-Classification/usecase4/2019-04-02-7b12732e-f55b9e8c/f55b9e8c819895beec0d5b30720cec60.simg"
url: https://datasets.datalad.org/shub/TMCantwell/AENEAS-use-case-Image-based-Object-Detection-Classification/usecase4/2019-04-02-7b12732e-f55b9e8c/
recipe: https://datasets.datalad.org/shub/TMCantwell/AENEAS-use-case-Image-based-Object-Detection-Classification/usecase4/2019-04-02-7b12732e-f55b9e8c/Singularity
collection: TMCantwell/AENEAS-use-case-Image-based-Object-Detection-Classification
---

# TMCantwell/AENEAS-use-case-Image-based-Object-Detection-Classification:usecase4

```bash
$ singularity pull shub://TMCantwell/AENEAS-use-case-Image-based-Object-Detection-Classification:usecase4
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:10.0-cudnn7-devel-centos7

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
yum -y install epel-release
yum -y install cuda
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
git clone https://github.com/TMCantwell/keras-retinanet.git
cd keras-retinanet
pip install .
python setup.py build_ext --inplace
cd ..
pip install numpy
yum -y install opencv
yum -y install opencv-devel
yum -y install opencv-python
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
pip install astropy
yum -y install python36u-tkinter
wget https://github.com/fizyr/keras-retinanet/releases/download/0.2/resnet50_coco_best_v2.0.3.h5
mv resnet50_coco_best_v2.0.3.h5 /keras-retinanet/snapshots

%environment
alias start-tensorflow="source /tensorflow/bin/activate"


%runscript
echo "Starting Tensorflow virtual environment"
source /tensorflow/bin/activate
echo "Arguments received: $*"
exec python "$@"
```

## Collection

 - Name: [TMCantwell/AENEAS-use-case-Image-based-Object-Detection-Classification](https://github.com/TMCantwell/AENEAS-use-case-Image-based-Object-Detection-Classification)
 - License: None

