---
id: 8265
name: "adityabalu/ros-sawyer-full-singularity"
branch: "master"
tag: "latest"
commit: "17a216b4c974dd6cc50205edd54b84cab400362e"
version: "90f2b824d352e2989542d15b3b97a1e2"
build_date: "2019-04-07T16:32:44.211Z"
size_mb: 3551
size: 1087746079
sif: "https://datasets.datalad.org/shub/adityabalu/ros-sawyer-full-singularity/latest/2019-04-07-17a216b4-90f2b824/90f2b824d352e2989542d15b3b97a1e2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/adityabalu/ros-sawyer-full-singularity/latest/2019-04-07-17a216b4-90f2b824/
recipe: https://datasets.datalad.org/shub/adityabalu/ros-sawyer-full-singularity/latest/2019-04-07-17a216b4-90f2b824/Singularity
collection: adityabalu/ros-sawyer-full-singularity
---

# adityabalu/ros-sawyer-full-singularity:latest

```bash
$ singularity pull shub://adityabalu/ros-sawyer-full-singularity:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
From: docker://kailiang/ros-sawyer-full-nvidia:Init
%labels

AUTHOR Aditya Balu baditya@iastate.edu

%environment
    CPATH="/usr/local/cuda/include:$CPATH"
    PATH="/usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}"
    LD_LIBRARY_PATH="/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/usr/local/cuda/lib64:${LD_LIBRARY_PATH}"
    CUDA_HOME="/usr/local/cuda"
    NVIDIA_VISIBLE_DEVICES=all
    NVIDIA_DRIVER_CAPABILITIES=compute,utility
    NVIDIA_REQUIRE_CUDA="cuda>=9.0"
    export PATH LD_LIBRARY_PATH CPATH CUDA_HOME

%post
    . /environment
    # use bash as default shell
    echo "\n #Using bash as default shell \n" >> /environment
    echo 'SHELL=/bin/bash' >> /environment

    # default mount paths
    mkdir /scratch /data 

    #Add CUDA paths
    echo "\n #Cuda paths \n" >> /environment
    echo 'export CPATH="/usr/local/cuda/include:$CPATH"' >> /environment
    echo 'export PATH="/usr/local/cuda/bin:$PATH"' >> /environment
    echo 'export LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"' >> /environment
    echo 'export CUDA_HOME="/usr/local/cuda"' >> /environment
    echo "/usr/local/cuda-9.0/lib64/" >/etc/ld.so.conf.d/cuda.conf
    echo "/usr/local/cuda/extras/CUPTI/lib64/" >>/etc/ld.so.conf.d/cuda.conf
    echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf
```

## Collection

 - Name: [adityabalu/ros-sawyer-full-singularity](https://github.com/adityabalu/ros-sawyer-full-singularity)
 - License: None

