---
id: 2953
name: "RedHenLab/singularity_containers"
branch: "master"
tag: "deepspeech2-wget"
commit: "f4a657757a70ca1ed6f2cbcabc46991d54a9cb97"
version: "8836e3eb1717b32b840e18445b7bd0fa"
build_date: "2018-05-27T16:15:48.559Z"
size_mb: 1893
size: 704602143
sif: "https://datasets.datalad.org/shub/RedHenLab/singularity_containers/deepspeech2-wget/2018-05-27-f4a65775-8836e3eb/8836e3eb1717b32b840e18445b7bd0fa.simg"
url: https://datasets.datalad.org/shub/RedHenLab/singularity_containers/deepspeech2-wget/2018-05-27-f4a65775-8836e3eb/
recipe: https://datasets.datalad.org/shub/RedHenLab/singularity_containers/deepspeech2-wget/2018-05-27-f4a65775-8836e3eb/Singularity
collection: RedHenLab/singularity_containers
---

# RedHenLab/singularity_containers:deepspeech2-wget

```bash
$ singularity pull shub://RedHenLab/singularity_containers:deepspeech2-wget
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
#        wget http://downloads.xiph.org/releases/flac/flac-1.3.2.tar.xz   
#        tar -xvf flac-1.3.2.tar.xz
#        cd flac-1.3.2
#        ./configure --prefix=$HOME/usr --disable-ogg
#        make
#        make install
#        cd          

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

