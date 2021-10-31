---
id: 3220
name: "tyson-swetnam/blender-singularity"
branch: "master"
tag: "latest"
commit: "db9988d88774515dad184ab05f475b178199d5ed"
version: "811ad81a9b6382bd97ffb34a40a3d3fb"
build_date: "2020-08-27T08:26:51.716Z"
size_mb: 791
size: 301625375
sif: "https://datasets.datalad.org/shub/tyson-swetnam/blender-singularity/latest/2020-08-27-db9988d8-811ad81a/811ad81a9b6382bd97ffb34a40a3d3fb.simg"
url: https://datasets.datalad.org/shub/tyson-swetnam/blender-singularity/latest/2020-08-27-db9988d8-811ad81a/
recipe: https://datasets.datalad.org/shub/tyson-swetnam/blender-singularity/latest/2020-08-27-db9988d8-811ad81a/Singularity
collection: tyson-swetnam/blender-singularity
---

# tyson-swetnam/blender-singularity:latest

```bash
$ singularity pull shub://tyson-swetnam/blender-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/opengl:1.1-glvnd-runtime-ubuntu16.04

%runscript
    exec echo "Starting Blender"
    exec blender
%setup
    echo "Looking in directory '$SINGULARITY_ROOTFS' for /bin/sh"
        if [ ! -x "$SINGULARITY_ROOTFS/bin/sh" ]; then
            echo "Hrmm, this container does not have /bin/sh installed..."
            exit 1
        fi
    exit 0

%post
    echo "deb http://us.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse" >> /etc/apt/sources.list

    apt-get update
    apt-get -y upgrade
    apt-get install -y vim nano lshw lsb-release bash-completion kmod iputils-ping net-tools wget

    wget https://sourceforge.net/projects/virtualgl/files/2.5.2/virtualgl_2.5.2_amd64.deb/download -O /tmp/virtualgl_2.5.2_amd64.deb
    apt-get -y install mesa-utils mesa-utils-extra x11-apps
    dpkg -i /tmp/virtualgl_2.5.2_amd64.deb
    
    # Install Blender & Meshlab
    apt-get install -y blender meshlab
```

## Collection

 - Name: [tyson-swetnam/blender-singularity](https://github.com/tyson-swetnam/blender-singularity)
 - License: None

