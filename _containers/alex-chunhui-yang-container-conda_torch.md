---
id: 14399
name: "alex-chunhui-yang/container"
branch: "master"
tag: "conda_torch"
commit: "806d7be8db5212f733cc563127b710ccc27fe308"
version: "cde5a32ffb8804099c118584a5d559909ea78cc9fa628a3caa52d5b807874e90"
build_date: "2020-09-25T03:44:49.692Z"
size_mb: 3921.28515625
size: 4111765504
sif: "https://datasets.datalad.org/shub/alex-chunhui-yang/container/conda_torch/2020-09-25-806d7be8-cde5a32f/cde5a32ffb8804099c118584a5d559909ea78cc9fa628a3caa52d5b807874e90.sif"
url: https://datasets.datalad.org/shub/alex-chunhui-yang/container/conda_torch/2020-09-25-806d7be8-cde5a32f/
recipe: https://datasets.datalad.org/shub/alex-chunhui-yang/container/conda_torch/2020-09-25-806d7be8-cde5a32f/Singularity
collection: alex-chunhui-yang/container
---

# alex-chunhui-yang/container:conda_torch

```bash
$ singularity pull shub://alex-chunhui-yang/container:conda_torch
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%environment
# use bash as default shell
SHELL=/bin/bash
export SHELL
export HDF5_USE_FILE_LOCKING='FALSE'
export PATH=/usr/local/cuda/bin:$PATH
export CPATH=/usr/local/cuda/include:$CPATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
export PATH=$PATH:/opt/anaconda3/bin

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

apt-get update && apt-get -y install locales
locale-gen en_US.UTF-8
apt-get -y --force-yes install vim wget bzip2

# install anaconda
# PREFIX=/opt/anaconda3
wget https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
bash ./Anaconda3-5.2.0-Linux-x86_64.sh -b -p /opt/anaconda3
export PATH=$PATH:/opt/anaconda3/bin

# setup tensorflow environment
# /opt/anaconda3/envs/tensorflow-env
conda create --name torch-env -y
chmod +x /opt/anaconda3/bin/activate
/opt/anaconda3/bin/activate torch-env
conda install pytorch==1.2.0 torchvision==0.4.0 cudatoolkit=10.0 -c pytorch

%runscript
# executes with the singularity run command
# delete this section to use existing docker ENTRYPOINT command

%test
# test that script is a success
```

## Collection

 - Name: [alex-chunhui-yang/container](https://github.com/alex-chunhui-yang/container)
 - License: None

