---
id: 7821
name: "yinglilu/deeplearning_cpu_singularity"
branch: "master"
tag: "latest"
commit: "abfc1108e371193fc083493443ef90c9e1faddad"
version: "02ce09c83d2a20061ed106a61b5e899a"
build_date: "2019-04-04T22:58:11.236Z"
size_mb: 5728
size: 2489720863
sif: "https://datasets.datalad.org/shub/yinglilu/deeplearning_cpu_singularity/latest/2019-04-04-abfc1108-02ce09c8/02ce09c83d2a20061ed106a61b5e899a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/yinglilu/deeplearning_cpu_singularity/latest/2019-04-04-abfc1108-02ce09c8/
recipe: https://datasets.datalad.org/shub/yinglilu/deeplearning_cpu_singularity/latest/2019-04-04-abfc1108-02ce09c8/Singularity
collection: yinglilu/deeplearning_cpu_singularity
---

# yinglilu/deeplearning_cpu_singularity:latest

```bash
$ singularity pull shub://yinglilu/deeplearning_cpu_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
#Python version: 3.6.4 
#From: continuumio/anaconda3:5.1.0

#Python version: 3.6.8
From: continuumio/miniconda3:4.5.4

%post
export PATH=/opt/conda/bin:$PATH

#DRYRUN=--dry-run
DRYRUN=

#update
apt-get update
conda update conda
pip install --upgrade pip

#tensorflow
conda install $DRYRUN tensorflow==1.12.0
conda install -c anaconda scikit-image==0.14.2

#pytorch
conda install $DRYRUN -c pytorch pytorch-cpu==1.0.1
conda install $DRYRUN -c pytorch torchvision-cpu==0.2.1

#theano
apt-get install -y build-essential
conda install $DRYRUN -c conda-forge theano==1.0.4
conda install mkl-service

#mxnet
#install opencv automatically
#conda install $DRYRUN mxnet==1.1.0

#sonnet
#conda install $DRYRUN -c hcc dm-sonnet==1.27

#opencv
conda install $DRYRUN -c anaconda opencv==3.4.2

#scikit-learn
conda install $DRYRUN -c anaconda scikit-learn==0.20.3

#simpleitk
conda install $DRYRUN -c simpleitk simpleitk==1.2.0

#niftynet
conda install -c anaconda pyyaml==3.13
pip install niftynet==0.5.0
```

## Collection

 - Name: [yinglilu/deeplearning_cpu_singularity](https://github.com/yinglilu/deeplearning_cpu_singularity)
 - License: None

