---
id: 425
name: "satra/om-tensorflow"
branch: "master"
tag: "master"
commit: "67c6be6d4ea7d84864dced2448649d1b9e506ce2"
version: "1f8e85586d2b73508b0dd868424a94ba"
build_date: "2017-10-19T18:03:08.226Z"
size_mb: 3173
size: 1480763217
sif: "https://datasets.datalad.org/shub/satra/om-tensorflow/master/2017-10-19-67c6be6d-1f8e8558/1f8e85586d2b73508b0dd868424a94ba.img.gz"
datalad_url: https://datasets.datalad.org?dir=/shub/satra/om-tensorflow/master/2017-10-19-67c6be6d-1f8e8558/
recipe: https://datasets.datalad.org/shub/satra/om-tensorflow/master/2017-10-19-67c6be6d-1f8e8558/Singularity
collection: satra/om-tensorflow
---

# satra/om-tensorflow:master

```bash
$ singularity pull shub://satra/om-tensorflow:master
```

## Singularity Recipe

```singularity
# To modify this file for your own system, use nvidia-smi
# to check your driver version and adjust the variable
# NV_DRIVER_VERSION below.
#
# Check sections <---- EDIT:

BootStrap: docker
From: tensorflow/tensorflow:1.0.0-gpu-py3
# <---- EDIT: ABOVE TO DETERMINE WHICH VERSION OF TENSORFLOW YOU WANT. do not put any comments on that line.

%runscript
    # When executed, the container will run Python with the TensorFlow module
    exec /usr/bin/python "$@"

%post
    # Set up some required environment defaults
    export LC_ALL=C
    export PATH=/bin:/sbin:/usr/bin:/usr/sbin:$PATH

    # add universe repo and install some packages
    sed -i '/xenial.*universe/s/^#//g' /etc/apt/sources.list
    locale-gen en_US.UTF-8
    apt-get -y update && apt-get -y install wget
    apt-get clean
    
    NV_DRIVER_VERSION=375.20      # <---- EDIT: CHANGE THIS FOR YOUR SYSTEM
    NV_DRIVER_FILE=NVIDIA-Linux-x86_64-${NV_DRIVER_VERSION}.run

    working_dir=$(pwd)
    # download and run NIH NVIDIA driver installer
    wget http://us.download.nvidia.com/XFree86/Linux-x86_64/${NV_DRIVER_VERSION}/NVIDIA-Linux-x86_64-${NV_DRIVER_VERSION}.run

    echo "Unpacking NVIDIA driver into container..."
    cd /usr/local/
    sh ${working_dir}/${NV_DRIVER_FILE} -x
    rm ${working_dir}/${NV_DRIVER_FILE}    
    mv NVIDIA-Linux-x86_64-${NV_DRIVER_VERSION} NVIDIA-Linux-x86_64
    cd NVIDIA-Linux-x86_64/
    for n in *.$NV_DRIVER_VERSION; do
        ln -v -s $n ${n%.375.20}   # <---- EDIT: CHANGE THIS IF DRIVER VERSION
    done
    ln -v -s libnvidia-ml.so.$NV_DRIVER_VERSION libnvidia-ml.so.1
    ln -v -s libcuda.so.$NV_DRIVER_VERSION libcuda.so.1
    cd $working_dir

    echo "Adding NVIDIA PATHs to /environment..."
    NV_DRIVER_PATH=/usr/local/NVIDIA-Linux-x86_64
    echo "

LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:$NV_DRIVER_PATH:\$LD_LIBRARY_PATH
PATH=$NV_DRIVER_PATH:\$PATH
export PATH LD_LIBRARY_PATH
    
" >> /environment   

    mkdir /om                      # <---- EDIT: SPECIFIC FILESYSTEM MOUNT
    mkdir /cm                      # <---- EDIT: SPECIFIC FILESYSTEM MOUNT
%test
    # Ensure that TensorFlow can be imported
    /usr/bin/python -c "import tensorflow as tf"
```

## Collection

 - Name: [satra/om-tensorflow](https://github.com/satra/om-tensorflow)
 - License: None

