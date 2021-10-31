---
id: 3238
name: "jmhays/brer-singularity"
branch: "master"
tag: "latest"
commit: "d4e302c8677276787be821fdeed4b6e0736dba9e"
version: "9a2f2957d74c07c4278c162b28fc2f62"
build_date: "2018-06-27T21:48:06.617Z"
size_mb: 2844
size: 1462767647
sif: "https://datasets.datalad.org/shub/jmhays/brer-singularity/latest/2018-06-27-d4e302c8-9a2f2957/9a2f2957d74c07c4278c162b28fc2f62.simg"
url: https://datasets.datalad.org/shub/jmhays/brer-singularity/latest/2018-06-27-d4e302c8-9a2f2957/
recipe: https://datasets.datalad.org/shub/jmhays/brer-singularity/latest/2018-06-27-d4e302c8-9a2f2957/Singularity
collection: jmhays/brer-singularity
---

# jmhays/brer-singularity:latest

```bash
$ singularity pull shub://jmhays/brer-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:8.0-devel-ubuntu16.04

%environment

# use bash as default shell
SHELL=/bin/bash

# add CUDA paths
CPATH="/usr/local/cuda/include:$CPATH"
PATH="/usr/local/gromacs/bin:/usr/local/cuda/bin:$PATH"
LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"
CUDA_HOME="/usr/local/cuda"

# # add Anaconda path
# PATH="/usr/local/anaconda3/bin:$PATH"

export PATH LD_LIBRARY_PATH CPATH CUDA_HOME
export PYTHONPATH="/build/sample_restraint/build/src/pythonmodule:\
/build/gmxapi/build:${PYTHONPATH}"

%setup
# runs on host
# the path to the image is $SINGULARITY_ROOTFS

%post
# post-setup script

# load environment variables
. /environment

# use bash as default shell
echo "\n #Using bash as default shell \n" >> /environment
echo 'SHELL=/bin/bash' >> /environment

# make environment file executable
chmod +x /environment

# default mount paths
echo "Default mount paths are /scratch and /data \n" >> /environment
mkdir /scratch /data

#Add CUDA paths
echo "\n #Cuda paths \n" >> /environment
echo 'export CPATH="/usr/local/cuda/include:$CPATH"' >> /environment
echo 'export PATH="/usr/local/cuda/bin:$PATH"' >> /environment
echo 'export LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"' >> /environment
echo 'export CUDA_HOME="/usr/local/cuda"' >> /environment

# updating and getting required packages
apt-get update
apt-get install -y wget git vim build-essential cmake libopenmpi-dev python3-pip

# Set up python3
pip3 install cmake networkx setuptools numpy scipy mpi4py

# Build the things you need
mkdir build
cd build

# gromacs-gmxapi
git clone https://github.com/kassonlab/gromacs-gmxapi.git
cd gromacs-gmxapi
git checkout devel
mkdir build; cd build
cmake ../ -DGMX_THREAD_MPI=ON -DGMX_GPU=ON -DGMX_BUILD_OWN_FFTW=ON -DGMX_USE_NVML=OFF
make -j8; make install
cd /build
#
# # gmxapi
git clone https://github.com/kassonlab/gmxapi.git
cd gmxapi
git checkout devel
mkdir build; cd build
cmake ../ -Dgmxapi_DIR="/usr/local/gromacs/share/cmake/gmxapi"
make -j8; make install
cd /build
#
# sample_restraint
git clone https://github.com/jmhays/sample_restraint.git
cd sample_restraint
git checkout devel
mkdir build; cd build
cmake ../ -Dgmxapi_DIR="/usr/local/gromacs/share/cmake/gmxapi" -DGROMACS_DIR="/usr/local/gromacs/share/cmake/gromacs"
make -j8

%runscript
# executes with the singularity run command
# delete this section to use existing docker ENTRYPOINT command

%test
# test that script is a success
```

## Collection

 - Name: [jmhays/brer-singularity](https://github.com/jmhays/brer-singularity)
 - License: None

