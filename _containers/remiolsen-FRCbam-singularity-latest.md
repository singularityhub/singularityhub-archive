---
id: 617
name: "remiolsen/FRCbam-singularity"
branch: "master"
tag: "latest"
commit: "a0907801ca70ba0bb321b5189d480f5c173d3bb1"
version: "c09bc96df7a3eb1f2404d4710a4fac46"
build_date: "2017-10-30T16:11:34.719Z"
size_mb: 1033
size: 314036255
sif: "https://datasets.datalad.org/shub/remiolsen/FRCbam-singularity/latest/2017-10-30-a0907801-c09bc96d/c09bc96df7a3eb1f2404d4710a4fac46.simg"
url: https://datasets.datalad.org/shub/remiolsen/FRCbam-singularity/latest/2017-10-30-a0907801-c09bc96d/
recipe: https://datasets.datalad.org/shub/remiolsen/FRCbam-singularity/latest/2017-10-30-a0907801-c09bc96d/Singularity
collection: remiolsen/FRCbam-singularity
---

# remiolsen/FRCbam-singularity:latest

```bash
$ singularity pull shub://remiolsen/FRCbam-singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:9

%label
    Maintainer remi-andre.olsen@scilifelab.se

%post
    apt-get update
    apt-get install -y git build-essential cmake libboost1.62-all-dev zlib1g-dev

    git clone https://github.com/vezzi/FRC_align.git
    cd FRC_align
    mkdir build
    cd build
    cmake ..
    make

    cp lib/bamtools/src/api/libbamtools.so* /lib
    cp ../bin/FRC /bin

    apt-get clean
    rm -rf /var/lib/apt/lists/*

    #UPPMAX stuff NOTE: Only testing for now, should use singulary run -B /sw:/sw etc container.img
    mkdir /sw
    mkdir /proj
    mkdir /pica
    mkdir /lupus

%runscript
    exec FRC "$@"
```

## Collection

 - Name: [remiolsen/FRCbam-singularity](https://github.com/remiolsen/FRCbam-singularity)
 - License: None

