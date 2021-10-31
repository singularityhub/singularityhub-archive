---
id: 12296
name: "lizolson1/example"
branch: "master"
tag: "latest"
commit: "7f0034d214ca99e27448a74d317a7779f7dbf225"
version: "1df7d62bd10f726b3534e86a7dfd050b"
build_date: "2020-02-18T01:35:35.875Z"
size_mb: 15243.0
size: 7752527903
sif: "https://datasets.datalad.org/shub/lizolson1/example/latest/2020-02-18-7f0034d2-1df7d62b/1df7d62bd10f726b3534e86a7dfd050b.sif"
url: https://datasets.datalad.org/shub/lizolson1/example/latest/2020-02-18-7f0034d2-1df7d62b/
recipe: https://datasets.datalad.org/shub/lizolson1/example/latest/2020-02-18-7f0034d2-1df7d62b/Singularity
collection: lizolson1/example
---

# lizolson1/example:latest

```bash
$ singularity pull shub://lizolson1/example:latest
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
apt-get install -y vim
conda update conda
pip install --upgrade pip

##tensorflow
#conda install tensorflow-gpu==1.13.0
conda install tensorflow-gpu==1.14.0

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

 - Name: [lizolson1/example](https://github.com/lizolson1/example)
 - License: None

