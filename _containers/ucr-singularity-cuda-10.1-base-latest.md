---
id: 8921
name: "ucr-singularity/cuda-10.1-base"
branch: "master"
tag: "latest"
commit: "c2caae1eb71d69efc0810dea0573771d1c0cdb17"
version: "e895f39d17b32a24d87475c05a078080"
build_date: "2021-04-15T16:29:08.410Z"
size_mb: 3953
size: 2146115615
sif: "https://datasets.datalad.org/shub/ucr-singularity/cuda-10.1-base/latest/2021-04-15-c2caae1e-e895f39d/e895f39d17b32a24d87475c05a078080.simg"
url: https://datasets.datalad.org/shub/ucr-singularity/cuda-10.1-base/latest/2021-04-15-c2caae1e-e895f39d/
recipe: https://datasets.datalad.org/shub/ucr-singularity/cuda-10.1-base/latest/2021-04-15-c2caae1e-e895f39d/Singularity
collection: ucr-singularity/cuda-10.1-base
---

# ucr-singularity/cuda-10.1-base:latest

```bash
$ singularity pull shub://ucr-singularity/cuda-10.1-base:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

%post

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

    # Clean up
    apt-get -y autoremove
    rm -rvf /var/lib/apt/lists/*
```

## Collection

 - Name: [ucr-singularity/cuda-10.1-base](https://github.com/ucr-singularity/cuda-10.1-base)
 - License: None

