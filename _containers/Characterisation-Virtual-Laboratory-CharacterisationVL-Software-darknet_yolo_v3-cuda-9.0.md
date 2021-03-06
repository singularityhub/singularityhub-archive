---
id: 8734
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "darknet_yolo_v3-cuda-9.0"
commit: "a4a84554049a0f8f6b26b896c36795895eafa287"
version: "b5525a96bd255566bbd3e9fb1dd8d135"
build_date: "2019-05-01T22:22:24.859Z"
size_mb: 6935
size: 3381477407
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/darknet_yolo_v3-cuda-9.0/2019-05-01-a4a84554-b5525a96/b5525a96bd255566bbd3e9fb1dd8d135.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/darknet_yolo_v3-cuda-9.0/2019-05-01-a4a84554-b5525a96/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/darknet_yolo_v3-cuda-9.0/2019-05-01-a4a84554-b5525a96/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:darknet_yolo_v3-cuda-9.0

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:darknet_yolo_v3-cuda-9.0
```

## Singularity Recipe

```singularity
Bootstrap: shub
From:      Characterisation-Virtual-Laboratory/CharacterisationVL-Software:1804-cuda9

%labels
    MAINTAINER_NAME  Jay van Schyndel
    MAINTAINER_EMAIL jay.vanschyndel@monash.edu

    APPLICATION_NAME ubuntu
    APPLICATION_VERSION 18.04

    HARDWARE GPU

    LAST_UPDATED 26-APR-2019

%environment
    export PKG_CONFIG_PATH="/opt/opencv/lib/pkgconfig:$PKG_CONFIG_PATH"
    CUDA="/usr/local/cuda/bin"
    OPENCV="/opt/opencv/bin/"
    DARKNET="/opt/darknet"
    DARKNET_CFG="/opt/darknet/cfg"
    DARKNET_DATA="/opt/darknet/data"
    export PATH="$CUDA:$OPENCV:$DARKNET:$DARKNET_CFG:$DARKNET_DATA:$PATH"
    export LD_LIBRARY_PATH="/usr/local/cuda/lib64/:/opt/opencv/lib:$LD_LIBRARY_PATH"

%post -c /bin/bash
    echo "*********************************************************"
    echo "Setup and display environment"
    echo "*********************************************************"
    export LC_ALL=en_AU.UTF-8
    export LANGUAGE=en_AU.UTF-8
    export DEBIAN_FRONTEND=noninteractive
    echo $LC_ALL
    echo $LANGUAGE
    echo $DEBIAN_FRONTEND
    echo "*********************************************************"
    echo "Install repositories"
    echo "*********************************************************"
    apt-get install -y software-properties-common
    apt-add-repository -y 'deb http://us.archive.ubuntu.com/ubuntu/ bionic main restricted'
    apt-add-repository -y 'deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates main restricted'
    apt-add-repository -y 'deb http://us.archive.ubuntu.com/ubuntu/ bionic universe'
    apt-add-repository -y 'deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates universe'
    echo "*********************************************************"
    echo "Update repositories and install desktop"
    echo "*********************************************************"
    apt update
    apt upgrade -y
    apt install -y locales
    locale-gen en_AU.UTF-8

    echo "===================================="
    echo "Setting up env variables"
    echo "===================================="
    export PKG_CONFIG_PATH="/opt/opencv/lib/pkgconfig:$PKG_CONFIG_PATH"
    CUDA="/usr/local/cuda/bin"
    OPENCV="/opt/opencv/bin/"
    DARKNET="/opt/darknet"
    export PATH="$CUDA:$OPENCV:$PATH:$DARKNET"
    export LD_LIBRARY_PATH="/usr/local/cuda/lib64/:/opt/opencv/lib:$LD_LIBRARY_PATH"

    echo "===================================="
    echo "Installing dependencies             "
    echo "===================================="
    #OpenCV 2.x.x and OpenCV <= 3.4.0
    apt install -y libopencv-core-dev libopencv-core3.2 libopencv-highgui-dev libopencv-highgui3.2 
    apt install -y libopencv-calib3d-dev libopencv-calib3d3.2 libopencv-objdetect-dev libopencv-objdetect3.2 libopencv-photo-dev libopencv-photo3.2
    apt install -y libopencv-shape-dev libopencv-shape3.2 libopencv-stitching-dev libopencv-stitching3.2 libopencv-superres-dev libopencv-superres3.2
    apt install -y libopencv-videostab-dev libopencv-videostab3.2 libopencv-viz-dev libopencv-viz3.2 libopencv-dev libopencv-core-dev libopencv-core3.2

    echo "===================================="
    echo "Installing DarkNet 3.4.4"
    echo "===================================="
    cd /opt/
    git clone -b darknet_yolo_v3 https://github.com/AlexeyAB/darknet.git
    cd darknet
    sed -i -e 's/GPU=0/GPU=1/' Makefile
    #sed -i -e 's/CUDNN=0/CUDNN=1/' Makefile
    sed -i -e 's/OPENCV=0/OPENCV=1/' Makefile
    #Fix so that the cuda libraries are found during build
    sed -i -e 's/LDFLAGS+= -L\/usr\/local\/cuda\/lib64 -lcuda -lcudart -lcublas -lcurand/LDFLAGS+= -L\/usr\/local\/cuda\/lib64\/stubs -lcuda -L\/usr\/local\/cuda\/lib64\/ -lcudart -lcublas -lcurand/' Makefile
    make -j8    

    #For testing purposes
    wget https://pjreddie.com/media/files/yolov3.weights

%runscript
    $*
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

