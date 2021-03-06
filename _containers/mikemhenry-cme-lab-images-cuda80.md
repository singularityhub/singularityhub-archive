---
id: 3404
name: "mikemhenry/cme-lab-images"
branch: "master"
tag: "cuda80"
commit: "71b0b1f5a45583e80131bfc88d7e7d0f54fc762d"
version: "9658380e1387608908332eb1773eab24"
build_date: "2018-07-05T12:20:18.272Z"
size_mb: 1894
size: 1100005407
sif: "https://datasets.datalad.org/shub/mikemhenry/cme-lab-images/cuda80/2018-07-05-71b0b1f5-9658380e/9658380e1387608908332eb1773eab24.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mikemhenry/cme-lab-images/cuda80/2018-07-05-71b0b1f5-9658380e/
recipe: https://datasets.datalad.org/shub/mikemhenry/cme-lab-images/cuda80/2018-07-05-71b0b1f5-9658380e/Singularity
collection: mikemhenry/cme-lab-images
---

# mikemhenry/cme-lab-images:cuda80

```bash
$ singularity pull shub://mikemhenry/cme-lab-images:cuda80
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: shub://singularity-hub.org/mikemhenry/cme-lab-images:base

%help
Base cuda8 image used in CME-Lab workflows.

http://coen.boisestate.edu/cmelab/

%setup

%files

%labels
  Maintainer Mike Henry
  Maintaine_rEmail mikehenry@boisestate.edu
  Version v0.01

%environment

  PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}
  LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64

  # nvidia-container-runtime
  NVIDIA_VISIBLE_DEVICES=all
  NVIDIA_DRIVER_CAPABILITIES=compute,utility
  NVIDIA_REQUIRE_CUDA="cuda>=8.0"

  # devel envs
  LIBRARY_PATH=/usr/local/cuda/lib64/stubs


  export PATH LD_LIBRARY_PATH NVIDIA_VISIBLE_DEVICES NVIDIA_DRIVER_CAPABILITIES NVIDIA_REQUIRE_CUDA LIBRARY_PATH



%post
  # runtime https://gitlab.com/nvidia/cuda/blob/ubuntu16.04/8.0/runtime/Dockerfile
  export CUDA_VERSION=8.0.61
  export CUDA_PKG_VERSION=8-0=$CUDA_VERSION-1
  
  apt-get update && apt-get install -y --no-install-recommends ca-certificates apt-transport-https gnupg-curl
  rm -rf /var/lib/apt/lists/*
    
  NVIDIA_GPGKEY_SUM=d1be581509378368edeec8c1eb2958702feedf3bc3d17011adbf24efacce4ab5
  NVIDIA_GPGKEY_FPR=ae09fe4bbd223a84b2ccfce3f60f4b3d7fa2af80
  
  apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
  apt-key adv --export --no-emit-version -a $NVIDIA_GPGKEY_FPR | tail -n +5 > cudasign.pub
  echo "$NVIDIA_GPGKEY_SUM  cudasign.pub" | sha256sum -c --strict - && rm cudasign.pub 
  echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/cuda.list 
  echo "deb https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list

  apt-get update && apt-get install -y --no-install-recommends \
        cuda-nvrtc-$CUDA_PKG_VERSION \
        cuda-nvgraph-$CUDA_PKG_VERSION \
        cuda-cusolver-$CUDA_PKG_VERSION \
        cuda-cublas-8-0=8.0.61.2-1 \
        cuda-cufft-$CUDA_PKG_VERSION \
        cuda-curand-$CUDA_PKG_VERSION \
        cuda-cusparse-$CUDA_PKG_VERSION \
        cuda-npp-$CUDA_PKG_VERSION \
        cuda-cudart-$CUDA_PKG_VERSION

  ln -s cuda-8.0 /usr/local/cuda
  rm -rf /var/lib/apt/lists/*

  echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf
  echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf




  # Devel https://gitlab.com/nvidia/cuda/blob/ubuntu16.04/8.0/devel/Dockerfile 
  
  apt-get update && apt-get install -y --no-install-recommends \
        cuda-core-$CUDA_PKG_VERSION \
        cuda-misc-headers-$CUDA_PKG_VERSION \
        cuda-command-line-tools-$CUDA_PKG_VERSION \
        cuda-nvrtc-dev-$CUDA_PKG_VERSION \
        cuda-nvml-dev-$CUDA_PKG_VERSION \
        cuda-nvgraph-dev-$CUDA_PKG_VERSION \
        cuda-cusolver-dev-$CUDA_PKG_VERSION \
        cuda-cublas-dev-8-0=8.0.61.2-1 \
        cuda-cufft-dev-$CUDA_PKG_VERSION \
        cuda-curand-dev-$CUDA_PKG_VERSION \
        cuda-cusparse-dev-$CUDA_PKG_VERSION \
        cuda-npp-dev-$CUDA_PKG_VERSION \
        cuda-cudart-dev-$CUDA_PKG_VERSION \
        cuda-driver-dev-$CUDA_PKG_VERSION
   
  rm -rf /var/lib/apt/lists/*

 
%runscript

%test
```

## Collection

 - Name: [mikemhenry/cme-lab-images](https://github.com/mikemhenry/cme-lab-images)
 - License: None

