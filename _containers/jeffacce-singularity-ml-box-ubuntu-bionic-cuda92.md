---
id: 7642
name: "jeffacce/singularity-ml-box"
branch: "master"
tag: "ubuntu-bionic-cuda92"
commit: "e0743c33ec7f811b1f226b35218f53623d0b1160"
version: "905257ead482d989acf94460a55dde7e"
build_date: "2019-03-07T20:54:44.111Z"
size_mb: 5876
size: 2825228319
sif: "https://datasets.datalad.org/shub/jeffacce/singularity-ml-box/ubuntu-bionic-cuda92/2019-03-07-e0743c33-905257ea/905257ead482d989acf94460a55dde7e.simg"
url: https://datasets.datalad.org/shub/jeffacce/singularity-ml-box/ubuntu-bionic-cuda92/2019-03-07-e0743c33-905257ea/
recipe: https://datasets.datalad.org/shub/jeffacce/singularity-ml-box/ubuntu-bionic-cuda92/2019-03-07-e0743c33-905257ea/Singularity
collection: jeffacce/singularity-ml-box
---

# jeffacce/singularity-ml-box:ubuntu-bionic-cuda92

```bash
$ singularity pull shub://jeffacce/singularity-ml-box:ubuntu-bionic-cuda92
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.2-cudnn7-devel-ubuntu18.04

%post
        apt-get update
        apt-get install -y tmux vim wget curl
        apt-get install -y libglib2.0-0
        apt-get install -y python3.6 python3.6-dev python3.6-distutils
        apt update
        apt install -y libsm6 libxext6
        apt-get install -y libxrender-dev
        curl https://bootstrap.pypa.io/get-pip.py | python3.6
        pip3.6 --no-cache-dir install --upgrade pip
        pip3.6 --no-cache-dir install torch torchvision
        pip3.6 --no-cache-dir install h5py graphviz pydot
        pip3.6 --no-cache-dir install scipy numpy matplotlib scikit-learn pandas opencv-python opencv-contrib-python
        pip3.6 --no-cache-dir install ipdb imgaug jupyter notebook ipython jupyterlab
        pip3.6 --no-cache-dir install tensorflow-gpu
        pip3.6 --no-cache-dir install Keras
        pip3.6 --no-cache-dir install virtualenv tqdm seaborn requests
        pip3.6 --no-cache-dir install 'tornado>=4, <6'
        pip3.6 --no-cache-dir install tensorboardX

%startscript
        cd ~
        jupyter lab --ip=0.0.0.0 --port=3123
```

## Collection

 - Name: [jeffacce/singularity-ml-box](https://github.com/jeffacce/singularity-ml-box)
 - License: None

