---
id: 422
name: "satra/om-images"
branch: "torch-gpu"
tag: "torch-gpu"
commit: "e4fd09dbcb9f2bd5b5789d0ef3ee975924155967"
version: "1837ea95c56bc0ea983c7697c30a22fb"
build_date: "2017-10-19T17:45:42.820Z"
size_mb: 9813
size: 3296556875
sif: "https://datasets.datalad.org/shub/satra/om-images/torch-gpu/2017-10-19-e4fd09db-1837ea95/1837ea95c56bc0ea983c7697c30a22fb.img.gz"
url: https://datasets.datalad.org/shub/satra/om-images/torch-gpu/2017-10-19-e4fd09db-1837ea95/
recipe: https://datasets.datalad.org/shub/satra/om-images/torch-gpu/2017-10-19-e4fd09db-1837ea95/Singularity
collection: satra/om-images
---

# satra/om-images:torch-gpu

```bash
$ singularity pull shub://satra/om-images:torch-gpu
```

## Singularity Recipe

```singularity
# To modify this file for your own system, use nvidia-smi
# to check your driver version and adjust the variable
# NV_DRIVER_VERSION below.
# Check sections <---- EDIT:

BootStrap: docker
From: bethgelab/jupyter-torch:cuda8.0-cudnn5

%runscript
    # When executed, the container will run Python
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
```

## Collection

 - Name: [satra/om-images](https://github.com/satra/om-images)
 - License: None

