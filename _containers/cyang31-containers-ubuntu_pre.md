---
id: 14446
name: "cyang31/containers"
branch: "master"
tag: "ubuntu_pre"
commit: "8167c17776383a5fe0c1eb9651299f7ad2f23833"
version: "0be7cf2b4ed48401a313ce8a92534a43f5aa46dcddc8d4eb6b026b99dea86f68"
build_date: "2020-09-25T16:26:47.295Z"
size_mb: 3974.19140625
size: 4167241728
sif: "https://datasets.datalad.org/shub/cyang31/containers/ubuntu_pre/2020-09-25-8167c177-0be7cf2b/0be7cf2b4ed48401a313ce8a92534a43f5aa46dcddc8d4eb6b026b99dea86f68.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/cyang31/containers/ubuntu_pre/2020-09-25-8167c177-0be7cf2b/
recipe: https://datasets.datalad.org/shub/cyang31/containers/ubuntu_pre/2020-09-25-8167c177-0be7cf2b/Singularity
collection: cyang31/containers
---

# cyang31/containers:ubuntu_pre

```bash
$ singularity pull shub://cyang31/containers:ubuntu_pre
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.1-cudnn7-runtime-ubuntu16.04

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
apt-get update && apt-get -y install locales
locale-gen en_US.UTF-8
apt-get -y --force-yes install vim wget bzip2 git
apt-get -y install build-essential
wget https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
bash ./Anaconda3-5.2.0-Linux-x86_64.sh -b -p /opt/anaconda3
export PATH=$PATH:/opt/anaconda3/bin
conda create -n torch-env python=3.6
chmod +x /opt/anaconda3/bin/activate
/opt/anaconda3/bin/activate torch-env
conda update -n base conda
conda install numpy ninja pyyaml mkl mkl-include setuptools cmake cffi typing_extensions future six requests dataclasses
conda install -c pytorch magma-cuda101
pip install Pillow 
pip install matplotlib 
pip install tqdm 
pip install h5py
pip install pandas
pip install wrapt --upgrade --ignore-installed
pip install comet_ml
pip install pyyaml
pip install simpleitk

%runscript
# executes with the singularity run command
# delete this section to use existing docker ENTRYPOINT command
echo "Welcome to Singularity Container pytorch ubuntu 16.04"

%test
# test that script is a success
```

## Collection

 - Name: [cyang31/containers](https://github.com/cyang31/containers)
 - License: None

