---
id: 2436
name: "TMCantwell/CNN_container"
branch: "master"
tag: "v1.0"
commit: "a25c8e7914131f0343ea7dfeb89fe265f446c0d1"
version: "fcb1ba6ba309febf2780b11f536b3de7"
build_date: "2018-04-06T14:51:53.990Z"
size_mb: 10644
size: 6853599263
sif: "https://datasets.datalad.org/shub/TMCantwell/CNN_container/v1.0/2018-04-06-a25c8e79-fcb1ba6b/fcb1ba6ba309febf2780b11f536b3de7.simg"
url: https://datasets.datalad.org/shub/TMCantwell/CNN_container/v1.0/2018-04-06-a25c8e79-fcb1ba6b/
recipe: https://datasets.datalad.org/shub/TMCantwell/CNN_container/v1.0/2018-04-06-a25c8e79-fcb1ba6b/Singularity
collection: TMCantwell/CNN_container
---

# TMCantwell/CNN_container:v1.0

```bash
$ singularity pull shub://TMCantwell/CNN_container:v1.0
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum wget

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
yum -y install kernel-devel-3.10.0-693.21.1.el7.x86_64 kernel-headers-3.10.0-693.21.1.el7.x86_64
wget https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda-repo-rhel7-9-0-local-9.0.176-1.x86_64-rpm
mv cuda-repo-rhel7-9-0-local-9.0.176-1.x86_64-rpm cuda-repo-rhel7-9-0-local-9.0.176-1.x86_64-rpm.rpm
rpm -i cuda-repo-rhel7-9-0-local-9.0.176-1.x86_64-rpm.rpm
yum clean expire-cache
yum -y install cuda
export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64
curl -O http://developer.download.nvidia.com/compute/redist/cudnn/v7.1.2/cudnn-9.0-linux-x64-v7.1.tgz
tar -zxf cudnn-9.0-linux-x64-v7.1.tgz 
cd cuda
cp -av lib64/* /usr/local/cuda/lib64/
cp -av include/* /usr/local/cuda/include/
cd ..
export LD_LIBRARY_PATH=/usr/local/cuda/lib64/:$LD_LIBRARY_PATH
export LIBRARY_PATH=/usr/local/cuda/lib64/:$LIBRARY_PATH
yum -y install cuda-command-line-tools-9-0
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64
yum -y install epel-release
pip3.6 install -U virtualenv
virtualenv --system-site-packages /tensorflow
virtualenv --system-site-packages -p python3.6 /tensorflow
source /tensorflow/bin/activate
easy_install -U pip
pip3 install --upgrade tensorflow-gpu
deactivate
yum -y install hdf5
yum -y install hdf5-devel
yum -y install h5py
yum -y install graphviz
source /tensorflow/bin/activate
pip install keras
git clone https://github.com/fizyr/keras-retinanet.git
pip install numpy
pip install opencv-python
pip install matplotlib
pip install pillow
pip install h5py
pip install cython
pip install jupyter
yum -y install python36u-tkinter
wget https://github.com/fizyr/keras-retinanet/releases/download/0.2/resnet50_coco_best_v2.0.2.h5
mv resnet50_coco_best_v2.0.2.h5 /keras-retinanet/snapshots

%environment
export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
export PATH=/keras-retinanet:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64
export LD_LIBRARY_PATH=/usr/local/cuda/lib64/:$LD_LIBRARY_PATH
export LIBRARY_PATH=/usr/local/cuda/lib64/:$LIBRARY_PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64
alias start-tensorflow="source /tensorflow/bin/activate"
```

## Collection

 - Name: [TMCantwell/CNN_container](https://github.com/TMCantwell/CNN_container)
 - License: None

