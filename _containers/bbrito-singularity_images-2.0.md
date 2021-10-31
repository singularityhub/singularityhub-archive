---
id: 2758
name: "bbrito/singularity_images"
branch: "master"
tag: "2.0"
commit: "8ac63448fb7a51a7d4d7c782defea3945d7d15f7"
version: "0c0f9fd1607d5c1bacb2d9fefd0f4280"
build_date: "2018-10-15T17:10:04.000Z"
size_mb: 4092
size: 1361686559
sif: "https://datasets.datalad.org/shub/bbrito/singularity_images/2.0/2018-10-15-8ac63448-0c0f9fd1/0c0f9fd1607d5c1bacb2d9fefd0f4280.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bbrito/singularity_images/2.0/2018-10-15-8ac63448-0c0f9fd1/
recipe: https://datasets.datalad.org/shub/bbrito/singularity_images/2.0/2018-10-15-8ac63448-0c0f9fd1/Singularity
collection: bbrito/singularity_images
---

# bbrito/singularity_images:2.0

```bash
$ singularity pull shub://bbrito/singularity_images:2.0
```

## Singularity Recipe

```singularity
bootstrap:docker
From:ubuntu:16.04

%post

# to find pip
export PATH=/usr/local/bin:/usr/local/sbin:/bin:/usr/bin:/usr/sbin:/bin:/sbin

apt-get update && apt-get upgrade -y --allow-unauthenticated

export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y --allow-unauthenticated \
        build-essential \
        cmake \
        curl \
        git \
        libfreetype6-dev \
        libpng12-dev \
        libssl-dev \
        libzmq3-dev \
        module-init-tools \
        pkg-config \
        python \
	python-pip \
        python-dev \
        python-tk \
        python3 \
        python3-dev \
        python3-tk \
        rsync \
        software-properties-common \
        unzip \
        zip \
        zlib1g-dev \
        openjdk-8-jdk \
        openjdk-8-jre-headless \
        vim \
        wget \
        libxpm-dev

apt-get clean 
rm -rf /var/lib/apt/lists/*

# bazel is required for some TensorFlow projects
echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" >/etc/apt/sources.list.d/bazel.list
curl https://bazel.build/bazel-release.pub.gpg | apt-key add -

export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y --allow-unauthenticated \
        bazel

curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

pip --no-cache-dir install \
        h5py \
        ipykernel \
        jupyter \
        matplotlib \
        numpy \
        pandas \
        Pillow \
        scipy \
        sklearn \
        ipdb \
	opencv-python \
	opencv-contrib-python-headless \
	seaborn \
	attrdict==2.0.0 \
	six==1.11.0 \
	http://download.pytorch.org/whl/cpu/torch-0.4.1-cp27-cp27mu-linux_x86_64.whl \
	torchvision==0.2.1

python -m ipykernel.kernelspec

# Install TensorFlow
pip install tensorflow

# keras
pip install --upgrade keras


#############################
# now do the same for python3

curl -O https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    rm get-pip.py

pip3 --no-cache-dir install \
        h5py \
        ipykernel \
        jupyter \
        matplotlib \
        numpy \
        pandas \
        Pillow \
        scipy \
        sklearn \
	opencv-python \
	opencv-contrib-python-headless \
	attrdict==2.0.0 \
	six==1.11.0 \
	http://download.pytorch.org/whl/cpu/torch-0.4.1-cp35-cp35m-linux_x86_64.whl \
	torchvision==0.2.1

python3 -m ipykernel.kernelspec

# Install TensorFlow
pip3 install tensorflow

# keras
pip3 install --upgrade keras

# required directories
mkdir -p /cvmfs

# root
cd /opt && \
    wget -nv https://root.cern.ch/download/root_v6.10.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz && \
    tar xzf root_v6.10.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz && \
    rm -f root_v6.10.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz

# xrootd
cd /opt && \
    wget http://xrootd.org/download/v4.7.1/xrootd-4.7.1.tar.gz && \
    tar xzf xrootd-4.7.1.tar.gz && \
    cd xrootd-4.7.1 && \
    mkdir build && \
    cd  build && \
    cmake /opt/xrootd-4.7.1 -DCMAKE_INSTALL_PREFIX=/opt/xrootd -DENABLE_PERL=FALSE && \
    make && \
    make install && \
    cd /opt && \
    rm -rf xrootd-4.7.1.tar.gz xrootd-4.7.1

# stashcp
cd /opt && \
    git clone https://github.com/opensciencegrid/StashCache.git

# build info
echo "Timestamp:" `date --utc` | tee /image-build-info.txt
```

## Collection

 - Name: [bbrito/singularity_images](https://github.com/bbrito/singularity_images)
 - License: None

