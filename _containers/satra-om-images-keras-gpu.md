---
id: 423
name: "satra/om-images"
branch: "keras-gpu"
tag: "keras-gpu"
commit: "e4871c3694fc5ad76efb3a08f8aed1201661317f"
version: "e195e797f84ec0159d26b23257c6b1da"
build_date: "2019-07-31T07:07:05.691Z"
size_mb: 3446
size: 1562221744
sif: "https://datasets.datalad.org/shub/satra/om-images/keras-gpu/2019-07-31-e4871c36-e195e797/e195e797f84ec0159d26b23257c6b1da.img.gz"
datalad_url: https://datasets.datalad.org?dir=/shub/satra/om-images/keras-gpu/2019-07-31-e4871c36-e195e797/
recipe: https://datasets.datalad.org/shub/satra/om-images/keras-gpu/2019-07-31-e4871c36-e195e797/Singularity
collection: satra/om-images
---

# satra/om-images:keras-gpu

```bash
$ singularity pull shub://satra/om-images:keras-gpu
```

## Singularity Recipe

```singularity
# To modify this file for your own system, use nvidia-smi
# to check your driver version and adjust the variable
# NV_DRIVER_VERSION below.
# Check sections <---- EDIT:

BootStrap: docker
From: tensorflow/tensorflow:1.1.0-rc1-gpu-py3

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
    pip install keras
    pip install nibabel
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

%test
    # Ensure that TensorFlow can be imported
    /usr/bin/python -c "import tensorflow as tf"
    # Ensure that keras can be imported
    /usr/bin/python -c "from keras.models import Sequential"
    # Ensure that nibabel can be imported
    /usr/bin/python -c "import nibabel as nb"
```

## Collection

 - Name: [satra/om-images](https://github.com/satra/om-images)
 - License: None

