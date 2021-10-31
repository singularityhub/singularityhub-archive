---
id: 9604
name: "keceli/ffn"
branch: "master"
tag: "tf1.12"
commit: "c664ca2ff0f8cf9cb40ce02be7ca11adc8cb036f"
version: "51ec09270f8e8c78cd52b33ffaf4de8f"
build_date: "2019-06-06T09:15:15.412Z"
size_mb: 2402
size: 721670175
sif: "https://datasets.datalad.org/shub/keceli/ffn/tf1.12/2019-06-06-c664ca2f-51ec0927/51ec09270f8e8c78cd52b33ffaf4de8f.simg"
url: https://datasets.datalad.org/shub/keceli/ffn/tf1.12/2019-06-06-c664ca2f-51ec0927/
recipe: https://datasets.datalad.org/shub/keceli/ffn/tf1.12/2019-06-06-c664ca2f-51ec0927/Singularity
collection: keceli/ffn
---

# keceli/ffn:tf1.12

```bash
$ singularity pull shub://keceli/ffn:tf1.12
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%help
Centos7 with mkl_dnn tensorflow
ML/DL packages  : tensorflow keras torch sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm mpi4py horovod
Development kit : g++/gcc cython nvcc libqt4-dev python-dev
Utility kit     : git wget emacs vim openssh-client openmpi

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec THIS_CONTAINER.simg bash

%labels
Maintainer keceli,coreyjadams
Version centos7-mkldnn-tf1.11.0-torch0.4.1

#------------
# Global installation
#------------

%post

    yum update -y
    yum groupinstall -y "Development Tools"
    yum install -y epel-release
    yum install -y wget emacs vim 
    yum install -y PyQt4 PyQt4-devel
    yum install -y emacs vim openssh-clients zip 
    yum install -y python-devel python-pip  python-setuptools centos-release-scl
    yum install -y hdf5  rh-python36 python36-setuptools
    scl enable rh-python36 bash
    yum install -y easy_install-3.6 python36-pip
    # install MPICH
    wget -q http://www.mpich.org/static/downloads/3.2.1/mpich-3.2.1.tar.gz
    tar xf mpich-3.2.1.tar.gz
    rm mpich-3.2.1.tar.gz
    cd mpich-3.2.1
    # disable the addition of the RPATH to compiled executables
    # this allows us to override the MPI libraries to use those
    # found via LD_LIBRARY_PATH
    ./configure --prefix=/usr/local/mpich/install --disable-wrapper-rpath
    make -j 4 install
    export PATH=$PATH:/usr/local/mpich/install/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/mpich/install/lib
    env | sort
    cd ..
    rm -rf mpich-3.2.1

    pip3 --no-cache-dir --disable-pip-version-check install --upgrade setuptools 
    pip3 --no-cache-dir --disable-pip-version-check install 'matplotlib' 
    pip3 --no-cache-dir --disable-pip-version-check install 'ipython'    
    pip3 --no-cache-dir --disable-pip-version-check install 'ipykernel'
    pip3 --no-cache-dir --disable-pip-version-check install numpy wheel zmq six pygments pyyaml cython gputil psutil humanize h5py tqdm scipy seaborn tables
    pip3 --no-cache-dir --disable-pip-version-check install  pandas scikit-image scikit-learn Pillow opencv-python
    pip3 --no-cache-dir --disable-pip-version-check install jupyter notebook
    pip3 --no-cache-dir --disable-pip-version-check install cloud-volume

    # tensorflow with mkl-dnn:
    pip3 --no-cache-dir --disable-pip-version-check install intel-tensorflow==1.12.0

    # mpi and horovod
    pip --no-cache-dir --disable-pip-version-check install mpi4py
    HOROVOD_WITH_TENSORFLOW=1 pip --no-cache-dir --disable-pip-version-check install horovod==0.15.2
    
    # keras
    pip3 --no-cache-dir --disable-pip-version-check install keras
```

## Collection

 - Name: [keceli/ffn](https://github.com/keceli/ffn)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

