---
id: 14416
name: "alex-chunhui-yang/container"
branch: "master"
tag: "centos_torch2"
commit: "f2063940948b07a506858df3b26e9b58a6537fd7"
version: "f702ba9a6cd00d4bf52519477191f2c4956b4936078b0902b34012ad30b6cb0e"
build_date: "2020-11-15T22:27:27.108Z"
size_mb: 4790.94921875
size: 5023674368
sif: "https://datasets.datalad.org/shub/alex-chunhui-yang/container/centos_torch2/2020-11-15-f2063940-f702ba9a/f702ba9a6cd00d4bf52519477191f2c4956b4936078b0902b34012ad30b6cb0e.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/alex-chunhui-yang/container/centos_torch2/2020-11-15-f2063940-f702ba9a/
recipe: https://datasets.datalad.org/shub/alex-chunhui-yang/container/centos_torch2/2020-11-15-f2063940-f702ba9a/Singularity
collection: alex-chunhui-yang/container
---

# alex-chunhui-yang/container:centos_torch2

```bash
$ singularity pull shub://alex-chunhui-yang/container:centos_torch2
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
  export ANACONDA_HOME=/opt/anaconda3/:$ANACONDA_HOME
  
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
yum -y install git
yum -y install wget
yum -y install bzip2

wget https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
bash ./Anaconda3-5.2.0-Linux-x86_64.sh -b -p /opt/anaconda3
export PATH=$PATH:/opt/anaconda3/bin
# setup environment
conda create -n torch-env python=3.6 anaconda
source activate torch-env
conda -y install numpy ninja pyyaml mkl mkl-include setuptools cmake cffi typing_extensions future six requests dataclasses
conda -y install -c pytorch magma-cuda101
git clone --recursive https://github.com/pytorch/pytorch
cd pytorch
# if you are updating an existing checkout
git submodule sync
git submodule update --init --recursive
export CMAKE_PREFIX_PATH=${CONDA_PREFIX:-"$(dirname $(which conda))/../"}
python setup.py install

conda install Pillow 
conda install matplotlib 
conda install tqdm 
conda install h5py
conda install pandas
conda install simpleitk
conda install comet_ml
conda install pyyaml

pip install torch-scatter==latest+cu101 -f https://pytorch-geometric.com/whl/torch-1.4.0.html
pip install torch-sparse==latest+cu101 -f https://pytorch-geometric.com/whl/torch-1.4.0.html
pip install torch-cluster==latest+cu101 -f https://pytorch-geometric.com/whl/torch-1.4.0.html
pip install torch-spline-conv==latest+cu101 -f https://pytorch-geometric.com/whl/torch-1.4.0.html
pip install torch-geometric

%runscript
# executes with the singularity run command
# delete this section to use existing docker ENTRYPOINT command
exec source activate torch-env

%test
# test that script is a success
```

## Collection

 - Name: [alex-chunhui-yang/container](https://github.com/alex-chunhui-yang/container)
 - License: None

