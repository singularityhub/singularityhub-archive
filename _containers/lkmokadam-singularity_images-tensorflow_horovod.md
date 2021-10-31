---
id: 2180
name: "lkmokadam/singularity_images"
branch: "master"
tag: "tensorflow_horovod"
commit: "554fa115b1b83da9a74b2f27cbb0bec56066a3b4"
version: "d88a58497c9c3eb99c0470196bc44735"
build_date: "2018-03-20T18:41:47.106Z"
size_mb: 3796
size: 1704124447
sif: "https://datasets.datalad.org/shub/lkmokadam/singularity_images/tensorflow_horovod/2018-03-20-554fa115-d88a5849/d88a58497c9c3eb99c0470196bc44735.simg"
url: https://datasets.datalad.org/shub/lkmokadam/singularity_images/tensorflow_horovod/2018-03-20-554fa115-d88a5849/
recipe: https://datasets.datalad.org/shub/lkmokadam/singularity_images/tensorflow_horovod/2018-03-20-554fa115-d88a5849/Singularity
collection: lkmokadam/singularity_images
---

# lkmokadam/singularity_images:tensorflow_horovod

```bash
$ singularity pull shub://lkmokadam/singularity_images:tensorflow_horovod
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:9.0-devel-ubuntu16.04

%runscript

    echo "examples at location /examples"

%post
 

    # TensorFlow version is tightly coupled to CUDA and cuDNN so it should be selected carefully
    export TENSORFLOW_VERSION=1.6.0
    export CUDNN_VERSION=7.0.5.15-1+cuda9.0
    export NCCL_VERSION=2.1.15-1+cuda9.0

    # Python 2.7 or 3.5 is supported by Ubuntu Xenial out of the box
    export PYTHON_VERSION=2.7

    echo "deb http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list

    apt-get update && apt-get install -y --no-install-recommends \
            build-essential \
            cmake \
            git \
            curl \
            vim \
            wget \
            ca-certificates \
            libcudnn7=$CUDNN_VERSION \
            libnccl2=$NCCL_VERSION \
            libnccl-dev=$NCCL_VERSION \
            libjpeg-dev \
            libpng-dev \
            python$PYTHON_VERSION \
            python$PYTHON_VERSION-dev

    ln -s /usr/bin/python$PYTHON_VERSION /usr/bin/python

    curl -O https://bootstrap.pypa.io/get-pip.py && \
        python get-pip.py && \
        rm get-pip.py

    # Install TensorFlow and Keras
    pip install --no-cache-dir tensorflow-gpu==$TENSORFLOW_VERSION keras h5py

    # Install Open MPI
    mkdir /tmp/openmpi && \
        cd /tmp/openmpi && \
        wget https://www.open-mpi.org/software/ompi/v3.0/downloads/openmpi-3.0.0.tar.gz && \
        tar zxf openmpi-3.0.0.tar.gz && \
        cd openmpi-3.0.0 && \
        ./configure --enable-orterun-prefix-by-default --enable-mpi-thread-multiple && \
        make -j $(nproc) all && \
        make install && \
        ldconfig && \
        rm -rf /tmp/openmpi

    # Install Horovod, temporarily using CUDA stubs
    ldconfig /usr/local/cuda-9.0/targets/x86_64-linux/lib/stubs && \
        HOROVOD_GPU_ALLREDUCE=NCCL pip install --no-cache-dir horovod && \
        ldconfig

    # Create a wrapper for OpenMPI to allow running as root by default
    mv /usr/local/bin/mpirun /usr/local/bin/mpirun.real && \
        echo '#!/bin/bash' > /usr/local/bin/mpirun && \
        echo 'mpirun.real --allow-run-as-root "$@"' >> /usr/local/bin/mpirun && \
        chmod a+x /usr/local/bin/mpirun

    # Configure OpenMPI to run good defaults:
    #   --bind-to none --map-by slot --mca btl_tcp_if_exclude lo,docker0
    echo "hwloc_base_binding_policy = none" >> /usr/local/etc/openmpi-mca-params.conf && \
        echo "rmaps_base_mapping_policy = slot" >> /usr/local/etc/openmpi-mca-params.conf && \
        echo "btl_tcp_if_exclude = lo,docker0" >> /usr/local/etc/openmpi-mca-params.conf

    # Set default NCCL parameters
    echo NCCL_DEBUG=INFO >> /etc/nccl.conf && \
        echo NCCL_SOCKET_IFNAME=^docker0 >> /etc/nccl.conf

    # Install OpenSSH for MPI to communicate between containers
    apt-get install -y --no-install-recommends openssh-client openssh-server && \
        mkdir -p /var/run/sshd

    # Allow OpenSSH to talk to containers without asking for confirmation
    cat /etc/ssh/ssh_config | grep -v StrictHostKeyChecking > /etc/ssh/ssh_config.new && \
        echo "    StrictHostKeyChecking no" >> /etc/ssh/ssh_config.new && \
        mv /etc/ssh/ssh_config.new /etc/ssh/ssh_config
        
    # Patch container to work on Titan
    ####
    ## Append to #post in bootstrap or run after container creation
    ## sudo singularity exec -w ./TitanPrep.sh
    ####

    # Print commands executed
    set -x

    # Mount point for Cray files
    mkdir -p /opt/cray

    # Mount point for Cray files needed for ALSP runtime
    mkdir -p /var/spool/alps
    mkdir -p /var/opt/cray

    # Mount point for lustre
    mkdir -p /lustre/atlas
    mkdir -p /lustre/atlas1
    mkdir -p /lustre/atlas2

    # Mount point for /sw
    mkdir -p /sw
    mkdir -p /ccs/sw
    mkdir -p /autofs/nccs-svm1_sw

    # Mount point for proj read-only dirs
    mkdir -p /ccs/proj
    mkdir -p /autofs/nccs-svm1_proj

    # Create dummy file to bindmount to
    # This file sources OLFC specific environment variables
    touch /.singularity.d/env/98-OLCF.sh
```

## Collection

 - Name: [lkmokadam/singularity_images](https://github.com/lkmokadam/singularity_images)
 - License: None

