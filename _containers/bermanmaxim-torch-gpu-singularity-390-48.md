---
id: 2604
name: "bermanmaxim/torch-gpu-singularity"
branch: "master"
tag: "390-48"
commit: "075fe4d42d6b8efd321811d93b4bc488a38f2ea2"
version: "5869900815d883e0a5fb29f55a7f191e"
build_date: "2018-04-20T11:21:32.387Z"
size_mb: 9529
size: 3100815391
sif: "https://datasets.datalad.org/shub/bermanmaxim/torch-gpu-singularity/390-48/2018-04-20-075fe4d4-58699008/5869900815d883e0a5fb29f55a7f191e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bermanmaxim/torch-gpu-singularity/390-48/2018-04-20-075fe4d4-58699008/
recipe: https://datasets.datalad.org/shub/bermanmaxim/torch-gpu-singularity/390-48/2018-04-20-075fe4d4-58699008/Singularity
collection: bermanmaxim/torch-gpu-singularity
---

# bermanmaxim/torch-gpu-singularity:390-48

```bash
$ singularity pull shub://bermanmaxim/torch-gpu-singularity:390-48
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
    
    NV_DRIVER_VERSION=390.48      # <---- EDIT: CHANGE THIS FOR YOUR SYSTEM
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
        ln -v -s $n ${n%.390.48}   # <---- EDIT: CHANGE THIS WITH DRIVER VERSION
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

 - Name: [bermanmaxim/torch-gpu-singularity](https://github.com/bermanmaxim/torch-gpu-singularity)
 - License: None

