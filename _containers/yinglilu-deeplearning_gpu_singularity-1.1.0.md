---
id: 9603
name: "yinglilu/deeplearning_gpu_singularity"
branch: "master"
tag: "1.1.0"
commit: "619b310af0c288f7ef4ff65c6503e737976aef34"
version: "b6a63fcbe0371a9d251d68a88b72e3e2"
build_date: "2020-03-13T14:57:25.455Z"
size_mb: 13014
size: 7015391263
sif: "https://datasets.datalad.org/shub/yinglilu/deeplearning_gpu_singularity/1.1.0/2020-03-13-619b310a-b6a63fcb/b6a63fcbe0371a9d251d68a88b72e3e2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/yinglilu/deeplearning_gpu_singularity/1.1.0/2020-03-13-619b310a-b6a63fcb/
recipe: https://datasets.datalad.org/shub/yinglilu/deeplearning_gpu_singularity/1.1.0/2020-03-13-619b310a-b6a63fcb/Singularity
collection: yinglilu/deeplearning_gpu_singularity
---

# yinglilu/deeplearning_gpu_singularity:1.1.0

```bash
$ singularity pull shub://yinglilu/deeplearning_gpu_singularity:1.1.0
```

## Singularity Recipe

```singularity
#-----------------------
#updates:

# 2019-06-05
# pytorch 1.1.0
#-----------------------

Bootstrap: docker
#Python version: 3.6.4 
From: continuumio/anaconda3:5.1.0

%post
export PATH=/opt/conda/bin:$PATH

#update
apt-get update
apt-get install -y tree
conda update conda
pip install --upgrade pip

#tensorflow
conda install tensorflow-gpu==1.12.0
# conda install -c anaconda scikit-image==0.14.2

#pytorch
conda install -c pytorch pytorch==1.1.0 torchvision==0.3.0 cudatoolkit=9.0

#theano
#apt-get install -y build-essential
#conda install -c conda-forge theano==1.0.4
#conda install mkl-service

#opencv
conda install -c anaconda opencv==3.4.2

#scikit-learn
conda install -c anaconda scikit-learn==0.20.3

#simpleitk
conda install -c simpleitk simpleitk==1.2.0

#niftynet
conda install -c anaconda pyyaml==3.13
pip install niftynet==0.5.0

#niwidgets
pip install niwidgets==0.1.3
```

## Collection

 - Name: [yinglilu/deeplearning_gpu_singularity](https://github.com/yinglilu/deeplearning_gpu_singularity)
 - License: None

