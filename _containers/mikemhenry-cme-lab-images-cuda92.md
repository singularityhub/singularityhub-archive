---
id: 3392
name: "mikemhenry/cme-lab-images"
branch: "master"
tag: "cuda92"
commit: "23b83e2fcc31962bceb133f6ce61c7a19e29d221"
version: "190334b817048ed6563924bad322bf0c"
build_date: "2018-07-02T22:28:01.271Z"
size_mb: 2433
size: 1341001759
sif: "https://datasets.datalad.org/shub/mikemhenry/cme-lab-images/cuda92/2018-07-02-23b83e2f-190334b8/190334b817048ed6563924bad322bf0c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mikemhenry/cme-lab-images/cuda92/2018-07-02-23b83e2f-190334b8/
recipe: https://datasets.datalad.org/shub/mikemhenry/cme-lab-images/cuda92/2018-07-02-23b83e2f-190334b8/Singularity
collection: mikemhenry/cme-lab-images
---

# mikemhenry/cme-lab-images:cuda92

```bash
$ singularity pull shub://mikemhenry/cme-lab-images:cuda92
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
  NVIDIA_REQUIRE_CUDA="cuda>=9.2"

  # devel envs
  LIBRARY_PATH=/usr/local/cuda/lib64/stubs


  export PATH LD_LIBRARY_PATH NVIDIA_VISIBLE_DEVICES NVIDIA_DRIVER_CAPABILITIES NVIDIA_REQUIRE_CUDA LIBRARY_PATH



%post
  # Base https://gitlab.com/nvidia/cuda/blob/ubuntu16.04/9.2/base/Dockerfile
  export CUDA_VERSION=9.2.88
  export CUDA_PKG_VERSION=9-2=$CUDA_VERSION-1
  
  apt-get update && apt-get install -y --no-install-recommends ca-certificates apt-transport-https gnupg-curl
  rm -rf /var/lib/apt/lists/*
    
  NVIDIA_GPGKEY_SUM=d1be581509378368edeec8c1eb2958702feedf3bc3d17011adbf24efacce4ab5
  NVIDIA_GPGKEY_FPR=ae09fe4bbd223a84b2ccfce3f60f4b3d7fa2af80
  
  apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
  apt-key adv --export --no-emit-version -a $NVIDIA_GPGKEY_FPR | tail -n +5 > cudasign.pub
  echo "$NVIDIA_GPGKEY_SUM  cudasign.pub" | sha256sum -c --strict - && rm cudasign.pub 
  echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/cuda.list 
  echo "deb https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list

  apt-get update && apt-get install -y --no-install-recommends cuda-cudart-$CUDA_PKG_VERSION
  ln -s cuda-9.2 /usr/local/cuda
  rm -rf /var/lib/apt/lists/*

  echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf
  echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf

  # Runtime https://gitlab.com/nvidia/cuda/blob/ubuntu16.04/9.2/runtime/Dockerfile

  export NCCL_VERSION=2.2.12

  apt-get update && apt-get install -y --no-install-recommends \
        cuda-libraries-$CUDA_PKG_VERSION \
        cuda-nvtx-$CUDA_PKG_VERSION \
        libnccl2=$NCCL_VERSION-1+cuda9.2
  rm -rf /var/lib/apt/lists/*

  # Devel https://gitlab.com/nvidia/cuda/blob/ubuntu16.04/9.2/devel/Dockerfile

  apt-get update && apt-get install -y --no-install-recommends \
        cuda-libraries-dev-$CUDA_PKG_VERSION \
        cuda-nvml-dev-$CUDA_PKG_VERSION \
        cuda-minimal-build-$CUDA_PKG_VERSION \
        cuda-command-line-tools-$CUDA_PKG_VERSION \
        libnccl-dev=$NCCL_VERSION-1+cuda9.2
  rm -rf /var/lib/apt/lists/*

 
%runscript

%test
```

## Collection

 - Name: [mikemhenry/cme-lab-images](https://github.com/mikemhenry/cme-lab-images)
 - License: None

