---
id: 14409
name: "alex-chunhui-yang/container"
branch: "master"
tag: "centos_tf"
commit: "ca84fce7c68b4cf8be08d871ecd0ae0e46150f3f"
version: "5851adba515e6759d5a28fcffdcfebecbb0887c48a192541f438eb0e0d0bfcd5"
build_date: "2020-09-23T16:40:26.219Z"
size_mb: 2758.52734375
size: 2892525568
sif: "https://datasets.datalad.org/shub/alex-chunhui-yang/container/centos_tf/2020-09-23-ca84fce7-5851adba/5851adba515e6759d5a28fcffdcfebecbb0887c48a192541f438eb0e0d0bfcd5.sif"
url: https://datasets.datalad.org/shub/alex-chunhui-yang/container/centos_tf/2020-09-23-ca84fce7-5851adba/
recipe: https://datasets.datalad.org/shub/alex-chunhui-yang/container/centos_tf/2020-09-23-ca84fce7-5851adba/Singularity
collection: alex-chunhui-yang/container
---

# alex-chunhui-yang/container:centos_tf

```bash
$ singularity pull shub://alex-chunhui-yang/container:centos_tf
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.1-cudnn8-runtime-centos7

%environment 
  SHELL=/bin/bash
  export SHELL
  export HDF5_USE_FILE_LOCKING='FALSE'
  export PATH=/usr/local/cuda/bin:$PATH
  export CPATH=/usr/local/cuda/include:$CPATH
  export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

%setup
# runs on host
# the path to the image is $SINGULARITY_ROOTFS

%post
# post-setup script

# load environment variables
. /environment

# use bash as default shell
echo 'SHELL=/bin/bash' >> /environment

# make environment file executable
chmod +x /environment

# default mount paths
mkdir /scratch

# fix this issue: https://github.com/singularityware/singularity/issues/1182#issuecomment-381796545
touch /usr/bin/nvidia-smi

yum -y update
yum -y install yum-utils
yum -y groupinstall development
yum -y install epel-release
yum -y install dnf
yum -y install https://repo.ius.io/ius-release-el7.rpm
yum -y install python36u
yum -y install python36u-devel
yum -y install python36u-pip
yum -y install gcc gcc-c++ numpy python-devel scipy
#yum -y install python3-scikit-learn

pip3.6 install --upgrade pip	
#pip install tensorflow-gpu==2.1.0
pip install tf-nightly-gpu==2.4.0.dev20200923
pip install Pillow
pip install matplotlib
pip install tqdm
pip install h5py
pip install pandas
pip install simpleitk
pip install comet_ml
pip install pyyaml
pip install spektral

%runscript
# executes with the singularity run command
# delete this section to use existing docker ENTRYPOINT command

%test
# test that script is a success
```

## Collection

 - Name: [alex-chunhui-yang/container](https://github.com/alex-chunhui-yang/container)
 - License: None

