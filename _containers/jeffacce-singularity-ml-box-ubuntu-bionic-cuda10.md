---
id: 7646
name: "jeffacce/singularity-ml-box"
branch: "master"
tag: "ubuntu-bionic-cuda10"
commit: "c4184e68478748f85684ea6ae9143edcd322cb9e"
version: "5e28108d69c1016ef04095b53fa198e2"
build_date: "2019-09-25T04:31:35.290Z"
size_mb: 6270
size: 3132313631
sif: "https://datasets.datalad.org/shub/jeffacce/singularity-ml-box/ubuntu-bionic-cuda10/2019-09-25-c4184e68-5e28108d/5e28108d69c1016ef04095b53fa198e2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jeffacce/singularity-ml-box/ubuntu-bionic-cuda10/2019-09-25-c4184e68-5e28108d/
recipe: https://datasets.datalad.org/shub/jeffacce/singularity-ml-box/ubuntu-bionic-cuda10/2019-09-25-c4184e68-5e28108d/Singularity
collection: jeffacce/singularity-ml-box
---

# jeffacce/singularity-ml-box:ubuntu-bionic-cuda10

```bash
$ singularity pull shub://jeffacce/singularity-ml-box:ubuntu-bionic-cuda10
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

%post
        apt-get update
        apt-get install -y tmux vim wget curl
        apt-get install -y python3.6 python3.6-dev python3.6-distutils
        apt-get install -y libglib2.0-0
        apt update
        apt install -y libsm6 libxext6
        apt-get install -y libxrender-dev
        curl https://bootstrap.pypa.io/get-pip.py | python3.6
        pip3.6 --no-cache-dir install --upgrade pip
        pip3.6 --no-cache-dir install https://download.pytorch.org/whl/cu100/torch-1.0.0-cp36-cp36m-linux_x86_64.whl
        pip3.6 --no-cache-dir install torchvision
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
        nohup jupyter lab --ip=0.0.0.0 --port=3123 &
```

## Collection

 - Name: [jeffacce/singularity-ml-box](https://github.com/jeffacce/singularity-ml-box)
 - License: None

