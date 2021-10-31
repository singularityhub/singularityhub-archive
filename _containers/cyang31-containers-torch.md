---
id: 14891
name: "cyang31/containers"
branch: "master"
tag: "torch"
commit: "c692fb043c715b111d7dd8b3ddf4ad1996b451fa"
version: "762f75d92d76e0a886f52403ee0aa79eccb3fbe844b82c6ebd7255404c27ab76"
build_date: "2021-03-24T02:53:18.635Z"
size_mb: 2969.92578125
size: 3114192896
sif: "https://datasets.datalad.org/shub/cyang31/containers/torch/2021-03-24-c692fb04-762f75d9/762f75d92d76e0a886f52403ee0aa79eccb3fbe844b82c6ebd7255404c27ab76.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/cyang31/containers/torch/2021-03-24-c692fb04-762f75d9/
recipe: https://datasets.datalad.org/shub/cyang31/containers/torch/2021-03-24-c692fb04-762f75d9/Singularity
collection: cyang31/containers
---

# cyang31/containers:torch

```bash
$ singularity pull shub://cyang31/containers:torch
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.1-cudnn7-runtime-ubuntu16.04

%environment
# use bash as default shell
SHELL=/bin/bash
export SHELL
export HDF5_USE_FILE_LOCKING='FALSE'
export PATH=/usr/local/cuda/bin:$PATH
export CPATH=/usr/local/cuda/include:$CPATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
export HOME=/scratch/alexyang

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

apt-get update && apt-get install -y apt-utils
apt-get update && apt-get install -y locales
locale-gen en_US.UTF-8
apt-get install -y git wget

apt-get install -y software-properties-common
add-apt-repository ppa:deadsnakes/ppa 
apt-get update
apt-get install -y python3.7-dev
#apt-get install -y python3-pip
wget https://bootstrap.pypa.io/get-pip.py
python3.7 get-pip.py
apt-get install -y build-essential 
apt-get install -y vim
# scikit, scipy
# apt-get install -y python3-sklearn python3-sklearn-lib
apt-get clean

pip3 install --upgrade pip
pip install Pillow
pip install matplotlib
pip install tqdm
pip install h5py
pip install pandas
pip install comet_ml

# sklearn from source
git clone git://github.com/scikit-learn/scikit-learn.git
cd scikit-learn
pip install cython
pip install --verbose --editable .

pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html

cd ..
git clone https://github.com/facebookresearch/mmf.git
cd mmf
pip install --editable .

cd ..
pip install git+https://github.com/aleju/imgaug.git

%runscript
# executes with the singularity run command
# delete this section to use existing docker ENTRYPOINT command

%test
# test that script is a success
```

## Collection

 - Name: [cyang31/containers](https://github.com/cyang31/containers)
 - License: None

