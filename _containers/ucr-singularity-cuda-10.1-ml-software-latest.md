---
id: 8964
name: "ucr-singularity/cuda-10.1-ml-software"
branch: "master"
tag: "latest"
commit: "fba85d57222a461f83f26484f314756d5af89c99"
version: "0fc82fee7d803f4c3ae6ccf17c3e1dcb"
build_date: "2020-02-25T19:35:42.009Z"
size_mb: 5772
size: 3083792415
sif: "https://datasets.datalad.org/shub/ucr-singularity/cuda-10.1-ml-software/latest/2020-02-25-fba85d57-0fc82fee/0fc82fee7d803f4c3ae6ccf17c3e1dcb.simg"
url: https://datasets.datalad.org/shub/ucr-singularity/cuda-10.1-ml-software/latest/2020-02-25-fba85d57-0fc82fee/
recipe: https://datasets.datalad.org/shub/ucr-singularity/cuda-10.1-ml-software/latest/2020-02-25-fba85d57-0fc82fee/Singularity
collection: ucr-singularity/cuda-10.1-ml-software
---

# ucr-singularity/cuda-10.1-ml-software:latest

```bash
$ singularity pull shub://ucr-singularity/cuda-10.1-ml-software:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ucrdocker/cuda-10.1-base

%post

    # Update list of available packages, then upgrade them

    apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get -y upgrade
    
    # Pytorch

    apt-get install -y python-pip
    pip install --no-cache-dir https://download.pytorch.org/whl/cu100/torch-1.1.0-cp27-cp27mu-linux_x86_64.whl
    pip install --no-cache-dir torchvision

    # OpenCV dependencies
    # ===================
 
    # Developer tools
    apt-get install -y build-essential cmake unzip pkg-config
    # Image files
    apt-get install -y libjpeg-dev libpng-dev libtiff-dev
    # Video
    apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
    apt-get install -y libxvidcore-dev libx264-dev
    # GTK for GUI
    apt-get install -y libgtk-3-dev
    # Optimization
    apt-get install -y libatlas-base-dev gfortran
    # Python dev tools
    apt-get install -y python3-dev

    # Clean up
    apt-get -y autoremove
    rm -rvf /var/lib/apt/lists/*
```

## Collection

 - Name: [ucr-singularity/cuda-10.1-ml-software](https://github.com/ucr-singularity/cuda-10.1-ml-software)
 - License: None

