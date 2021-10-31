---
id: 3589
name: "ffineis/nurcs-singularity"
branch: "bugfix/shub_builds"
tag: "keras_cpu"
commit: "2a4c047b1e46b7cc63989f01ab928f40223253bf"
version: "a98bc1013af2ad3c7cf0a48dd7058275"
build_date: "2018-07-18T23:19:18.904Z"
size_mb: 3068
size: 1143869471
sif: "https://datasets.datalad.org/shub/ffineis/nurcs-singularity/keras_cpu/2018-07-18-2a4c047b-a98bc101/a98bc1013af2ad3c7cf0a48dd7058275.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ffineis/nurcs-singularity/keras_cpu/2018-07-18-2a4c047b-a98bc101/
recipe: https://datasets.datalad.org/shub/ffineis/nurcs-singularity/keras_cpu/2018-07-18-2a4c047b-a98bc101/Singularity
collection: ffineis/nurcs-singularity
---

# ffineis/nurcs-singularity:keras_cpu

```bash
$ singularity pull shub://ffineis/nurcs-singularity:keras_cpu
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
	autoconf \
	automake \
	build-essential \
	cmake \
	curl \
	git \
	gfortran \
	libtool \
	libssl-dev \
	libffi-dev \
	libopencv-dev \
	libxslt1-dev \
	pkg-config \
	python-dev \
	python-pip \
	python-tk \
	python-wheel \
	unzip \
	wget \
	zip \
	zlib1g-dev

    # ------------------------------------------------ #
    #                   TF for python2                 #
    # ------------------------------------------------ #

    # python2 TF/data science package dependencies
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

    pip install tensorflow==1.8
    pip install keras==2.2.0

    # ------------------------------------------------ #
    #                   TF for python3                 #
    # ------------------------------------------------ #

    apt-get -y --allow-unauthenticated install \
	libxml2-dev \
	python3-dev \
	python3-pip \
	python3-wheel

    pip3 install numpy # requisite for mlpy install
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
	seaborn

    pip3 install tensorflow==1.8
    pip3 install keras==2.2.0

%test

    # python2
    python /opt/tf_mnist_deep.py
    python /opt/keras_lstm.py

    # python3
    python3 /opt/tf_mnist_deep.py
    python3 /opt/keras_lstm.py

%files

    singularity_logo.txt /opt
    tf_mnist_deep.py /opt
    keras_lstm.py /opt

%runscript

    cat /opt/singularity_logo.txt

%environment
```

## Collection

 - Name: [ffineis/nurcs-singularity](https://github.com/ffineis/nurcs-singularity)
 - License: None

