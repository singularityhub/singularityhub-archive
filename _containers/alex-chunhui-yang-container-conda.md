---
id: 14398
name: "alex-chunhui-yang/container"
branch: "master"
tag: "conda"
commit: "eca005665669ffe536a3076aa702ad2e4d6aceab"
version: "25d85d11999c3d2eea62da563f3b810e0882926623f111e357236a67a88fccad"
build_date: "2020-09-23T11:52:58.154Z"
size_mb: 5334.80078125
size: 5593944064
sif: "https://datasets.datalad.org/shub/alex-chunhui-yang/container/conda/2020-09-23-eca00566-25d85d11/25d85d11999c3d2eea62da563f3b810e0882926623f111e357236a67a88fccad.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/alex-chunhui-yang/container/conda/2020-09-23-eca00566-25d85d11/
recipe: https://datasets.datalad.org/shub/alex-chunhui-yang/container/conda/2020-09-23-eca00566-25d85d11/Singularity
collection: alex-chunhui-yang/container
---

# alex-chunhui-yang/container:conda

```bash
$ singularity pull shub://alex-chunhui-yang/container:conda
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
conda create --name tensorflow-env -y
chmod +x /opt/anaconda3/bin/activate
/opt/anaconda3/bin/activate tensorflow-env
conda install -c anaconda tensorflow-gpu  -y

%runscript
# executes with the singularity run command
# delete this section to use existing docker ENTRYPOINT command

%test
# test that script is a success
```

## Collection

 - Name: [alex-chunhui-yang/container](https://github.com/alex-chunhui-yang/container)
 - License: None

