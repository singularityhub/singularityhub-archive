---
id: 7886
name: "14renus/sdsc"
branch: "master"
tag: "latest"
commit: "496f1f05e461844a3ee9cfd0398515fb06d5067a"
version: "04f2b99d5358d4e11c25cf549fca9de9"
build_date: "2020-03-12T19:03:31.671Z"
size_mb: 6936
size: 3095064607
sif: "https://datasets.datalad.org/shub/14renus/sdsc/latest/2020-03-12-496f1f05-04f2b99d/04f2b99d5358d4e11c25cf549fca9de9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/14renus/sdsc/latest/2020-03-12-496f1f05-04f2b99d/
recipe: https://datasets.datalad.org/shub/14renus/sdsc/latest/2020-03-12-496f1f05-04f2b99d/Singularity
collection: 14renus/sdsc
---

# 14renus/sdsc:latest

```bash
$ singularity pull shub://14renus/sdsc:latest
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
MirrorURL: http://us.archive.ubuntu.com/ubuntu
OSVersion: xenial

%labels

    APPLICATION_NAME tensorflow
    APPLICATION_VERSION 1.12
    APPLICATION_URL https://www.tensorflow.org

    SYSTEM_NAME comet
    SYSTEM_SINGULARITY_VERSION 2.5.2
    SYSTEM_URL http://www.sdsc.edu/support/user_guides/comet.html

    SINGULARITY_IMAGE_SIZE 32768

    AUTHOR_NAME Marty Kandes
    AUTHOR_EMAIL mkandes@sdsc.edu

    LAST_UPDATED 20181218

%setup

%environment

    # Set system locale
    export LC_ALL=C
    export PATH="/usr/local/cuda-9.2/bin${PATH:+:${PATH}}"
    export LD_LIBRARY_PATH="/usr/local/cuda-9.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}"
    export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/usr/local/cuda/extras/CUPTI/lib64"
    export PATH="/opt/openmpi-1.8.4/bin:${PATH}"
    export LD_LIBRARY_PATH="/opt/openmpi-1.8.4/lib:${LD_LIBRARY_PATH}"

%post -c /bin/bash

    # Set system locale
    export LC_ALL=C

    # Install system metapackages
    apt-get -y install ubuntu-standard
    apt-get -y install ubuntu-server

    # Add repositories
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION} main"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION} universe"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION} multiverse"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION} restricted"

    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-updates main"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-updates universe"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-updates multiverse"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-updates restricted"

    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-backports main"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-backports universe"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-backports multiverse"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-backports restricted"

    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-security main"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-security universe"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-security multiverse"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-security restricted"

    # Upgrade all packages to their latest versions
    apt-get -y update && apt-get -y upgrade

    # Install common packages from 'main'
    apt-get -y install autoconf
    apt-get -y install automake
    apt-get -y install build-essential
    apt-get -y install cmake
    apt-get -y install libtool
    apt-get -y install pkg-config
    apt-get -y install gfortran
    apt-get -y install zip

    # Install expect to automate responses for interactive build questions
    apt-get -y install expect

    # Make filesystem mount points
    mkdir /cvmfs /oasis /projects /scratch

    # Use /tmp to store temporary files within the container during the
    # bootstraping process
    cd /tmp

    # Location of NVIDIA repositories
    declare -r NVIDIA_ROOT_URL='http://developer.download.nvidia.com/compute'
    declare -r CUDA_REPO_URL="${NVIDIA_ROOT_URL}/cuda/repos/ubuntu1604/x86_64"
    declare -r ML_REPO_URL="${NVIDIA_ROOT_URL}/machine-learning/repos/ubuntu1604/x86_64/"

    # Install NVIDIA package dependencies
    apt-get -y install x11-common
    apt-get -y install xserver-xorg-core
    apt-get -y install xserver-xorg-legacy
    apt-get -y install cmake
    apt-get -y install make
    apt-get -y install dkms
    apt-get -y install linux-libc-dev
    apt-get -y install libc6-dev
    apt-get -y install lib32gcc1
    apt-get -y install libc6-i386
    apt-get -y install libgl1
    apt-get -y install libwayland-client0
    apt-get -y install libwayland-server0
    apt-get -y install pkg-config
    apt-get -y install screen-resolution-extra
    apt-get -y install libvdpau1
    apt-get -y install libatk1.0-0
    apt-get -y install libcairo-gobject2
    apt-get -y install libcairo2
    apt-get -y install libfontconfig1
    apt-get -y install libgdk-pixbuf2.0-0
    apt-get -y install libgtk-3-0
    apt-get -y install libgtk2.0-0
    apt-get -y install libjansson4
    apt-get -y install freeglut3-dev
    apt-get -y install libx11-dev
    apt-get -y install libxmu-dev
    apt-get -y install libxi-dev
    apt-get -y install libglu1-mesa
    apt-get -y install libglu1-mesa-dev
    apt-get -y install default-jre

    # Download NVIDIA drivers, libraries, and packages
    wget --wait=10 "${CUDA_REPO_URL}/nvidia-396_396.26-0ubuntu1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/nvidia-396-dev_396.26-0ubuntu1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/nvidia-modprobe_396.26-0ubuntu1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/libcuda1-396_396.26-0ubuntu1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/nvidia-libopencl1-396_396.26-0ubuntu1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/nvidia-opencl-icd-396_396.26-0ubuntu1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/libxnvctrl0_396.26-0ubuntu1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/nvidia-settings_396.26-0ubuntu1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-drivers_396.26-1_amd64.deb"

    wget --wait=10 "${CUDA_REPO_URL}/cuda-license-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-misc-headers-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-nvcc-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-cuobjdump-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-nvprune-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-compiler-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-core-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-cudart-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-driver-dev-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-cudart-dev-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-nvdisasm-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-gdb-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-nvprof-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-memcheck-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-cupti-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-gpu-library-advisor-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-nvtx-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-command-line-tools-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-nvrtc-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-nvrtc-dev-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-nvml-dev-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-nvgraph-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-nvgraph-dev-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-cusolver-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-cusolver-dev-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-cublas-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-cublas-dev-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-cufft-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-cufft-dev-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-curand-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-curand-dev-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-cusparse-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-cusparse-dev-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-npp-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-npp-dev-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-samples-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-documentation-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-nsight-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-nvvp-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-visual-tools-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-tools-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-libraries-dev-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-toolkit-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-libraries-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-runtime-9-2_9.2.88-1_amd64.deb"
    wget --wait=10 "${CUDA_REPO_URL}/cuda-demo-suite-9-2_9.2.88-1_amd64.deb"

    wget --wait=10 "${ML_REPO_URL}/libcudnn7_7.2.1.38-1+cuda9.2_amd64.deb"
    wget --wait=10 "${ML_REPO_URL}/libcudnn7-dev_7.2.1.38-1+cuda9.2_amd64.deb"

    wget --wait=10 "${ML_REPO_URL}/libnccl2_2.3.4-1+cuda9.2_amd64.deb"
    wget --wait=10 "${ML_REPO_URL}/libnccl-dev_2.3.4-1+cuda9.2_amd64.deb"

    # Fix for "update-alternatives: error: error creating symbolic link '/usr/lib/nvidia/alternate-install-present.dpkg-tmp': No such file or directory"
    mkdir -p /usr/lib/nvidia

    # Install NVIDIA drivers, libraries, and packages
    dpkg -i nvidia-396_396.26-0ubuntu1_amd64.deb
    dpkg -i nvidia-396-dev_396.26-0ubuntu1_amd64.deb
    dpkg -i nvidia-modprobe_396.26-0ubuntu1_amd64.deb
    dpkg -i libcuda1-396_396.26-0ubuntu1_amd64.deb
    dpkg -i nvidia-libopencl1-396_396.26-0ubuntu1_amd64.deb
    dpkg -i nvidia-opencl-icd-396_396.26-0ubuntu1_amd64.deb
    dpkg -i libxnvctrl0_396.26-0ubuntu1_amd64.deb
    dpkg -i nvidia-settings_396.26-0ubuntu1_amd64.deb
    dpkg -i cuda-drivers_396.26-1_amd64.deb

    dpkg -i cuda-license-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-misc-headers-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-nvcc-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-cuobjdump-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-nvprune-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-compiler-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-core-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-cudart-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-driver-dev-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-cudart-dev-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-nvdisasm-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-gdb-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-nvprof-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-memcheck-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-cupti-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-gpu-library-advisor-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-nvtx-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-command-line-tools-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-nvrtc-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-nvrtc-dev-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-nvml-dev-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-nvgraph-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-nvgraph-dev-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-cusolver-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-cusolver-dev-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-cublas-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-cublas-dev-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-cufft-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-cufft-dev-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-curand-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-curand-dev-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-cusparse-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-cusparse-dev-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-npp-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-npp-dev-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-samples-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-documentation-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-nsight-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-nvvp-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-visual-tools-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-tools-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-libraries-dev-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-toolkit-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-libraries-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-runtime-9-2_9.2.88-1_amd64.deb
    dpkg -i cuda-demo-suite-9-2_9.2.88-1_amd64.deb

    dpkg -i libcudnn7_7.2.1.38-1+cuda9.2_amd64.deb
    dpkg -i libcudnn7-dev_7.2.1.38-1+cuda9.2_amd64.deb

    dpkg -i libnccl2_2.3.4-1+cuda9.2_amd64.deb
    dpkg -i libnccl-dev_2.3.4-1+cuda9.2_amd64.deb

    # Fixing some TensorFlow and libnccl*.deb path issues ...
    mv /usr/lib/x86_64-linux-gnu/libnccl_static.a /usr/local/cuda-9.2/lib64/libnccl_static.a
    mv /usr/lib/x86_64-linux-gnu/libnccl.so.2.3.4 /usr/local/cuda-9.2/lib64/libnccl.so.2.3.4
    ln -s /usr/local/cuda-9.2/lib64/libnccl.so.2.3.4 /usr/local/cuda-9.2/lib64/libnccl.so.2
    ln -s /usr/local/cuda-9.2/lib64/libnccl.so.2 /usr/local/cuda-9.2/lib64/libnccl.so
    mv /usr/include/nccl.h /usr/local/cuda-9.2/include/nccl.h
    ln -s /usr/local/cuda-9.2/lib64 /usr/local/cuda-9.2/lib
    mv /usr/share/doc/libnccl2/NCCL-SLA.txt.gz /usr/local/cuda-9.2/NCCL-SLA.txt

    # Set paths to CUDA binaries and libraries
    export PATH="/usr/local/cuda-9.2/bin${PATH:+:${PATH}}"
    export LD_LIBRARY_PATH="/usr/local/cuda-9.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}"
    export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/usr/local/cuda/extras/CUPTI/lib64"

    # Install basic drivers for user space access to Ethernet, RDMA,
    # and Infiniband. See https://community.mellanox.com/docs/DOC-2431
    apt-get -y install dkms
    apt-get -y install infiniband-diags
    apt-get -y install libibverbs-dev
    apt-get -y install ibacm
    apt-get -y install librdmacm-dev
    apt-get -y install libmlx4-dev
    apt-get -y install libmlx5-dev
    apt-get -y install mstflint
    apt-get -y install libibcm-dev
    apt-get -y install libibmad-dev
    apt-get -y install libibumad-dev
    apt-get -y install opensm
    apt-get -y install srptools

    # Install additional tools
    apt-get -y install ibutils
    apt-get -y install ibverbs-utils
    apt-get -y install rdmacm-utils
    apt-get -y install perftest
    apt-get -y install numactl
    apt-get -y install libnuma-dev

    # Install libnl
    apt-get -y install libnl-3-200
    apt-get -y install libnl-route-3-200
    apt-get -y install libnl-route-3-dev
    apt-get -y install libnl-utils

    # Install OpenMPI dependencies
    apt-get -y install zlib1g-dev

    # Download, build, and install CUDA-aware OpenMPI
    wget https://www.open-mpi.org/software/ompi/v1.8/downloads/openmpi-1.8.4.tar.gz
    tar -xzvf openmpi-1.8.4.tar.gz
    cd openmpi-1.8.4
    ./configure --prefix=/opt/openmpi-1.8.4 --with-cuda
    make all install

    # Set paths to OpenMPI binaries and libraries
    export PATH="/opt/openmpi-1.8.4/bin:${PATH}"
    export LD_LIBRARY_PATH="/opt/openmpi-1.8.4/lib:${LD_LIBRARY_PATH}"

    # Install Bazel from Debian Package
    apt-get -y install openjdk-8-jdk
    apt-get -y install zlib1g-dev
    wget https://github.com/bazelbuild/bazel/releases/download/0.17.2/bazel_0.17.2-linux-x86_64.deb
    dpkg -i bazel_0.17.2-linux-x86_64.deb

    # Install TensorFlow python(2) dependencies
    apt-get -y install python
    apt-get -y install python-dev
    apt-get -y install python-pip
    apt-get -y install python-six
    apt-get -y install python-wheel
    apt-get -y install python-enum34
    apt-get -y install python-mock
    apt-get -y install python-numpy

    pip install keras_applications==1.0.5 --no-deps
    pip install keras_preprocessing==1.0.3 --no-deps

    pip install scikit-image SimpleITK nibabel

    cd /opt

    # Download TensorFlow source
    git clone https://github.com/tensorflow/tensorflow
    cd /opt/tensorflow
    git checkout r1.12

    # Build and install TensorFlow for python(2)
    echo '#!/usr/bin/expect -f' > install-tensorflow-python.exp
    echo 'spawn ./configure' >> install-tensorflow-python.exp
    echo 'expect "Please specify the location of python. \[Default is /usr/bin/python\]: "' >> install-tensorflow-python.exp
    echo 'send "/usr/bin/python\r"' >> install-tensorflow-python.exp
    echo 'expect "Please input the desired Python library path to use.  Default is \[/usr/local/lib/python2.7/dist-packages\]\r"' >> install-tensorflow-python.exp
    echo 'send "/usr/local/lib/python2.7/dist-packages\r"' >> install-tensorflow-python.exp
    echo 'expect "Do you wish to build TensorFlow with Apache Ignite support? \[Y/n\]: "' >> install-tensorflow-python.exp
    echo 'send "N\r"' >> install-tensorflow-python.exp
    echo 'expect "Do you wish to build TensorFlow with XLA JIT support? \[Y/n\]: "' >> install-tensorflow-python.exp
    echo 'send "N\r"' >> install-tensorflow-python.exp
    echo 'expect "Do you wish to build TensorFlow with OpenCL SYCL support? \[y/N\]: "' >> install-tensorflow-python.exp
    echo 'send "N\r"' >> install-tensorflow-python.exp
    echo 'expect "Do you wish to build TensorFlow with ROCm support? \[y/N\]: "' >> install-tensorflow-python.exp
    echo 'send "N\r"' >> install-tensorflow-python.exp
    echo 'expect "Do you wish to build TensorFlow with CUDA support? \[y/N\]: "' >> install-tensorflow-python.exp
    echo 'send "Y\r"' >> install-tensorflow-python.exp
    echo 'expect "Please specify the CUDA SDK version you want to use. \[Leave empty to default to CUDA 9.0\]: "' >> install-tensorflow-python.exp
    echo 'send "9.2.88\r"' >> install-tensorflow-python.exp
    echo 'expect "Please specify the location where CUDA 9.2 toolkit is installed. Refer to README.md for more details. \[Default is /usr/local/cuda\]: "' >> install-tensorflow-python.exp
    echo 'send "/usr/local/cuda\r"' >> install-tensorflow-python.exp
    echo 'expect "Please specify the cuDNN version you want to use. \[Leave empty to default to cuDNN 7\]: "' >> install-tensorflow-python.exp
    echo 'send "7.2.1.38\r"' >> install-tensorflow-python.exp
    echo 'expect "Please specify the location where cuDNN 7 library is installed. Refer to README.md for more details. \[Default is /usr/local/cuda\]: "' >> install-tensorflow-python.exp
    echo 'send "/usr/lib/x86_64-linux-gnu\r"' >> install-tensorflow-python.exp
    echo 'expect "Do you wish to build TensorFlow with TensorRT support? \[y/N\]: "' >> install-tensorflow-python.exp
    echo 'send "N\r"' >> install-tensorflow-python.exp
    echo 'expect "Please specify the NCCL version you want to use. If NCCL 2.2 is not installed, then you can use version 1.3 that can be fected automatically but it may have worse performance with multiple GPUs. \[Default is 2.2\]:"' >> install-tensorflow-python.exp
    echo 'send "2.3.4\r"' >> install-tensorflow-python.exp
    echo 'expect "Please specify a list of comma-separated Cuda compute capabilities you want to build with.\r"' >> install-tensorflow-python.exp
    echo 'expect "You can find the compute capability of your device at: https://developer.nvidia.com/cuda-gpus.\r"' >> install-tensorflow-python.exp
    echo 'expect "Please note that each additional compute capability significantly increases your build time and binary size. \[Default is: 3.5,7.0\]"' >> install-tensorflow-python.exp
    echo 'send "3.7,6.0\r"' >> install-tensorflow-python.exp
    echo 'expect "Do you want to use clang as CUDA compiler? \[y/N\]: "' >> install-tensorflow-python.exp
    echo 'send "N\r"' >> install-tensorflow-python.exp
    echo 'expect "Please specify which gcc should be used by nvcc as the host compiler. \[Default is /usr/bin/gcc\]: "' >> install-tensorflow-python.exp
    echo 'send "/usr/bin/gcc\r"' >> install-tensorflow-python.exp
    echo 'expect "Do you wish to build TensorFlow with MPI support? \[y/N\]: "' >> install-tensorflow-python.exp
    echo 'send "N\r"' >> install-tensorflow-python.exp
    #echo 'expect "Please specify the MPI toolkit folder. \[Default is /opt/openmpi-1.8.4\]: "' >> install-tensorflow-python.exp
    #echo 'send "/opt/openmpi-1.8.4\r"' >> install-tensorflow-python.exp
    echo 'expect "Please specify optimization flags to use during compilation when bazel option \"--config=opt\" is specified \[Default is -march=native\]: "' >> install-tensorflow-python.exp
    echo 'send " -march=haswell -mmmx -mno-3dnow -msse -msse2 -msse3 -mssse3 -mno-sse4a -mcx16 -msahf -mmovbe -maes -mno-sha -mpclmul -mpopcnt -mabm -mno-lwp -mfma -mno-fma4 -mno-xop -mbmi -mbmi2 -mno-tbm -mavx -mavx2 -msse4.2 -msse4.1 -mlzcnt -mno-rtm -mno-hle -mrdrnd -mf16c -mfsgsbase -mno-rdseed -mno-prfchw -mno-adx -mfxsr -mxsave -mxsaveopt -mno-avx512f -mno-avx512er -mno-avx512cd -mno-avx512pf -mno-prefetchwt1 -mtune=haswell \r"' >> install-tensorflow-python.exp
    echo 'expect "Would you like to interactively configure ./WORKSPACE for Android builds? \[y/N\]: "' >> install-tensorflow-python.exp
    echo 'send "N\r"' >> install-tensorflow-python.exp
    echo 'expect "> "' >> install-tensorflow-python.exp

    chmod +x install-tensorflow-python.exp
    ./install-tensorflow-python.exp
 
    # See https://github.com/tensorflow/tensorflow/issues/17801
    #ln -s /usr/local/cuda-8.0/nvvm/libdevice/libdevice.compute_50.10.bc /usr/local/cuda-8.0/nvvm/libdevice/libdevice.10.bc

    # See https://github.com/tensorflow/tensorflow/issues/19203
    #     https://github.com/ghostplant/tensorflow-cuda8-optimized/blob/master/Dockerfile.tf18-py35-cuda8-cudnn6021
    #sed -i 's/^#if TF_HAS_.*$/#if !defined(__NVCC__)/g' tensorflow/core/platform/macros.h

    # Clear /home/root/.cache prior to bazel build. Otherwise, previous builds may cause some conflicts. See 'dangling symbolic links' at https://github.com/tensorflow/tensorflow/issues/13928
    rm -rf /home/root/.cache

    #bazel build --local_resources 2048,.5,1.0 -c opt --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0" --config=cuda --config=gdr --config=verbs //tensorflow/tools/pip_package:build_pip_package
    bazel build --local_resources 2048,.5,1.0 -c opt --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0" --config=cuda //tensorflow/tools/pip_package:build_pip_package
    bazel-bin/tensorflow/tools/pip_package/build_pip_package tensorflow_pkg

    pip install tensorflow_pkg/tensorflow-1.12.0-cp27-cp27mu-linux_x86_64.whl

    # Install common python packages for data science and machine learning applications
    apt-get -y install python-scipy
    apt-get -y install python-pandas
    apt-get -y install python-matplotlib
    apt-get -y install ipython
    apt-get -y install ipython-notebook
    apt-get -y install python-sympy
    apt-get -y install python-nose
    apt-get -y install python-sklearn
    apt-get -y install python-mlpy
    apt-get -y install python-nltk
    apt-get -y install python-statsmodels
    apt-get -y install libopencv-dev
    apt-get -y install python-opencv

    # Install common python packages for the biological and biomedical sciences
    apt-get -y install python-biopython
    apt-get -y install python-biopython-sql

    # Install other common python packages
    apt-get -y install python-h5py

    # Install Keras-related python packages
    apt-get -y install python-pydot

    # Install custom requests from users
    pip install h5py-cache

    # Install TensorFlow python3 dependencies
    apt-get -y install python3
    apt-get -y install python3-dev
    apt-get -y install python3-pip
    apt-get -y install python3-six
    apt-get -y install python3-wheel
    apt-get -y install python3-mock
    apt-get -y install python3-numpy

    pip3 install keras_applications==1.0.5 --no-deps
    pip3 install keras_preprocessing==1.0.3 --no-deps

    # Build and install TensorFlow for python3
    echo '#!/usr/bin/expect -f' > install-tensorflow-python3.exp
    echo 'spawn ./configure' >> install-tensorflow-python3.exp
    echo 'expect "Please specify the location of python. \[Default is /usr/bin/python\]: "' >> install-tensorflow-python3.exp
    echo 'send "/usr/bin/python3\r"' >> install-tensorflow-python3.exp
    echo 'expect "Please input the desired Python library path to use.  Default is \[/usr/local/lib/python2.7/dist-packages\]\r"' >> install-tensorflow-python3.exp
    echo 'send "/usr/local/lib/python3.5/dist-packages\r"' >> install-tensorflow-python3.exp
    echo 'expect "Do you wish to build TensorFlow with Apache Ignite support? \[Y/n\]: "' >> install-tensorflow-python3.exp
    echo 'send "N\r"' >> install-tensorflow-python3.exp
    echo 'expect "Do you wish to build TensorFlow with XLA JIT support? \[Y/n\]: "' >> install-tensorflow-python3.exp
    echo 'send "N\r"' >> install-tensorflow-python3.exp
    echo 'expect "Do you wish to build TensorFlow with OpenCL SYCL support? \[y/N\]: "' >> install-tensorflow-python3.exp
    echo 'send "N\r"' >> install-tensorflow-python3.exp
    echo 'expect "Do you wish to build TensorFlow with ROCm support? \[y/N\]: "' >> install-tensorflow-python3.exp
    echo 'send "N\r"' >> install-tensorflow-python3.exp
    echo 'expect "Do you wish to build TensorFlow with CUDA support? \[y/N\]: "' >> install-tensorflow-python3.exp
    echo 'send "Y\r"' >> install-tensorflow-python3.exp
    echo 'expect "Please specify the CUDA SDK version you want to use. \[Leave empty to default to CUDA 9.0\]: "' >> install-tensorflow-python3.exp
    echo 'send "9.2.88\r"' >> install-tensorflow-python3.exp
    echo 'expect "Please specify the location where CUDA 9.2 toolkit is installed. Refer to README.md for more details. \[Default is /usr/local/cuda\]: "' >> install-tensorflow-python3.exp
    echo 'send "/usr/local/cuda\r"' >> install-tensorflow-python3.exp
    echo 'expect "Please specify the cuDNN version you want to use. \[Leave empty to default to cuDNN 7\]: "' >> install-tensorflow-python3.exp
    echo 'send "7.2.1.38\r"' >> install-tensorflow-python3.exp
    echo 'expect "Please specify the location where cuDNN 7 library is installed. Refer to README.md for more details. \[Default is /usr/local/cuda\]: "' >> install-tensorflow-python3.exp
    echo 'send "/usr/lib/x86_64-linux-gnu\r"' >> install-tensorflow-python3.exp
    echo 'expect "Do you wish to build TensorFlow with TensorRT support? \[y/N\]: "' >> install-tensorflow-python3.exp
    echo 'send "N\r"' >> install-tensorflow-python3.exp
    echo 'expect "Please specify the NCCL version you want to use. If NCCL 2.2 is not installed, then you can use version 1.3 that can be fected automatically but it may have worse performance with multiple GPUs. \[Default is 2.2\]:"' >> install-tensorflow-python3.exp
    echo 'send "2.3.4\r"' >> install-tensorflow-python3.exp
    echo 'expect "Please specify a list of comma-separated Cuda compute capabilities you want to build with.\r"' >> install-tensorflow-python3.exp
    echo 'expect "You can find the compute capability of your device at: https://developer.nvidia.com/cuda-gpus.\r"' >> install-tensorflow-python3.exp
    echo 'expect "Please note that each additional compute capability significantly increases your build time and binary size. \[Default is: 3.5,7.0\]"' >> install-tensorflow-python3.exp
    echo 'send "3.7,6.0\r"' >> install-tensorflow-python3.exp
    echo 'expect "Do you want to use clang as CUDA compiler? \[y/N\]: "' >> install-tensorflow-python3.exp
    echo 'send "N\r"' >> install-tensorflow-python3.exp
    echo 'expect "Please specify which gcc should be used by nvcc as the host compiler. \[Default is /usr/bin/gcc\]: "' >> install-tensorflow-python3.exp
    echo 'send "/usr/bin/gcc\r"' >> install-tensorflow-python3.exp
    echo 'expect "Do you wish to build TensorFlow with MPI support? \[y/N\]: "' >> install-tensorflow-python3.exp
    echo 'send "N\r"' >> install-tensorflow-python3.exp
    #echo 'expect "Please specify the MPI toolkit folder. \[Default is /opt/openmpi-1.8.4\]: "' >> install-tensorflow-python3.exp
    #echo 'send "/opt/openmpi-1.8.4\r"' >> install-tensorflow-python3.exp
    echo 'expect "Please specify optimization flags to use during compilation when bazel option \"--config=opt\" is specified \[Default is -march=native\]: "' >> install-tensorflow-python3.exp
    echo 'send " -march=haswell -mmmx -mno-3dnow -msse -msse2 -msse3 -mssse3 -mno-sse4a -mcx16 -msahf -mmovbe -maes -mno-sha -mpclmul -mpopcnt -mabm -mno-lwp -mfma -mno-fma4 -mno-xop -mbmi -mbmi2 -mno-tbm -mavx -mavx2 -msse4.2 -msse4.1 -mlzcnt -mno-rtm -mno-hle -mrdrnd -mf16c -mfsgsbase -mno-rdseed -mno-prfchw -mno-adx -mfxsr -mxsave -mxsaveopt -mno-avx512f -mno-avx512er -mno-avx512cd -mno-avx512pf -mno-prefetchwt1 -mtune=haswell \r"' >> install-tensorflow-python3.exp
    echo 'expect "Would you like to interactively configure ./WORKSPACE for Android builds? \[y/N\]: "' >> install-tensorflow-python3.exp
    echo 'send "N\r"' >> install-tensorflow-python3.exp
    echo 'expect "> "' >> install-tensorflow-python3.exp

    chmod +x install-tensorflow-python3.exp
    ./install-tensorflow-python3.exp

    # Clear /home/root/.cache prior to bazel build. Otherwise, previous builds may cause some conflicts. See 'dangling symbolic links' at https://github.com/tensorflow/tensorflow/issues/13928
    rm -rf /home/root/.cache

    # It is recommended to run bazel clean when switching between two configurations in the same source tree.
    bazel clean

    bazel build --local_resources 2048,.5,1.0 -c opt --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0" --config=cuda //tensorflow/tools/pip_package:build_pip_package
    bazel-bin/tensorflow/tools/pip_package/build_pip_package tensorflow_pkg

    pip3 install tensorflow_pkg/tensorflow-1.12.0-cp35-cp35m-linux_x86_64.whl

    # Install common python3 packages for data science and machine learning applications
    apt-get -y install python3-scipy
    apt-get -y install python3-pandas
    apt-get -y install python3-matplotlib
    apt-get -y install ipython3
    apt-get -y install ipython3-notebook
    apt-get -y install python3-sympy
    apt-get -y install python3-nose
    apt-get -y install python3-sklearn
    apt-get -y install python3-nltk

    # Install common python3 packages for the biological and biomedical sciences
    apt-get -y install python3-biopython
    apt-get -y install python3-biopython-sql

    # Install other common python3 packages
    apt-get -y install python3-h5py

    # Install Keras-related python3 packages
    apt-get -y install python3-pydot

    # Install custom requests from users
    pip3 install h5py-cache

    # Update database for mlocate
    updatedb

%files

%runscript

%test
```

## Collection

 - Name: [14renus/sdsc](https://github.com/14renus/sdsc)
 - License: None

