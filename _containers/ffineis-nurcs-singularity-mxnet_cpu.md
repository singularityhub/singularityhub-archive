---
id: 3606
name: "ffineis/nurcs-singularity"
branch: "feature/mxnet_cpu"
tag: "mxnet_cpu"
commit: "2513d649760cd8113ed12a4aa2cc424f83016d37"
version: "314fe5d7c73501200f226469e36456bb"
build_date: "2018-07-20T04:10:47.274Z"
size_mb: 3810
size: 1353125919
sif: "https://datasets.datalad.org/shub/ffineis/nurcs-singularity/mxnet_cpu/2018-07-20-2513d649-314fe5d7/314fe5d7c73501200f226469e36456bb.simg"
url: https://datasets.datalad.org/shub/ffineis/nurcs-singularity/mxnet_cpu/2018-07-20-2513d649-314fe5d7/
recipe: https://datasets.datalad.org/shub/ffineis/nurcs-singularity/mxnet_cpu/2018-07-20-2513d649-314fe5d7/Singularity
collection: ffineis/nurcs-singularity
---

# ffineis/nurcs-singularity:mxnet_cpu

```bash
$ singularity pull shub://ffineis/nurcs-singularity:mxnet_cpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment

    # Set system locale
    export LC_ALL=C

%post

    # ------------------------------------------------ #
    #                   Kernel overhead                #
    # ------------------------------------------------ #

    apt-get -y update && apt-get -y upgrade
    apt-get -y --allow-unauthenticated install \
	apt-utils \
	apt-transport-https \
	autoconf \
	automake \
	build-essential \
	cmake \
	curl \
	git \
	gfortran \
	graphviz \
	libopenblas-dev \
	liblapack-dev \
	libcairo2-dev \
	libcurl4-openssl-dev \
	libtool \
	libssl-dev \
	libffi-dev \
	libgfortran3 \
	libopencv-dev \
	libxslt1-dev \
	libxml2-dev \
	libxt-dev \
	unzip \
	wget \
	zip \
	zlib1g-dev \
	pkg-config \
	python-dev \
	python-pip \
	python-tk \
	python-wheel \
	python-setuptools \
	python3-dev \
	python3-pip \
	python3-wheel \
	software-properties-common \
	python-software-properties

    # ------------------------------------------------ #
    #                  Build MXNet    	               #
    # ------------------------------------------------ #

    # move to /tmp for mxnet install; keep 
    cd /opt
	
    git clone --recursive https://github.com/apache/incubator-mxnet
    cd ./incubator-mxnet
    make -j $(nproc) USE_OPENCV=1 USE_BLAS=openblas

    # ------------------------------------------------ #
    #            MXNet: python bindings                #
    # ------------------------------------------------ #

    cd ./python
    pip install -e .
    pip install graphviz

    # ------------------------------------------------ #
    #                 R and its bindings               #
    # ------------------------------------------------ #

    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
    add-apt-repository 'deb [arch=amd64,i386] https://cran.rstudio.com/bin/linux/ubuntu xenial/'
    apt-get update
    apt-get -y --allow-unauthenticated install \
	r-base \
	r-base-dev

    cd ..
    R --version
    make rpkg

    # ------------------------------------------------ #
    #          Install DS/ML python packages           #
    # ------------------------------------------------ #

    pip install numpy # requisite for mlpy install
    pip install Cython \
	pandas \
	feather-format \
	mock \
	scipy \
	sklearn \
	matplotlib \
	mlpy \
	nose \
	nltk \
	statsmodels \
	opencv-python \
	biopython \
	seaborn

    pip3 install numpy
    pip3 install Cython \
	pandas \
	feather-format \
	mock \
	scipy \
	sklearn \
	matplotlib \
	ipython \
	nose \
	nltk \
	statsmodels \
	opencv-python \
	biopython \
	seaborn \
	graphviz

    # ------------------------------------------------ #
    #             Install R packages for DS            #
    # ------------------------------------------------ #

    Rscript --vanilla /opt/install_packages.r


%test

    python -c 'import mxnet as mx; print(mx.nd.ones((2, 3)))'
    Rscript -e 'library(mxnet); print(mx.nd.ones(c(2,3), ctx = mx.cpu()))'

%files

    install_packages.r /opt
    singularity_logo.txt /opt

%runscript

    cat /opt/singularity_logo.txt

%environment
```

## Collection

 - Name: [ffineis/nurcs-singularity](https://github.com/ffineis/nurcs-singularity)
 - License: None

