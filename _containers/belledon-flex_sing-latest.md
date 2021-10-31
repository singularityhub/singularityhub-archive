---
id: 1447
name: "belledon/flex_sing"
branch: "master"
tag: "latest"
commit: "f4d6b9653eb7e7af70e5636a90c0de81ed1cbe38"
version: "70249ecdb1c1ead20b8c9b10dadb221a"
build_date: "2018-01-24T08:43:02.474Z"
size_mb: 2999
size: 1558945823
sif: "https://datasets.datalad.org/shub/belledon/flex_sing/latest/2018-01-24-f4d6b965-70249ecd/70249ecdb1c1ead20b8c9b10dadb221a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/belledon/flex_sing/latest/2018-01-24-f4d6b965-70249ecd/
recipe: https://datasets.datalad.org/shub/belledon/flex_sing/latest/2018-01-24-f4d6b965-70249ecd/Singularity
collection: belledon/flex_sing
---

# belledon/flex_sing:latest

```bash
$ singularity pull shub://belledon/flex_sing:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04


%environment

  export PATH=$PATH:/usr/local/cuda/bin/
  export CUDA_PATH=/usr/local/cuda
  #export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64:$LD_LIBRARY_PATH
  #export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}

%post

    echo "sym link cuda"
    ln -s /usr/local/cuda/bin/nvcc /bin/nvcc

    echo "Apt-getting packages"
    apt-get update && apt-get -y install locales
    locale-gen en_US.UTF-8

    apt-get -y install  build-essential \
		    git \
        cmake \
        g++ \
        vim \
        wget \
        gdb \
        libpng-dev \
        freeglut3-dev

    apt-get clean

    echo "Manually installing glew packages"

    cd /

    wget http://mirrors.kernel.org/ubuntu/pool/main/g/glew/libglew1.10_1.10.0-3_amd64.deb
    dpkg -i libglew1.10_1.10.0-3_amd64.deb
    rm libglew1.10_1.10.0-3_amd64.deb

    wget http://mirrors.kernel.org/ubuntu/pool/main/g/glew/libglew-dev_1.10.0-3_amd64.deb
    dpkg -i libglew-dev_1.10.0-3_amd64.deb
    rm libglew-dev_1.10.0-3_amd64.deb


    apt-get clean



    if [ -d "/yaml-cpp"]; then

        echo "Found yaml-cpp"
    else

        echo "installing yaml-cpp"
        cd /
        git clone https://github.com/jbeder/yaml-cpp.git
        cd yaml-cpp && mkdir build && cd build
        cmake ..
        make
        make install
        make clean
    fi



%test
    echo "hello dad!"
```

## Collection

 - Name: [belledon/flex_sing](https://github.com/belledon/flex_sing)
 - License: None

