---
id: 14884
name: "cyang31/containers"
branch: "master"
tag: "torch_mmf"
commit: "74cbf0facb92decbdd28f009ecf0119b82cec1dd"
version: "5560e7b835f52ffe72ce3d7dce64075dcad5b90391a75616dfecfc9d6642d73e"
build_date: "2021-03-24T03:07:33.505Z"
size_mb: 1950.5859375
size: 2045337600
sif: "https://datasets.datalad.org/shub/cyang31/containers/torch_mmf/2021-03-24-74cbf0fa-5560e7b8/5560e7b835f52ffe72ce3d7dce64075dcad5b90391a75616dfecfc9d6642d73e.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/cyang31/containers/torch_mmf/2021-03-24-74cbf0fa-5560e7b8/
recipe: https://datasets.datalad.org/shub/cyang31/containers/torch_mmf/2021-03-24-74cbf0fa-5560e7b8/Singularity
collection: cyang31/containers
---

# cyang31/containers:torch_mmf

```bash
$ singularity pull shub://cyang31/containers:torch_mmf
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: anibali/pytorch:1.4.0-cuda10.1-ubuntu16.04

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
rm -rf /home/user/miniconda
rm -rf /usr/local/lib/python3.5
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

%runscript
# executes with the singularity run command
# delete this section to use existing docker ENTRYPOINT command

%test
# test that script is a success
```

## Collection

 - Name: [cyang31/containers](https://github.com/cyang31/containers)
 - License: None

