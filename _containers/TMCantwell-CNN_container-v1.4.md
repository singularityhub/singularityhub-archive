---
id: 4218
name: "TMCantwell/CNN_container"
branch: "master"
tag: "v1.4"
commit: "e4a575c01dede51828221db3277021ce855d24f7"
version: "081c2f0849ace8fbe650749f6e078e5b"
build_date: "2018-08-28T16:37:57.475Z"
size_mb: 10252
size: 6688641055
sif: "https://datasets.datalad.org/shub/TMCantwell/CNN_container/v1.4/2018-08-28-e4a575c0-081c2f08/081c2f0849ace8fbe650749f6e078e5b.simg"
url: https://datasets.datalad.org/shub/TMCantwell/CNN_container/v1.4/2018-08-28-e4a575c0-081c2f08/
recipe: https://datasets.datalad.org/shub/TMCantwell/CNN_container/v1.4/2018-08-28-e4a575c0-081c2f08/Singularity
collection: TMCantwell/CNN_container
---

# TMCantwell/CNN_container:v1.4

```bash
$ singularity pull shub://TMCantwell/CNN_container:v1.4
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
#yum -y install kernel-devel-3.10.0-693.21.1.el7.x86_64 kernel-headers-3.10.0-693.21.1.el7.x86_64
wget https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda-repo-rhel7-9-0-local-9.0.176-1.x86_64-rpm
mv cuda-repo-rhel7-9-0-local-9.0.176-1.x86_64-rpm cuda-repo-rhel7-9-0-local-9.0.176-1.x86_64-rpm.rpm
rpm -i cuda-repo-rhel7-9-0-local-9.0.176-1.x86_64-rpm.rpm
yum clean expire-cache
yum -y install cuda
export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64
curl -O http://developer.download.nvidia.com/compute/redist/cudnn/v7.0.5/cudnn-9.0-linux-x64-v7.tgz
tar -zxf cudnn-9.0-linux-x64-v7.tgz 
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
pip3 install tensorflow-gpu
deactivate
yum -y install hdf5
yum -y install hdf5-devel
yum -y install h5py
yum -y install graphviz
source /tensorflow/bin/activate
pip install keras
git clone https://github.com/fizyr/keras-retinanet.git
cd keras-retinanet
pip install .
cd ..
pip install numpy
pip install opencv-python
pip install matplotlib
pip install pillow
pip install h5py
pip install cython
pip install jupyter
yum -y install python36u-tkinter
wget https://github.com/fizyr/keras-retinanet/releases/download/0.2/resnet50_coco_best_v2.0.3.h5
mv resnet50_coco_best_v2.0.3.h5 /keras-retinanet/snapshots

%environment
export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64
export LD_LIBRARY_PATH=/usr/local/cuda/lib64/:$LD_LIBRARY_PATH
export LIBRARY_PATH=/usr/local/cuda/lib64/:$LIBRARY_PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64
export CUDA_HOME=/usr/local/cuda-9.0
alias start-tensorflow="source /tensorflow/bin/activate"


%runscript
echo "Starting Tensorflow virtual environment"
source /tensorflow/bin/activate
echo "Arguments received: $*"
exec python "$@"
```

## Collection

 - Name: [TMCantwell/CNN_container](https://github.com/TMCantwell/CNN_container)
 - License: None

