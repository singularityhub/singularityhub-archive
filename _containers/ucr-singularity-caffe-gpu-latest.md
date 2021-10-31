---
id: 1924
name: "ucr-singularity/caffe-gpu"
branch: "master"
tag: "latest"
commit: "47de8bc25df7353d31a1940683a418a8cdc49603"
version: "1cf092e9af39bd7f54e8104eb7ca05b3"
build_date: "2020-05-04T23:21:52.875Z"
size_mb: 3618
size: 1788268575
sif: "https://datasets.datalad.org/shub/ucr-singularity/caffe-gpu/latest/2020-05-04-47de8bc2-1cf092e9/1cf092e9af39bd7f54e8104eb7ca05b3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ucr-singularity/caffe-gpu/latest/2020-05-04-47de8bc2-1cf092e9/
recipe: https://datasets.datalad.org/shub/ucr-singularity/caffe-gpu/latest/2020-05-04-47de8bc2-1cf092e9/Singularity
collection: ucr-singularity/caffe-gpu
---

# ucr-singularity/caffe-gpu:latest

```bash
$ singularity pull shub://ucr-singularity/caffe-gpu:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bvlc/caffe:gpu

%post
# Update list of packages and install packages for ease of use.
apt-get update
apt-get install -y apt-utils
apt-get install -y vim
apt-get install -y tmux screen
apt-get install -y xterm
	
# Install for tkinter
apt-get install -y python-tk
#Install dependencies for caffe
apt-get install -y libxcb-xfixes0-dev

# OpenCV from pip, including contrib.  This makes the install MUCH faster.
# See https://pypi.python.org/pypi/opencv-contrib-python for capabilities 
# and limitations.  
pip install --no-cache-dir opencv-contrib-python

# Installing imutils,dlib,progressbar for FACES projectt
pip install --no-cache-dir imutils
pip install --no-cache-dir dlib
pip install --no-cache-dir progressbar2
pip install --no-cache-dir lmdb
pip install --no-cache-dir flask
pip install --no-cache-dir flask_cors
pip install --no-cache-dir sklearn
```

## Collection

 - Name: [ucr-singularity/caffe-gpu](https://github.com/ucr-singularity/caffe-gpu)
 - License: None

