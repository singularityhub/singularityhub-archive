---
id: 15897
name: "mahwisharif/singularity-cinnamon"
branch: "master"
tag: "latest"
commit: "28a805d5346f8aa8da862aff03149c6bc310d87e"
version: "1301be6c5b08296cceff2517662d7008"
build_date: "2021-04-15T16:36:16.307Z"
size_mb: 2061.0
size: 715456543
sif: "https://datasets.datalad.org/shub/mahwisharif/singularity-cinnamon/latest/2021-04-15-28a805d5-1301be6c/1301be6c5b08296cceff2517662d7008.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/mahwisharif/singularity-cinnamon/latest/2021-04-15-28a805d5-1301be6c/
recipe: https://datasets.datalad.org/shub/mahwisharif/singularity-cinnamon/latest/2021-04-15-28a805d5-1301be6c/Singularity
collection: mahwisharif/singularity-cinnamon
---

# mahwisharif/singularity-cinnamon:latest

```bash
$ singularity pull shub://mahwisharif/singularity-cinnamon:latest
```

## Singularity Recipe

```singularity
BootStrap:debootstrap 
OSVersion: xenial
MirrorURL:  http://us.archive.ubuntu.com/ubuntu/

%runscript
    echo "going to set up and install - please wait"
    echo "This is what happens when you run the container..."
    lsb_release -a
    echo "checking cmake version..."
    cmake --version
    echo "checking make version..."
    make --version
    echo "checking gcc version..."
    gcc --version
    echo "checking clang version..."
    clang --version
    echo "checking bison version..."
    bison --version
    echo "checking clang version"
%post
    apt-get install -y software-properties-common
    add-apt-repository universe
    apt-get update
    apt-get -y install sudo 
    apt-get -y install build-essential curl git man wget vim autoconf libtool bison flex cmake clang-3.8 libelf-dev libboost-all-dev libdwarf-dev zlib1g-dev libtbb-dev binutils-dev libiberty-dev
    apt -y install python
    apt-get clean
    git clone https://github.com/mahwisharif/Janus.git /home/Janus
    cd /home/Janus
    git checkout -b cinnamon origin/cinnamon
    cd /home
    wget https://software.intel.com/sites/landingpage/pintool/downloads/pin-3.13-98189-g60a6ef199-gcc-linux.tar.gz 
    mkdir -p /home/pin-3.13 && tar xvzf pin-3.13-98189-g60a6ef199-gcc-linux.tar.gz --directory /home/pin-3.13 --strip-components 1
    git clone https://github.com/mahwisharif/pin-cinnamon /home/pin-cinnamon
    cp -r /home/pin-cinnamon/MyDSLTool /home/pin-3.13/source/tools/
    rm /home/pin-3.13-98189-g60a6ef199-gcc-linux.tar.gz
    cd /home
    wget https://github.com/dyninst/dyninst/archive/v10.1.0.tar.gz
    mkdir -p /home/dyninst-10.1.0 && tar xzvf v10.1.0.tar.gz --directory /home/dyninst-10.1.0 --strip-components 1
    rm /home/v10.1.0.tar.gz
    cd /home
    git clone https://github.com/mahwisharif/dyn-cinnamon /home/dyn-cinnamon
    cp -r /home/dyn-cinnamon/MyDSLTool /home/dyninst-10.1.0/examples/
    git clone https://github.com/CompArchCam/Cinnamon.git /home/Cinnamon
    git clone https://github.com/mahwisharif/cinnamon-scripts.git /home/scripts 
%help

%test
 
%environment
```

## Collection

 - Name: [mahwisharif/singularity-cinnamon](https://github.com/mahwisharif/singularity-cinnamon)
 - License: None

