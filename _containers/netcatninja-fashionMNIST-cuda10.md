---
id: 8980
name: "netcatninja/fashionMNIST"
branch: "master"
tag: "cuda10"
commit: "c39e1c89275b3cf1b211703b273c13f1a9ad856e"
version: "b26f38de175b5262b2d86f8e627a263c"
build_date: "2019-05-09T22:11:39.864Z"
size_mb: 8458
size: 5514649631
sif: "https://datasets.datalad.org/shub/netcatninja/fashionMNIST/cuda10/2019-05-09-c39e1c89-b26f38de/b26f38de175b5262b2d86f8e627a263c.simg"
url: https://datasets.datalad.org/shub/netcatninja/fashionMNIST/cuda10/2019-05-09-c39e1c89-b26f38de/
recipe: https://datasets.datalad.org/shub/netcatninja/fashionMNIST/cuda10/2019-05-09-c39e1c89-b26f38de/Singularity
collection: netcatninja/fashionMNIST
---

# netcatninja/fashionMNIST:cuda10

```bash
$ singularity pull shub://netcatninja/fashionMNIST:cuda10
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

%environment
    LD_LIBRARY_PATH=/usr/local/cuda/lib:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
    PATH=/usr/local/cuda/bin:/usr/sbin:/usr/bin:/sbin:/bin

%post
    sed -i 's/$/ universe/' /etc/apt/sources.list
    touch /usr/bin/nvidia-smi
    chmod +x /usr/bin/nvidia-smi
    mkdir -p /projects /scratch /opt
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
```

## Collection

 - Name: [netcatninja/fashionMNIST](https://github.com/netcatninja/fashionMNIST)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

