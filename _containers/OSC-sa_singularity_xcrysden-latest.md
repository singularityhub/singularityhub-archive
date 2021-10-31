---
id: 13366
name: "OSC/sa_singularity_xcrysden"
branch: "master"
tag: "latest"
commit: "ac6503e6d9369521e36e72afc99c3743391450a1"
version: "90664932264aea943741ba70dff86742"
build_date: "2021-03-17T20:18:27.192Z"
size_mb: 352.0
size: 126644255
sif: "https://datasets.datalad.org/shub/OSC/sa_singularity_xcrysden/latest/2021-03-17-ac6503e6-90664932/90664932264aea943741ba70dff86742.sif"
url: https://datasets.datalad.org/shub/OSC/sa_singularity_xcrysden/latest/2021-03-17-ac6503e6-90664932/
recipe: https://datasets.datalad.org/shub/OSC/sa_singularity_xcrysden/latest/2021-03-17-ac6503e6-90664932/Singularity
collection: OSC/sa_singularity_xcrysden
---

# OSC/sa_singularity_xcrysden:latest

```bash
$ singularity pull shub://OSC/sa_singularity_xcrysden:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%labels
    Maintainer zyou@osc.edu
    Recipe https://github.com/OSC/sa_singularity_xcrysden

%help

    Container with pre-built XCrysDen for Ubuntu 18.04

%environment
    export PATH=$PATH:/usr/local/xcrysden/1.6.2

%post
    apt update
    apt upgrade -y
    DEBIAN_FRONTEND=noninteractive apt install -y \
	wget tk libglu1-mesa libtogl2 libfftw3-3 libxmu6 imagemagick openbabel libgfortran5
    wget http://www.xcrysden.org/download/xcrysden-1.6.2-linux_x86_64-shared.tar.gz 
    mkdir -p /usr/local/xcrysden/1.6.2
    tar xf xcrysden-1.6.2-linux_x86_64-shared.tar.gz -C /usr/local/xcrysden/1.6.2 --strip=1
    rm -f xcrysden-1.6.2-linux_x86_64-shared.tar.gz 
    apt autoclean
    apt autoremove --purge -y
    rm -rf /var/lib/apt/lists/*

%runscript
    exec xcrysden "$@"
```

## Collection

 - Name: [OSC/sa_singularity_xcrysden](https://github.com/OSC/sa_singularity_xcrysden)
 - License: [MIT License](https://api.github.com/licenses/mit)

