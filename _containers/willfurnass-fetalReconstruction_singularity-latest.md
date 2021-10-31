---
id: 9399
name: "willfurnass/fetalReconstruction_singularity"
branch: "master"
tag: "latest"
commit: "70161d342ac10ccc8ed4146ad096c789f78f1557"
version: "c10ae4cb00c194b6c6d4113e9aaa5379"
build_date: "2019-05-29T23:06:07.669Z"
size_mb: 2747
size: 1466675231
sif: "https://datasets.datalad.org/shub/willfurnass/fetalReconstruction_singularity/latest/2019-05-29-70161d34-c10ae4cb/c10ae4cb00c194b6c6d4113e9aaa5379.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/willfurnass/fetalReconstruction_singularity/latest/2019-05-29-70161d34-c10ae4cb/
recipe: https://datasets.datalad.org/shub/willfurnass/fetalReconstruction_singularity/latest/2019-05-29-70161d34-c10ae4cb/Singularity
collection: willfurnass/fetalReconstruction_singularity
---

# willfurnass/fetalReconstruction_singularity:latest

```bash
$ singularity pull shub://willfurnass/fetalReconstruction_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.2-devel-ubuntu16.04

%labels

   AUTHOR w.furnass@sheffield.ac.uk

%post
    apt-get update
    apt-get install -y \
        bzip2 \
        cmake \
        git \
        libbz2-dev \
        libgsl-dev \
        libgsl2 \
        libnifti-dev \
        libtbb-dev \
        libtbb2 \
        wget \
	zlib1g-dev 
    cd /opt

    # Build and install Boost
    wget http://sourceforge.net/projects/boost/files/boost/1.58.0/boost_1_58_0.tar.gz -P /tmp 
    tar -C /opt -zxf /tmp/boost_1_58_0.tar.gz
    cd /opt/boost_1_58_0
    ./bootstrap.sh --with-libraries=atomic,date_time,exception,filesystem,iostreams,locale,program_options,regex,signals,system,test,thread,timer,log
    ./b2 --with=all install
    ldconfig

    # Grab CUDA Samples (needed for helper_cuda.h)
    git clone --branch v9.2 --depth 1 https://github.com/NVIDIA/cuda-samples.git /usr/local/cuda-9.2/samples && \

    # Build fetalReconstruction
    mkdir /opt/fetalReconstruction
    cd /opt/
    git clone https://github.com/bkainz/fetalReconstruction.git
    cd fetalReconstruction
    # NB need to use particular commit > tag r0.1 to get CUDA >=7.5 support
    git checkout 69c381f68cc5527650e08e926caebbffd73b7a9f

    mkdir source/build
    cd source/build
    cmake .. -DCUDA_SDK_ROOT_DIR=/usr/local/cuda-9.2/samples -DCUDA_ROOT_DIR=/usr/local/cuda-9.2 -DCUDA_HELPER_INCLUDE_DIR='/usr/local/cuda-9.2/samples/Common' -DCUDA_CUDA_LIBRARY=/usr/local/cuda-9.2/targets/x86_64-linux/lib/stubs/libcuda.so
    make

    # Ensure built binaries are executable and  on the PATH
    for i in /opt/fetalReconstruction/bin/linux64/*; do chmod +x $i; ln -s $i /usr/local/bin; done

    # Cleanup to reduce image size
    apt-get purge -y \
        cmake \
        git \
        libbz2-dev \
        libgsl-dev \
        libnifti-dev \
        libtbb-dev \
        wget \
	zlib1g-dev 
    apt-get --purge -y autoremove
    rm -rf /var/lib/apt/lists/*
    rm -r /opt/boost_1_58_0
    rm -rf /opt/fetalReconstruction/source
    rm -rf /opt/fetalReconstruction/.git

%runscript
    /usr/local/bin/PVRreconstructionGPU
```

## Collection

 - Name: [willfurnass/fetalReconstruction_singularity](https://github.com/willfurnass/fetalReconstruction_singularity)
 - License: None

