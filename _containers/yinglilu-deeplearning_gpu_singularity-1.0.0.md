---
id: 8967
name: "yinglilu/deeplearning_gpu_singularity"
branch: "master"
tag: "1.0.0"
commit: "d19c14fc6191da18fec0b04224afe5f031e8579f"
version: "2d811f0b650938aaab03f1914bfaa5a5"
build_date: "2021-03-09T02:54:02.249Z"
size_mb: 13591
size: 7488462879
sif: "https://datasets.datalad.org/shub/yinglilu/deeplearning_gpu_singularity/1.0.0/2021-03-09-d19c14fc-2d811f0b/2d811f0b650938aaab03f1914bfaa5a5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/yinglilu/deeplearning_gpu_singularity/1.0.0/2021-03-09-d19c14fc-2d811f0b/
recipe: https://datasets.datalad.org/shub/yinglilu/deeplearning_gpu_singularity/1.0.0/2021-03-09-d19c14fc-2d811f0b/Singularity
collection: yinglilu/deeplearning_gpu_singularity
---

# yinglilu/deeplearning_gpu_singularity:1.0.0

```bash
$ singularity pull shub://yinglilu/deeplearning_gpu_singularity:1.0.0
```

## Singularity Recipe

```singularity
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

conda install -c pytorch pytorch==1.0.1
conda install -c pytorch torchvision==0.2.1

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

