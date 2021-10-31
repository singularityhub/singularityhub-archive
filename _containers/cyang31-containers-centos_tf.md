---
id: 14408
name: "cyang31/containers"
branch: "master"
tag: "centos_tf"
commit: "fa8ac58c25004e85b61ff00fc35636791298fc5e"
version: "cd7f668ae55fa622f93cb76f190d5e733a62cd268a81e01fad566771c0b5b273"
build_date: "2020-09-28T18:28:55.656Z"
size_mb: 3204.46484375
size: 3360124928
sif: "https://datasets.datalad.org/shub/cyang31/containers/centos_tf/2020-09-28-fa8ac58c-cd7f668a/cd7f668ae55fa622f93cb76f190d5e733a62cd268a81e01fad566771c0b5b273.sif"
url: https://datasets.datalad.org/shub/cyang31/containers/centos_tf/2020-09-28-fa8ac58c-cd7f668a/
recipe: https://datasets.datalad.org/shub/cyang31/containers/centos_tf/2020-09-28-fa8ac58c-cd7f668a/Singularity
collection: cyang31/containers
---

# cyang31/containers:centos_tf

```bash
$ singularity pull shub://cyang31/containers:centos_tf
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:11.0-cudnn8-runtime-centos7

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
pip3.6 install tf-nightly-gpu
pip3.6 install Pillow
pip3.6 install matplotlib
pip3.6 install tqdm
pip3.6 install h5py
pip3.6 install pandas
pip3.6 install simpleitk
pip3.6 install comet_ml
pip3.6 install pyyaml
pip3.6 install spektral

%runscript
# executes with the singularity run command
# delete this section to use existing docker ENTRYPOINT command

%test
# test that script is a success
```

## Collection

 - Name: [cyang31/containers](https://github.com/cyang31/containers)
 - License: None

