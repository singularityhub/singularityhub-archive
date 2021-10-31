---
id: 9800
name: "bstriner/cuda-10.1-cudnn7-devel-ubuntu16.04"
branch: "master"
tag: "latest"
commit: "77457ec1616176b2d1a8381de5782eb666b837cb"
version: "6a875b0186820cae2a6da1e90fbe81a3"
build_date: "2020-04-23T14:58:00.000Z"
size_mb: 4095
size: 2281488415
sif: "https://datasets.datalad.org/shub/bstriner/cuda-10.1-cudnn7-devel-ubuntu16.04/latest/2020-04-23-77457ec1-6a875b01/6a875b0186820cae2a6da1e90fbe81a3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bstriner/cuda-10.1-cudnn7-devel-ubuntu16.04/latest/2020-04-23-77457ec1-6a875b01/
recipe: https://datasets.datalad.org/shub/bstriner/cuda-10.1-cudnn7-devel-ubuntu16.04/latest/2020-04-23-77457ec1-6a875b01/Singularity
collection: bstriner/cuda-10.1-cudnn7-devel-ubuntu16.04
---

# bstriner/cuda-10.1-cudnn7-devel-ubuntu16.04:latest

```bash
$ singularity pull shub://bstriner/cuda-10.1-cudnn7-devel-ubuntu16.04:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.1-cudnn7-devel-ubuntu16.04
#cuda-10.1-cudnn7-devel-ubuntu16.04
%environment
    LC_ALL=C
    export LC_ALL
%post
    export LC_ALL=C
    # Update list of available packages, then upgrade them
    apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get -y upgrade
    
    # Utility and support packages
    apt-get install -y screen terminator tmux vim wget 
    apt-get install -y aptitude build-essential cmake g++ gfortran git \
        pkg-config software-properties-common
    apt-get install -y unrar
    apt-get install -y ffmpeg
    apt-get install -y gnuplot-x11
```

## Collection

 - Name: [bstriner/cuda-10.1-cudnn7-devel-ubuntu16.04](https://github.com/bstriner/cuda-10.1-cudnn7-devel-ubuntu16.04)
 - License: None

