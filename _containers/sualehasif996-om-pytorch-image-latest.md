---
id: 5651
name: "sualehasif996/om-pytorch-image"
branch: "torch-gpu"
tag: "latest"
commit: "f778eaa1256467f7f491a76f539436155469eaa3"
version: "ad52e9a69e257d15324a62a01e0b5490"
build_date: "2018-11-26T17:12:55.483Z"
size_mb: 11606
size: 4034715679
sif: "https://datasets.datalad.org/shub/sualehasif996/om-pytorch-image/latest/2018-11-26-f778eaa1-ad52e9a6/ad52e9a69e257d15324a62a01e0b5490.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sualehasif996/om-pytorch-image/latest/2018-11-26-f778eaa1-ad52e9a6/
recipe: https://datasets.datalad.org/shub/sualehasif996/om-pytorch-image/latest/2018-11-26-f778eaa1-ad52e9a6/Singularity
collection: sualehasif996/om-pytorch-image
---

# sualehasif996/om-pytorch-image:latest

```bash
$ singularity pull shub://sualehasif996/om-pytorch-image:latest
```

## Singularity Recipe

```singularity
# To modify this file for your own system, use nvidia-smi
# to check your driver version and adjust the variable
# NV_DRIVER_VERSION below.
# Check sections <---- EDIT:

BootStrap: docker
From: floydhub/pytorch:1.0.0-gpu.cuda9cudnn7-py3.37

%runscript
    # When executed, the container will run Torch
    exec /usr/local/torch/install/bin/th "$@"

%post
    apt-get update && apt-get -y install locales
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
PATH=/usr/local/torch/install/bin/:\$PATH
export PATH LD_LIBRARY_PATH
    
" >> /environment
```

## Collection

 - Name: [sualehasif996/om-pytorch-image](https://github.com/sualehasif996/om-pytorch-image)
 - License: None

