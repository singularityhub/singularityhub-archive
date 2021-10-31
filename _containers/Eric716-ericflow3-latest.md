---
id: 9235
name: "Eric716/ericflow3"
branch: "master"
tag: "latest"
commit: "879f008ae4408b1425edd256cc1f1fd7fa8219b7"
version: "7b02860bb72b4583f878b64025cb31f4"
build_date: "2019-05-23T03:52:52.948Z"
size_mb: 5546
size: 2879995935
sif: "https://datasets.datalad.org/shub/Eric716/ericflow3/latest/2019-05-23-879f008a-7b02860b/7b02860bb72b4583f878b64025cb31f4.simg"
url: https://datasets.datalad.org/shub/Eric716/ericflow3/latest/2019-05-23-879f008a-7b02860b/
recipe: https://datasets.datalad.org/shub/Eric716/ericflow3/latest/2019-05-23-879f008a-7b02860b/Singularity
collection: Eric716/ericflow3
---

# Eric716/ericflow3:latest

```bash
$ singularity pull shub://Eric716/ericflow3:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.0-devel-ubuntu16.04

%post
apt-get update && apt-get install -y --allow-downgrades --allow-change-held-packages --no-install-recommends \
        build-essential \
        cmake \
        git \
        curl \
        vim \
        wget \
		sudo \
        ca-certificates \
        libcudnn7=7.5.1.10-1+cuda10.0 \
        libnccl2=2.4.7-1+cuda10.0 \
        libnccl-dev=2.4.7-1+cuda10.0 \
        libjpeg-dev \
        libpng-dev \
        python3.5 \
        python3.5-dev
ln -s /usr/bin/python3.5 /usr/bin/python
ln -s /usr/bin/python3.5 /usr/bin/python3
curl -O https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    rm get-pip.py
pip install tensorflow-gpu==1.13.1 h5py
apt-get update && apt-get install -y --no-install-recommends \
        wget \
        perl \
        lsb-release
cd / && \
    wget http://www.mellanox.com/downloads/ofed/MLNX_OFED-3.4-2.0.0.0/MLNX_OFED_LINUX-3.4-2.0.0.0-ubuntu16.04-x86_64.tgz && \
    tar -xzvf MLNX_OFED_LINUX-3.4-2.0.0.0-ubuntu16.04-x86_64.tgz && \
    yes y | head -1 | MLNX_OFED_LINUX-3.4-2.0.0.0-ubuntu16.04-x86_64/mlnxofedinstall --user-space-only --without-fw-update --all -vvv && \
    cd / && \
    rm -rf MLNX_OFED_LINUX-3.4-2.0.0.0-ubuntu16.04-x86_64.tgz
apt-get update && apt-get install -y --no-install-recommends \
	git \
	ca-certificates
cd / && \
    wget https://www.open-mpi.org/software/ompi/v4.0/downloads/openmpi-4.0.0.tar.gz && \
    tar zxf openmpi-4.0.0.tar.gz && \
    cd openmpi-4.0.0  && \
    ./configure \
    --enable-orterun-prefix-by-default \
    --enable-openib-control-hdr-padding \
    --enable-openib-rdmacm-ibaddr \
    --enable-openib-rdmacm \
    --enable-btl-portals4-flow-control \
    --enable-opal-btl-usnic-unit-tests \
    --enable-timing \
    --with-cuda \
    --with-slurm \
    --with-verbs \
    --disable-getpwuid \
    CXX=g++ FORTRAN=gfortran --enable-mpi-cxx -enable-mpi-fortran --enable-cxx-exceptions && \
    make -j $(nproc) all && \
    make install && \
    ldconfig
ldconfig /usr/local/cuda-9.0/targets/x86_64-linux/lib/stubs && \
    HOROVOD_GPU_ALLREDUCE=NCCL HOROVOD_WITH_TENSORFLOW=1 pip install --no-cache-dir horovod && \
    ldconfig
apt-get install -y --no-install-recommends openssh-client openssh-server && \
    mkdir -p /var/run/sshd
cat /etc/ssh/ssh_config | grep -v StrictHostKeyChecking > /etc/ssh/ssh_config.new && \
    echo "    StrictHostKeyChecking no" >> /etc/ssh/ssh_config.new && \
    mv /etc/ssh/ssh_config.new /etc/ssh/ssh_config
```

## Collection

 - Name: [Eric716/ericflow3](https://github.com/Eric716/ericflow3)
 - License: None

