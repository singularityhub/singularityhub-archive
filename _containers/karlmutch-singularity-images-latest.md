---
id: 836
name: "karlmutch/singularity-images"
branch: "master"
tag: "latest"
commit: "aedbeda3d1ecfbaf1f037839966be793311ffd53"
version: "eaeafd9b15d2e86bfc55082dac933858"
build_date: "2017-11-22T19:08:50.755Z"
size_mb: 622
size: 413757471
sif: "https://datasets.datalad.org/shub/karlmutch/singularity-images/latest/2017-11-22-aedbeda3-eaeafd9b/eaeafd9b15d2e86bfc55082dac933858.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/karlmutch/singularity-images/latest/2017-11-22-aedbeda3-eaeafd9b/
recipe: https://datasets.datalad.org/shub/karlmutch/singularity-images/latest/2017-11-22-aedbeda3-eaeafd9b/Singularity
collection: karlmutch/singularity-images
---

# karlmutch/singularity-images:latest

```bash
$ singularity pull shub://karlmutch/singularity-images:latest
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
```

## Collection

 - Name: [karlmutch/singularity-images](https://github.com/karlmutch/singularity-images)
 - License: None

