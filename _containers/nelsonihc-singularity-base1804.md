---
id: 5480
name: "nelsonihc/singularity"
branch: "master"
tag: "base1804"
commit: "b85a128585e986a043e86eb3d5faea4f275e438d"
version: "30fd240c36f0dcb89b4cd793e56e01b2"
build_date: "2018-11-05T14:28:49.783Z"
size_mb: 5834
size: 2537971743
sif: "https://datasets.datalad.org/shub/nelsonihc/singularity/base1804/2018-11-05-b85a1285-30fd240c/30fd240c36f0dcb89b4cd793e56e01b2.simg"
url: https://datasets.datalad.org/shub/nelsonihc/singularity/base1804/2018-11-05-b85a1285-30fd240c/
recipe: https://datasets.datalad.org/shub/nelsonihc/singularity/base1804/2018-11-05-b85a1285-30fd240c/Singularity
collection: nelsonihc/singularity
---

# nelsonihc/singularity:base1804

```bash
$ singularity pull shub://nelsonihc/singularity:base1804
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:9.2-cudnn7-devel-ubuntu18.04

%environment
    export LANG=C.UTF-8
    export LC_ALL=C.UTF-8
    export PATH=/opt/conda/bin:$PATH

%post
    export DEBIAN_FRONTEND=noninteractive
    export LANG=C.UTF-8
    export LC_ALL=C.UTF-8
    export PATH=/opt/conda/bin:$PATH

    apt update && apt install -qy \
          build-essential \
          cmake \
          git mercurial subversion \
          curl \
          vim \
          ca-certificates \
          ibacm \
          ibsim-utils \
          ibutils \
          ibverbs-utils \
          infiniband-diags \
          libdapl2 \
          libfontconfig1 \
          libgl1-mesa-glx \
          libglib2.0-0 \
          ibverbs-providers \
          libibmad5 \
          libibumad3 \
          libibverbs-dev \
          libibverbs1 \
          libjpeg-dev \
          libopensm5a \
          libpng-dev \
          librdmacm1 \
          libsm6 \
          libx11-xcb1 \
          libxext6 \
          libxrender1 \
          mstflint \
          opensm \
          perftest \
          rdmacm-utils \
          srptools

    rm -rf /var/lib/apt/lists/*

    cd /tmp && \
        curl -o /tmp/openmpi.tar.gz -O \
        https://download.open-mpi.org/release/open-mpi/v3.1/openmpi-3.1.2.tar.gz && \
        tar xzpvf /tmp/openmpi.tar.gz && \
        cd /tmp/openmpi-3.1.2 && \
        ./configure --with-cuda=/usr/local/cuda --enable-contrib-no-build=vt && \
        make -j 4 && \
        make install && ldconfig && \
        cd /tmp && rm -rf /tmp/openmpi.tar.gz /tmp/openmpi-3.1.2

    export PYTHON_VERSION=3.6
    export CONDA_INSTALL_PATH="/opt/conda"

    curl -o /tmp/miniconda.sh -O \
       https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
       chmod +x /tmp/miniconda.sh && \
       /tmp/miniconda.sh -b -p $CONDA_INSTALL_PATH && \
       rm /tmp/miniconda.sh && \
       /opt/conda/bin/conda install -y python=$PYTHON_VERSION anaconda && \
       /opt/conda/bin/conda clean -tipsy && \
       ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh
    
    # hotfix: matplotlib error   
    /opt/conda/bin/conda uninstall -y libxcb matplotlib
    /opt/conda/bin/pip install matplotlib
```

## Collection

 - Name: [nelsonihc/singularity](https://github.com/nelsonihc/singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

