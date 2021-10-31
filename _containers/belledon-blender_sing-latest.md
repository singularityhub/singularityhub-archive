---
id: 2390
name: "belledon/blender_sing"
branch: "master"
tag: "latest"
commit: "7ae0293a173e1878c26f747129adccaad3ca82f4"
version: "49308066d130ab6f8e6ddd67531ea9e0"
build_date: "2018-04-03T22:05:09.825Z"
size_mb: 2717
size: 899895327
sif: "https://datasets.datalad.org/shub/belledon/blender_sing/latest/2018-04-03-7ae0293a-49308066/49308066d130ab6f8e6ddd67531ea9e0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/belledon/blender_sing/latest/2018-04-03-7ae0293a-49308066/
recipe: https://datasets.datalad.org/shub/belledon/blender_sing/latest/2018-04-03-7ae0293a-49308066/Singularity
collection: belledon/blender_sing
---

# belledon/blender_sing:latest

```bash
$ singularity pull shub://belledon/blender_sing:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
from: ubuntu:16.04


%runscript
    echo "SINGULARITY RUNSCRIPT"
    echo "Arguments received: $*"
    exec /usr/bin/python3 "$@"


%post
    apt-get update && apt-get -y install locales
    locale-gen en_US.UTF-8
    apt-get install -y  vim \
                        wget \
                        bzip2 \
                        ca-certificates \
                        libglib2.0-0 \
                        libxext6 \
                        libsm6 \
                        libxrender1 \
                        git \
                        cmake \
                        g++ \
                        xvfb \
                        libyaml-cpp-dev \
                        python3-dev \
                        python3-pip \
                        software-properties-common

    apt-get clean

    cd /
    git clone -b 2.79 https://github.com/belledon/blender_fix.git
    cd blender_fix
    chmod +x install.sh
    ./install.sh
```

## Collection

 - Name: [belledon/blender_sing](https://github.com/belledon/blender_sing)
 - License: None

