---
id: 8671
name: "Sylvia-Liang/torch25"
branch: "master"
tag: "latest"
commit: "0e4b3314f522d37849ca23879a560f71b7a52480"
version: "32a26b38559da9fab5a2eabc1834c8f1"
build_date: "2019-04-26T11:40:34.664Z"
size_mb: 8818
size: 4059226143
sif: "https://datasets.datalad.org/shub/Sylvia-Liang/torch25/latest/2019-04-26-0e4b3314-32a26b38/32a26b38559da9fab5a2eabc1834c8f1.simg"
url: https://datasets.datalad.org/shub/Sylvia-Liang/torch25/latest/2019-04-26-0e4b3314-32a26b38/
recipe: https://datasets.datalad.org/shub/Sylvia-Liang/torch25/latest/2019-04-26-0e4b3314-32a26b38/Singularity
collection: Sylvia-Liang/torch25
---

# Sylvia-Liang/torch25:latest

```bash
$ singularity pull shub://Sylvia-Liang/torch25:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:9.0-cudnn7-devel

# Add CUDA to the path
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/cuda/lib64
ENV CUDA_HOME /usr/local/cuda
ENV CPATH CUDA_HOME/include:$CPATH
ENV LD_LIBRARY_PATH $CUDA_HOME/lib64:$LD_LIBRARY_PATH
ENV PATH CUDA_HOME/bin:$PATH
ENV PATH /opt/conda/bin:$PATH	
WORKDIR /root

%post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this will install all necessary packages and prepare the container
    apt-get -y update --fix-missing


    # install other dependencies
    apt-get -y install --allow-downgrades --no-install-recommends \
        build-essential \
        dbus \
        wget \
        git \
        mercurial \
        subversion \
        vim \
        nano \
        cmake \
        bzip2 \
        ca-certificates \
        libglib2.0-0 \
        libxext6 \
        libsm6 \
        libxrender1 \
        libboost-all-dev\
	build-essential \
        cuda-command-line-tools-9-0 \
        cuda-cublas-9-0 \
        cuda-cufft-9-0 \
        cuda-curand-9-0 \
        cuda-cusolver-9-0 \
        cuda-cusparse-9-0 \
        curl \
        libfreetype6-dev \
        libhdf5-serial-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        python \
        python-dev \
        rsync \
        software-properties-common \
        unzip

#    locale-gen en_US
#    locale-gen en_US.UTF-8
#    locale update

#    system-machine-id-setup
    rm /etc/machine-id
    dbus-uuidgen --ensure=/etc/machine-id

    export CUDA_HOME="/usr/local/cuda"
    export CPATH="$CUDA_HOME/include:$CPATH"
    export LD_LIBRARY_PATH="$CUDA_HOME/lib64:$LD_LIBRARY_PATH"
    export PATH="$CUDA_HOME/bin:$PATH"
    export PATH="/opt/conda/bin:$PATH"
 
    
    export BOOST_ROOT=/usr/local/boost

    wget --quiet https://repo.continuum.io/archive/Anaconda2-5.2.0-Linux-x86_64.sh -O ~/anaconda.sh
    /bin/bash ~/anaconda.sh -b -p /opt/conda
    rm ~/anaconda.sh

    conda update conda 
    conda install \
        pyqt=5.6.0 \
        spyder==3.2.6 \
        qtconsole==4.3.1 \
        qtpy==1.3.1
    pip install --upgrade pip


    # install pytorch
    conda install pytorch=0.4.1 torchvision -c pytorch


    #cd ../python-package
    #python setup.py install


    #cd ../python-package
    #python setup.py install --gpu --precompile

    conda clean --index-cache --tarballs --packages --yes

    # user requests (contact marcc-help@marcc.jhu.edu)
    /opt/conda/bin/conda install opencv scikit-learn scikit-image scipy pandas 
    /opt/conda/bin/conda install -c anaconda numpy pytest flake8 
    /opt/conda/bin/conda install -c conda-forge tqdm protobuf onnx spectrum nibabel

    # try a pip install
    /opt/conda/bin/pip install torchtext
    /opt/conda/bin/pip install tqdm
    /opt/conda/bin/pip install anytree
    /opt/conda/bin/pip install backports.functools_lru_cache
    /opt/conda/bin/pip install bitarray
    /opt/conda/bin/pip install certifi
    /opt/conda/bin/pip install click
    /opt/conda/bin/pip install Flask
    /opt/conda/bin/pip install gevent
    /opt/conda/bin/pip install greenlet
    /opt/conda/bin/pip install interruptingcow
    /opt/conda/bin/pip install itsdangerous
    /opt/conda/bin/pip install Jinja2
    /opt/conda/bin/pip install MarkupSafe
    /opt/conda/bin/pip install pybloom
    /opt/conda/bin/pip install setuptools
    /opt/conda/bin/pip install subprocess32
    /opt/conda/bin/pip install ujson

%runscript
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this text code will run whenever the container
# is called as an executable or with `singularity run`
exec python $@

%help
This container is backed by Anaconda version 5.2.0 and provides the Python 2.7 bindings for:
    * Tensorflow 1.6.0
    * Keras 2.2.4
    * PyTorch 0.4.0
    * XGBoost
    * LightGBM
    * OpenCV
    * CUDA 9.0
    * CuDNN 7.0.5.15


%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container
    export CUDA_HOME="/usr/local/cuda"
    export CPATH="$CUDA_HOME/include:$CPATH"
    export LD_LIBRARY_PATH="$CUDA_HOME/lib64:$LD_LIBRARY_PATH"
    export PATH="$CUDA_HOME/bin:$PATH"

    export PATH="/opt/conda/bin:$PATH"
    unset CONDA_DEFAULT_ENV
    export ANACONDA_HOME=/opt/conda
```

## Collection

 - Name: [Sylvia-Liang/torch25](https://github.com/Sylvia-Liang/torch25)
 - License: None

