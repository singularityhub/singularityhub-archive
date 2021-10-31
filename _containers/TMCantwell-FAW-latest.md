---
id: 7468
name: "TMCantwell/FAW"
branch: "master"
tag: "latest"
commit: "75e9174307c6629b30eb0e28758db8293573111d"
version: "7b56c15a44970224c582c2944693d010"
build_date: "2019-02-26T14:23:23.372Z"
size_mb: 10360
size: 6705696799
sif: "https://datasets.datalad.org/shub/TMCantwell/FAW/latest/2019-02-26-75e91743-7b56c15a/7b56c15a44970224c582c2944693d010.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TMCantwell/FAW/latest/2019-02-26-75e91743-7b56c15a/
recipe: https://datasets.datalad.org/shub/TMCantwell/FAW/latest/2019-02-26-75e91743-7b56c15a/Singularity
collection: TMCantwell/FAW
---

# TMCantwell/FAW:latest

```bash
$ singularity pull shub://TMCantwell/FAW:latest
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
yum -y install opencv
yum -y install opencv-devel
yum -y install opencv-python
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

 - Name: [TMCantwell/FAW](https://github.com/TMCantwell/FAW)
 - License: None

