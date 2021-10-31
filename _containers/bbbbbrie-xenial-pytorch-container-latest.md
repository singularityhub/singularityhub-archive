---
id: 2353
name: "bbbbbrie/xenial-pytorch-container"
branch: "master"
tag: "latest"
commit: "1003d9b59fd498e89866d187fc315819142b7d7a"
version: "6e93ba0ec20bdb577d4331917b634c3b"
build_date: "2019-11-04T15:14:17.062Z"
size_mb: 2765
size: 1364459551
sif: "https://datasets.datalad.org/shub/bbbbbrie/xenial-pytorch-container/latest/2019-11-04-1003d9b5-6e93ba0e/6e93ba0ec20bdb577d4331917b634c3b.simg"
url: https://datasets.datalad.org/shub/bbbbbrie/xenial-pytorch-container/latest/2019-11-04-1003d9b5-6e93ba0e/
recipe: https://datasets.datalad.org/shub/bbbbbrie/xenial-pytorch-container/latest/2019-11-04-1003d9b5-6e93ba0e/Singularity
collection: bbbbbrie/xenial-pytorch-container
---

# bbbbbrie/xenial-pytorch-container:latest

```bash
$ singularity pull shub://bbbbbrie/xenial-pytorch-container:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%runscript
    python3 /opt/main.py

%post
    echo "Hello from inside the container"
    sed -i 's/$/ universe/' /etc/apt/sources.list
    touch /usr/bin/nvidia-smi
    apt-get -y update
    apt-get -y --force-yes install blender fortune libxv1 libx11-6 lolcat python3 python3-pip python3-tk wget
    pip3 install --upgrade pip
    pip3 install gym jupyter lmdb matplotlib numpy pandas scipy six tqdm
    pip3 install http://download.pytorch.org/whl/cu80/torch-0.3.1-cp35-cp35m-linux_x86_64.whl 
    pip3 install torch torchvision    
    /usr/games/lolcat /etc/lsb-release
    /usr/games/fortune | /usr/games/lolcat
    wget -O /opt/main.py https://raw.githubusercontent.com/pytorch/examples/master/mnist/main.py
```

## Collection

 - Name: [bbbbbrie/xenial-pytorch-container](https://github.com/bbbbbrie/xenial-pytorch-container)
 - License: None

