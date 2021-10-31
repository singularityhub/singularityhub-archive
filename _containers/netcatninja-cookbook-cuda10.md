---
id: 8993
name: "netcatninja/cookbook"
branch: "master"
tag: "cuda10"
commit: "b1026b29202db971316587e067a9b5c6b485fd2a"
version: "fefd2f84eac21326b8784610c745358a"
build_date: "2019-10-15T14:42:29.703Z"
size_mb: 11973
size: 7632044063
sif: "https://datasets.datalad.org/shub/netcatninja/cookbook/cuda10/2019-10-15-b1026b29-fefd2f84/fefd2f84eac21326b8784610c745358a.simg"
url: https://datasets.datalad.org/shub/netcatninja/cookbook/cuda10/2019-10-15-b1026b29-fefd2f84/
recipe: https://datasets.datalad.org/shub/netcatninja/cookbook/cuda10/2019-10-15-b1026b29-fefd2f84/Singularity
collection: netcatninja/cookbook
---

# netcatninja/cookbook:cuda10

```bash
$ singularity pull shub://netcatninja/cookbook:cuda10
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%runscript
    echo "/usr/local/cuda/bin/nvcc --version"
    /usr/local/cuda/bin/nvcc  --version
    echo "nvcc --version"
    nvcc --version
    python3 /opt/fashionmnist.py
    
%files
    fashionmnist.py /opt

%environment
    LD_LIBRARY_PATH=/usr/local/cuda/lib:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
    PATH=/usr/local/cuda/bin:/usr/sbin:/usr/bin:/sbin:/bin

%post
    sed -i 's/$/ universe/' /etc/apt/sources.list
    touch /usr/bin/nvidia-smi
    chmod +x /usr/bin/nvidia-smi
    mkdir -p /opt
    apt-get -y update && \
    apt-get -y install curl emacs ffmpeg git htop less libffi-dev libssl-dev man  module-init-tools openjdk-8-jdk python-dev python-numpy python-pip  python-tk tmux virtualenv wget python3-dev python3-pip

   ## Install CUDA 10.0
   # Add NVIDIA package repositories
    mkdir -p /opt/tmp && cd /opt/tmp && \
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.0.130-1_amd64.deb && \
    dpkg -i cuda-repo-ubuntu1804_10.0.130-1_amd64.deb && \
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub && \
    apt-get -y update && \
    wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb && \
    apt-get -y update &&  dpkg -i  nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb  && \
    apt-get -y update && \
    apt-get install -y --no-install-recommends cuda-10-0 libcudnn7=7.4.1.5-1+cuda10.0 libcudnn7-dev=7.4.1.5-1+cuda10.0 && 
    apt-get install -y nvinfer-runtime-trt-repo-ubuntu1804-5.0.2-ga-cuda10.0 && apt-get -y update && \
    apt-get install -y --no-install-recommends libnvinfer-dev

    ## pip3 install
    pip3 install matplotlib tensorflow-gpu==2.0.0-alpha0 torch torchvision
```

## Collection

 - Name: [netcatninja/cookbook](https://github.com/netcatninja/cookbook)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

