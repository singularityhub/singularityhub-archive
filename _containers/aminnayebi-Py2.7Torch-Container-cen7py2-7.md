---
id: 6716
name: "aminnayebi/Py2.7Torch-Container"
branch: "master"
tag: "cen7py2-7"
commit: "a60d14494ed2a26e54d43d74c9656b5cdbd3325b"
version: "eb399de5f5d0dc668e396cd583723220"
build_date: "2019-01-31T04:31:41.316Z"
size_mb: 860
size: 294289439
sif: "https://datasets.datalad.org/shub/aminnayebi/Py2.7Torch-Container/cen7py2-7/2019-01-31-a60d1449-eb399de5/eb399de5f5d0dc668e396cd583723220.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/aminnayebi/Py2.7Torch-Container/cen7py2-7/2019-01-31-a60d1449-eb399de5/
recipe: https://datasets.datalad.org/shub/aminnayebi/Py2.7Torch-Container/cen7py2-7/2019-01-31-a60d1449-eb399de5/Singularity
collection: aminnayebi/Py2.7Torch-Container
---

# aminnayebi/Py2.7Torch-Container:cen7py2-7

```bash
$ singularity pull shub://aminnayebi/Py2.7Torch-Container:cen7py2-7
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum wget
 
%setup
    # commands to be executed on host outside container during bootstrap
 
%post
    # commands to be executed inside container during bootstrap
 
    # yum needs some tlc to work properly in container
    RELEASEVER=7
    ARCH=x86_64
    echo $RELEASEVER > /etc/yum/vars/releasever
    echo $ARCH > /etc/yum/vars/arch
    wget https://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/epel-release-7-11.noarch.rpm
    rpm -ivh --nodeps epel-release-7-11.noarch.rpm
    # yum -d 10 check-update  # this line caused problems in testing
 
    # install other needed packages
    yum -y install man which tar gzip vim-minimal perl python python-dev python-pip util-linux
 
    # create bind points for NIH HPC environment
    mkdir -p /extra /rsgrps
 
    # download and run NIH HPC cuda for singularity installer
    wget ftp://helix.nih.gov/CUDA/cuda4singularity
    chmod 755 cuda4singularity
    ./cuda4singularity
    rm cuda4singularity
 
    # install tensorflow
    #pip install --upgrade pip
    #pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl
 
%runscript
    # commands to be executed when the container runs
 
%test
    # commands to be executed within container at close of bootstrap process
```

## Collection

 - Name: [aminnayebi/Py2.7Torch-Container](https://github.com/aminnayebi/Py2.7Torch-Container)
 - License: None

