---
id: 2957
name: "RedHenLab/singularity_containers"
branch: "master"
tag: "deepspeech2-simplified"
commit: "aa34e3435b118c4bc016e6829129a1ce9d0aa22a"
version: "b7e96210367538076d5aa4e2fd32baf5"
build_date: "2018-05-27T22:25:50.846Z"
size_mb: 2456
size: 937078815
sif: "https://datasets.datalad.org/shub/RedHenLab/singularity_containers/deepspeech2-simplified/2018-05-27-aa34e343-b7e96210/b7e96210367538076d5aa4e2fd32baf5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/RedHenLab/singularity_containers/deepspeech2-simplified/2018-05-27-aa34e343-b7e96210/
recipe: https://datasets.datalad.org/shub/RedHenLab/singularity_containers/deepspeech2-simplified/2018-05-27-aa34e343-b7e96210/Singularity
collection: RedHenLab/singularity_containers
---

# RedHenLab/singularity_containers:deepspeech2-simplified

```bash
$ singularity pull shub://RedHenLab/singularity_containers:deepspeech2-simplified
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
                           flac \
                           libflac-dev \
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
#        wget http://downloads.xiph.org/releases/flac/flac-1.3.2.tar.xz   
#        tar -xvf flac-1.3.2.tar.xz
#	cd flac-1.3.2
#	./configure --prefix=$HOME/usr --disable-ogg
#	make
#	make install    
#	cd
        
# Manually compile libmkldnn.so (cf. https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=895729)
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

