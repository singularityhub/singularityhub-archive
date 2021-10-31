---
id: 12759
name: "mcw-rcc/xfce-ood-desktop"
branch: "master"
tag: "latest"
commit: "7302fc7ed79c2f9808814e463b29c7ef813e4c15"
version: "204d3287a8088055ed1882908e5b168da6060b9d9080954fd0574a41f7f73421"
build_date: "2020-11-21T20:33:49.056Z"
size_mb: 338.6328125
size: 355082240
sif: "https://datasets.datalad.org/shub/mcw-rcc/xfce-ood-desktop/latest/2020-11-21-7302fc7e-204d3287/204d3287a8088055ed1882908e5b168da6060b9d9080954fd0574a41f7f73421.sif"
url: https://datasets.datalad.org/shub/mcw-rcc/xfce-ood-desktop/latest/2020-11-21-7302fc7e-204d3287/
recipe: https://datasets.datalad.org/shub/mcw-rcc/xfce-ood-desktop/latest/2020-11-21-7302fc7e-204d3287/Singularity
collection: mcw-rcc/xfce-ood-desktop
---

# mcw-rcc/xfce-ood-desktop:latest

```bash
$ singularity pull shub://mcw-rcc/xfce-ood-desktop:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

%labels
Maintainer Matthew Flister

%help
This container includes Xfce desktop.

%environment 
    SHELL=/bin/bash
    export SHELL

%post
    # default mount points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts

    # Install necessary packages
    yum update -y && yum install -y epel-release
    yum -y groupinstall Xfce
    yum -y install xorg-x11-fonts-Type1 xorg-x11-fonts-misc
    yum clean all
```

## Collection

 - Name: [mcw-rcc/xfce-ood-desktop](https://github.com/mcw-rcc/xfce-ood-desktop)
 - License: [MIT License](https://api.github.com/licenses/mit)

