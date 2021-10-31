---
id: 2956
name: "RedHenLab/singularity_containers"
branch: "master"
tag: "deepspeech2-flac"
commit: "19881c4f5a6d75912e2112027e321eb37bfa6a02"
version: "7f4b956879e507d150df69149d2be190"
build_date: "2018-05-27T22:25:50.866Z"
size_mb: 1931
size: 713162783
sif: "https://datasets.datalad.org/shub/RedHenLab/singularity_containers/deepspeech2-flac/2018-05-27-19881c4f-7f4b9568/7f4b956879e507d150df69149d2be190.simg"
url: https://datasets.datalad.org/shub/RedHenLab/singularity_containers/deepspeech2-flac/2018-05-27-19881c4f-7f4b9568/
recipe: https://datasets.datalad.org/shub/RedHenLab/singularity_containers/deepspeech2-flac/2018-05-27-19881c4f-7f4b9568/Singularity
collection: RedHenLab/singularity_containers
---

# RedHenLab/singularity_containers:deepspeech2-flac

```bash
$ singularity pull shub://RedHenLab/singularity_containers:deepspeech2-flac
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:latest

%labels
        MAINTAINER xuzhaoqing

%environment
        export LANGUAGE=en_US.UTF-8
        export LANG=en_US.UTF-8
        export LC_ALL=en_US.UTF-8

%post
        apt-get update
        apt-get install -y apt-utils \
                           cmake \
                           locales \
                           language-pack-en \
                           git \
                           python2.7 \
                           python-pip \
                           gcc \
                           pkg-config \
                           libflac-dev \
                           libogg-dev  \
                           libvorbis-dev \
                           libboost-dev \
                           swig \
                           tar \
                           wget
                           
        locale-gen en_US.UTF-8 && dpkg-reconfigure locales
        pip install paddlepaddle-gpu

# It's not clear we need this manual install
        wget http://downloads.xiph.org/releases/flac/flac-1.3.2.tar.xz   
        tar -xvf flac-1.3.2.tar.xz
        cd flac-1.3.2
        ./configure --prefix=$HOME/usr --disable-ogg
        make
        make install
        cd          

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

