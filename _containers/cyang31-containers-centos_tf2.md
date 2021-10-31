---
id: 14479
name: "cyang31/containers"
branch: "master"
tag: "centos_tf2"
commit: "5d18f1862a039f05efc855020668f6e5976c7d0f"
version: "142e1009a88844dfe0e5a0b449f7240e3c3c73265533fb2ac7e3e49569fd2894"
build_date: "2020-09-28T17:55:05.012Z"
size_mb: 2428.51171875
size: 2546479104
sif: "https://datasets.datalad.org/shub/cyang31/containers/centos_tf2/2020-09-28-5d18f186-142e1009/142e1009a88844dfe0e5a0b449f7240e3c3c73265533fb2ac7e3e49569fd2894.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/cyang31/containers/centos_tf2/2020-09-28-5d18f186-142e1009/
recipe: https://datasets.datalad.org/shub/cyang31/containers/centos_tf2/2020-09-28-5d18f186-142e1009/Singularity
collection: cyang31/containers
---

# cyang31/containers:centos_tf2

```bash
$ singularity pull shub://cyang31/containers:centos_tf2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.1-cudnn7-runtime-centos7

%environment 
  SHELL=/bin/bash
  export SHELL
  export HDF5_USE_FILE_LOCKING='FALSE'
  export PATH=/usr/local/cuda/bin:$PATH
  export CPATH=/usr/local/cuda/include:$CPATH
  export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda-10.2/lib64:$LD_LIBRARY_PATH

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
pip3.6 install tensorflow-gpu==2.3.0
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

