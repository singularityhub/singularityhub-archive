---
id: 3369
name: "RedHenLab/singularity_containers"
branch: "master"
tag: "deepspeech2_ubuntu"
commit: "ccd7a0ce6698bb8ba9cd4b61a356bf66ad7d6bed"
version: "9bc4c0ce9f9260fff161da50a544c8ca"
build_date: "2021-03-18T07:13:52.642Z"
size_mb: 2508
size: 910721055
sif: "https://datasets.datalad.org/shub/RedHenLab/singularity_containers/deepspeech2_ubuntu/2021-03-18-ccd7a0ce-9bc4c0ce/9bc4c0ce9f9260fff161da50a544c8ca.simg"
url: https://datasets.datalad.org/shub/RedHenLab/singularity_containers/deepspeech2_ubuntu/2021-03-18-ccd7a0ce-9bc4c0ce/
recipe: https://datasets.datalad.org/shub/RedHenLab/singularity_containers/deepspeech2_ubuntu/2021-03-18-ccd7a0ce-9bc4c0ce/Singularity
collection: RedHenLab/singularity_containers
---

# RedHenLab/singularity_containers:deepspeech2_ubuntu

```bash
$ singularity pull shub://RedHenLab/singularity_containers:deepspeech2_ubuntu
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:latest

%labels
        MAINTAINER liontooth

%environment
        export LANGUAGE=en_US.UTF-8
        export LANG=en_US.UTF-8
        export LC_ALL=en_US.UTF-8

%post
        apt-get update
        apt-get install -y cmake \
                           locales \
                           language-pack-en \
                           git \
                           python2.7 \
                           python-pip \
                           gcc \
                           pkg-config \
                           libogg-dev  \
                           libvorbis-dev \
                           libboost-dev \
                           swig \
			   wget \
		           doxygen
			   
# Manually compile flac-1.3.2  
        wget http://downloads.xiph.org/releases/flac/flac-1.3.2.tar.xz   
        tar -xvf flac-1.3.2.tar.xz
	cd flac-1.3.2
	./configure --prefix=$HOME/usr --disable-ogg
	make
	make install    
	cd
        
# Manually compile libmkldnn.so
        git clone https://github.com/01org/mkl-dnn.git
	cd mkl-dnn
	cd scripts && ./prepare_mkl.sh && cd ..
	mkdir -p build && cd build && cmake .. && make && make install
	cd src
	cp libmkldnn.so.0.14.0 /usr/lib/libmkldnn.so.0.14.0
	cd /usr/lib
	ln -s libmkldnn.so.0.14.0 libmkldnn.so.0
	ln -s libmkldnn.so.0 libmkldnn.so
	ldconfig
	cd 
  
        locale-gen en_US.UTF-8 && dpkg-reconfigure locales
        pip install paddlepaddle-gpu

# Get DeepSpeech2 via PaddlePaddle
        git clone https://github.com/PaddlePaddle/DeepSpeech.git
        cd DeepSpeech
        sh setup.sh 

# Notes

# There may be an issue if you want to run Jupyter Notebook from the Singularity image -- here's a hint for a workaround:
# Solve Jupyter permission issue
#    CMD unset XDG_RUNTIME_DIR && \ 
#    jupyter notebook --port=12220 --no-browser
```

## Collection

 - Name: [RedHenLab/singularity_containers](https://github.com/RedHenLab/singularity_containers)
 - License: None

