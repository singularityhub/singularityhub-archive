---
id: 8030
name: "mcw-rcc/mitograph"
branch: "master"
tag: "latest"
commit: "845cedfff7e5c1ed0bb1490f3c08fe01ca18bac4"
version: "50c348ee2b50f946a5be5fe8d4924a97"
build_date: "2019-03-29T19:18:16.083Z"
size_mb: 2495
size: 672595999
sif: "https://datasets.datalad.org/shub/mcw-rcc/mitograph/latest/2019-03-29-845cedff-50c348ee/50c348ee2b50f946a5be5fe8d4924a97.simg"
url: https://datasets.datalad.org/shub/mcw-rcc/mitograph/latest/2019-03-29-845cedff-50c348ee/
recipe: https://datasets.datalad.org/shub/mcw-rcc/mitograph/latest/2019-03-29-845cedff-50c348ee/Singularity
collection: mcw-rcc/mitograph
---

# mcw-rcc/mitograph:latest

```bash
$ singularity pull shub://mcw-rcc/mitograph:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels
    Maintainer Matthew Flister

%help
    This container runs Mitograph.

%post
    # add paths
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/depts /rcc/stor1/projects
  
    apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc-multilib \
        cmake \
        wget \
        freeglut3-dev \
        git \
        ca-certificates
    apt-get clean

    wget https://www.vtk.org/files/release/8.2/VTK-8.2.0.tar.gz
    tar -xvf VTK-8.2.0.tar.gz && cd VTK-8.2.0
    mkdir build && cd build
    cmake .. && make && make install
    cd ~/ && rm -rf VTK-8.2.0*

    git clone https://github.com/vianamp/MitoGraph.git
    cd MitoGraph && sed -i 's/VTK 7.0/VTK 8.2.0/g' CMakeLists.txt
    mkdir build && cd build
    cmake .. && make && cp MitoGraph /usr/local/bin
    cd ~/ && rm -rf MitoGraph
```

## Collection

 - Name: [mcw-rcc/mitograph](https://github.com/mcw-rcc/mitograph)
 - License: None

