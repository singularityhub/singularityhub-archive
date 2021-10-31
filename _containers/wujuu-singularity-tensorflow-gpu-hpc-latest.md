---
id: 4959
name: "wujuu/singularity-tensorflow-gpu-hpc"
branch: "master"
tag: "latest"
commit: "17d3ea3434e3bdf9d6b3278071c2f64ca063883d"
version: "b121ed6c4c7c612aef99526fd654b43b"
build_date: "2018-09-24T12:27:05.647Z"
size_mb: 2981
size: 1629249567
sif: "https://datasets.datalad.org/shub/wujuu/singularity-tensorflow-gpu-hpc/latest/2018-09-24-17d3ea34-b121ed6c/b121ed6c4c7c612aef99526fd654b43b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/wujuu/singularity-tensorflow-gpu-hpc/latest/2018-09-24-17d3ea34-b121ed6c/
recipe: https://datasets.datalad.org/shub/wujuu/singularity-tensorflow-gpu-hpc/latest/2018-09-24-17d3ea34-b121ed6c/Singularity
collection: wujuu/singularity-tensorflow-gpu-hpc
---

# wujuu/singularity-tensorflow-gpu-hpc:latest

```bash
$ singularity pull shub://wujuu/singularity-tensorflow-gpu-hpc:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%environment
    SHELL=/bin/bash
    export SHELL

%files
    tensorflow_demo.py 


%post
    apt -y update
    apt -y install wget
    apt -y install gnupg
    apt -y install gnupg1
    apt -y install gnupg2



    apt -y install python3
    apt -y install python3-pip
    

    
    # Add NVIDIA package repository
    apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
    wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_9.1.85-1_amd64.deb
    apt -y install ./cuda-repo-ubuntu1604_9.1.85-1_amd64.deb
    wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb
    apt -y install ./nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb
    apt -y update

    # Install CUDA and tools. Include optional NCCL 2.x
    apt -y install cuda9.0 cuda-cublas-9-0 cuda-cufft-9-0 cuda-curand-9-0 \
        cuda-cusolver-9-0 cuda-cusparse-9-0 libcudnn7=7.2.1.38-1+cuda9.0 \
        libnccl2=2.2.13-1+cuda9.0 cuda-command-line-tools-9-0

    # Optional: Install the TensorRT runtime (must be after CUDA install)
    apt -y update
    apt -y install libnvinfer4=4.1.2-1+cuda9.0

    pip3 install tensorflow-gpu

%runscript
	python3 /tensorflow_demo.py
```

## Collection

 - Name: [wujuu/singularity-tensorflow-gpu-hpc](https://github.com/wujuu/singularity-tensorflow-gpu-hpc)
 - License: None

