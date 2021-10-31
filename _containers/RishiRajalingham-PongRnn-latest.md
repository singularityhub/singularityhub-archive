---
id: 10623
name: "RishiRajalingham/PongRnn"
branch: "master"
tag: "latest"
commit: "f05482b3432de5e5c916487ea57a77a3c2465d13"
version: "a9a9d5bb04cf450de9a1f6ddf2cbd921"
build_date: "2019-08-30T16:34:29.307Z"
size_mb: 3865.0
size: 1885241375
sif: "https://datasets.datalad.org/shub/RishiRajalingham/PongRnn/latest/2019-08-30-f05482b3-a9a9d5bb/a9a9d5bb04cf450de9a1f6ddf2cbd921.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/RishiRajalingham/PongRnn/latest/2019-08-30-f05482b3-a9a9d5bb/
recipe: https://datasets.datalad.org/shub/RishiRajalingham/PongRnn/latest/2019-08-30-f05482b3-a9a9d5bb/Singularity
collection: RishiRajalingham/PongRnn
---

# RishiRajalingham/PongRnn:latest

```bash
$ singularity pull shub://RishiRajalingham/PongRnn:latest
```

## Singularity Recipe

```singularity
# To modify this file for your own system, use nvidia-smi
# to check your driver version and adjust the variable
# NV_DRIVER_VERSION below.
# Check sections <---- EDIT:

BootStrap: docker
From: tensorflow/tensorflow:1.14.0-gpu-py3

%runscript
    # When executed, the container will run Python with the TensorFlow module
    exec /usr/local/bin/python "$@"

%post
    # Set up some required environment defaults
    export LC_ALL=C
    export PATH=/bin:/sbin:/usr/bin:/usr/sbin:$PATH

    # add universe repo and install some packages
    sed -i '/xenial.*universe/s/^#//g' /etc/apt/sources.list
    apt-get install -y locales
    # apt-get install python
    # added by rishi-r
    locale-gen en_US.UTF-8
    apt-get -y update && apt-get -y install wget
    apt-get clean

    mkdir /om

    NV_DRIVER_VERSION=410.93      # <---- EDIT: CHANGE THIS FOR YOUR SYSTEM
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
        ln -v -s $n ${n%.410.93}   # <---- EDIT: CHANGE THIS IF DRIVER VERSION
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

%test
    # Ensure that TensorFlow can be imported
    /usr/local/bin/python -c "import tensorflow as tf"
    #/usr/bin/python -c "import tensorflow as tf"
```

## Collection

 - Name: [RishiRajalingham/PongRnn](https://github.com/RishiRajalingham/PongRnn)
 - License: None

