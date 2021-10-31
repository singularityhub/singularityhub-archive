---
id: 14345
name: "alex-chunhui-yang/container"
branch: "master"
tag: "torch2"
commit: "0d8ad7a2b946b5299f7dd98d40ee6d64bcd199da"
version: "8bd9b0552601d695aaa4de0e8c614bb3fc4ef9eefee405c5f62569c66796aa3a"
build_date: "2020-11-15T22:28:44.490Z"
size_mb: 2333.7265625
size: 2447089664
sif: "https://datasets.datalad.org/shub/alex-chunhui-yang/container/torch2/2020-11-15-0d8ad7a2-8bd9b055/8bd9b0552601d695aaa4de0e8c614bb3fc4ef9eefee405c5f62569c66796aa3a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/alex-chunhui-yang/container/torch2/2020-11-15-0d8ad7a2-8bd9b055/
recipe: https://datasets.datalad.org/shub/alex-chunhui-yang/container/torch2/2020-11-15-0d8ad7a2-8bd9b055/Singularity
collection: alex-chunhui-yang/container
---

# alex-chunhui-yang/container:torch2

```bash
$ singularity pull shub://alex-chunhui-yang/container:torch2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: pytorch/pytorch:1.2-cuda10.0-cudnn7-runtime

%environment
# use bash as default shell
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
apt-get install -y git wget
apt-get install -y software-properties-common
add-apt-repository ppa:deadsnakes/ppa
apt-get update
apt-get install -y python3.6-dev
wget https://bootstrap.pypa.io/get-pip.py
python3.6 get-pip.py

# scikit, scipy
apt-get install -y python3-scipy python3-sklearn python3-sklearn-lib
apt-get clean
# PIL (pillow for python 3)
pip install --upgrade pip
pip install Pillow
pip install matplotlib
pip install tqdm
pip install h5py
pip install pandas
pip install simpleitk
pip install comet_ml
#pip3 install torch-scatter==latest+cu101 -f https://pytorch-geometric.com/whl/torch-1.4.0.html
#pip3 install torch-sparse==latest+cu101 -f https://pytorch-geometric.com/whl/torch-1.4.0.html
#pip3 install torch-cluster==latest+cu101 -f https://pytorch-geometric.com/whl/torch-1.4.0.html
#pip3 install torch-spline-conv==latest+cu101 -f https://pytorch-geometric.com/whl/torch-1.4.0.html
#pip3 install torch-geometric

%runscript
# executes with the singularity run command
# delete this section to use existing docker ENTRYPOINT command

%test
# test that script is a success
```

## Collection

 - Name: [alex-chunhui-yang/container](https://github.com/alex-chunhui-yang/container)
 - License: None

