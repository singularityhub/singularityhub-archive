---
id: 12011
name: "MephistophelesUCR/Research"
branch: "master"
tag: "latest"
commit: "52822743fcbd6b44d8545026d2f965e2141526cf"
version: "5ae793e9703740679935ea1cfdfe4658"
build_date: "2020-01-15T23:24:19.254Z"
size_mb: 3616.0
size: 1792864287
sif: "https://datasets.datalad.org/shub/MephistophelesUCR/Research/latest/2020-01-15-52822743-5ae793e9/5ae793e9703740679935ea1cfdfe4658.sif"
url: https://datasets.datalad.org/shub/MephistophelesUCR/Research/latest/2020-01-15-52822743-5ae793e9/
recipe: https://datasets.datalad.org/shub/MephistophelesUCR/Research/latest/2020-01-15-52822743-5ae793e9/Singularity
collection: MephistophelesUCR/Research
---

# MephistophelesUCR/Research:latest

```bash
$ singularity pull shub://MephistophelesUCR/Research:latest
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

 - Name: [MephistophelesUCR/Research](https://github.com/MephistophelesUCR/Research)
 - License: None

