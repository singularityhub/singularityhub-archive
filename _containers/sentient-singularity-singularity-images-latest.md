---
id: 865
name: "sentient-singularity/singularity-images"
branch: "master"
tag: "latest"
commit: "ff8be9b4fa2c51a3db44643ba7a8686b43518886"
version: "05f5e206952d312c440ac0fe4a13ea0d"
build_date: "2017-11-21T18:32:11.686Z"
size_mb: 1499
size: 808738847
sif: "https://datasets.datalad.org/shub/sentient-singularity/singularity-images/latest/2017-11-21-ff8be9b4-05f5e206/05f5e206952d312c440ac0fe4a13ea0d.simg"
url: https://datasets.datalad.org/shub/sentient-singularity/singularity-images/latest/2017-11-21-ff8be9b4-05f5e206/
recipe: https://datasets.datalad.org/shub/sentient-singularity/singularity-images/latest/2017-11-21-ff8be9b4-05f5e206/Singularity
collection: sentient-singularity/singularity-images
---

# sentient-singularity/singularity-images:latest

```bash
$ singularity pull shub://sentient-singularity/singularity-images:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
DistType "debian"
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

#
# To build an image from this definition file the following command could be used
#
#   sudo singularity build test.img minimal_cuda.def
#
# To run the result image from the build use a command such as the following
#
#   sudo singularity exec -B /usr/local/cuda:/usr/local/cuda -B /usr/lib/nvidia-384:/usr/lib/nvidia-384 --nv test.img bash
#

%runscript
    echo "This is what happens when you run the container..."

%environment
    LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia-384:/usr/local/cuda/lib64
    export LD_LIBRARY_PATH

%post
    cat <<EOT >>/etc/apt/sources.list
deb http://archive.ubuntu.com/ubuntu xenial universe multiverse
deb-src http://archive.ubuntu.com/ubuntu xenial universe multiverse

deb http://us.archive.ubuntu.com/ubuntu/ xenial universe
deb-src http://us.archive.ubuntu.com/ubuntu/ xenial universe
deb http://us.archive.ubuntu.com/ubuntu/ xenial-updates universe
deb-src http://us.archive.ubuntu.com/ubuntu/ xenial-updates universe

deb http://us.archive.ubuntu.com/ubuntu/ xenial multiverse
deb-src http://us.archive.ubuntu.com/ubuntu/ xenial multiverse
deb http://us.archive.ubuntu.com/ubuntu/ xenial-updates multiverse
deb-src http://us.archive.ubuntu.com/ubuntu/ xenial-updates multiverse

deb http://security.ubuntu.com/ubuntu xenial-security universe
deb-src http://security.ubuntu.com/ubuntu xenial-security universe
deb http://security.ubuntu.com/ubuntu xenial-security multiverse
deb-src http://security.ubuntu.com/ubuntu xenial-security multiverse
EOT
    apt-get -y install language-pack-en-base libgomp1 wget git
    wget --no-check-certificate https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
    dpkg -i cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
    apt-get update
    apt-get -y install --no-install-recommends gcc python2.7 python2.7-dev python3.5 python3.5-dev python-pip
    pip install --upgrade pip setuptools
    pip install tensorflow-gpu
```

## Collection

 - Name: [sentient-singularity/singularity-images](https://github.com/sentient-singularity/singularity-images)
 - License: None

