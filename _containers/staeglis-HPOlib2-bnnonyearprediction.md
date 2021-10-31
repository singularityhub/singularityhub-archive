---
id: 6417
name: "staeglis/HPOlib2"
branch: "container"
tag: "bnnonyearprediction"
commit: "75c324496a014c195755898d932a80c10e06407d"
version: "c488caf51bc0dce4b40eb6b44fe0879f"
build_date: "2019-02-26T20:10:20.970Z"
size_mb: 4313
size: 2512437279
sif: "https://datasets.datalad.org/shub/staeglis/HPOlib2/bnnonyearprediction/2019-02-26-75c32449-c488caf5/c488caf51bc0dce4b40eb6b44fe0879f.simg"
url: https://datasets.datalad.org/shub/staeglis/HPOlib2/bnnonyearprediction/2019-02-26-75c32449-c488caf5/
recipe: https://datasets.datalad.org/shub/staeglis/HPOlib2/bnnonyearprediction/2019-02-26-75c32449-c488caf5/Singularity
collection: staeglis/HPOlib2
---

# staeglis/HPOlib2:bnnonyearprediction

```bash
$ singularity pull shub://staeglis/HPOlib2:bnnonyearprediction
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

%labels
MAINTAINER Stefan Staeglich

%post
    apt update -y
    apt install git -y
    apt install libopenblas-base libopenblas-dev libblas3 liblas-c3 -y
    apt install python3-pip python3-numpy python-configparser -y
    pip3 install git+https://github.com/automl/ConfigSpace.git@master
    apt install python3-scipy -y
    pip3 install git+https://github.com/staeglis/HPOlib2@container
    pip3 install pyro4
    pip3 install Theano
    pip3 install git+https://github.com/Lasagne/Lasagne.git
    pip3 install git+https://github.com/automl/sgmcmc.git
    
    pip3 install cython
    apt install cmake gcc g++ -y
    git clone https://github.com/Theano/libgpuarray.git
    cd libgpuarray
    mkdir Build
    cd Build
    # you can pass -DCMAKE_INSTALL_PREFIX=/path/to/somewhere to install to an alternate location
    cmake .. -DCMAKE_BUILD_TYPE=Release # or Debug if you are investigating a crash
    make
    make install
    cd ..
    # This must be done after libgpuarray is installed as per instructions above.
    python3 setup.py build
    python3 setup.py install
    
    mkdir /var/lib/hpolib/
    python3 /usr/local/lib/python3.6/dist-packages/hpolib/container/util/download_data.py ml.bnn_benchmark BNNOnYearPrediction
    chmod -R 777 /var/lib/hpolib/

%environment
    export LD_LIBRARY_PATH=/usr/local/lib/:$LD_LIBRARY_PATH

%runscript
    python3 -s /usr/local/lib/python3.6/dist-packages/hpolib/container/server/abstract_benchmark.py ml.bnn_benchmark $@
```

## Collection

 - Name: [staeglis/HPOlib2](https://github.com/staeglis/HPOlib2)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

