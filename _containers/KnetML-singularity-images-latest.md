---
id: 1936
name: "KnetML/singularity-images"
branch: "master"
tag: "latest"
commit: "2d3c2b3648be93f2b087d57c2536a0f4296fcca4"
version: "e04a2d4f2773ee1e780a4a760c965eb0"
build_date: "2021-01-21T14:37:52.958Z"
size_mb: 1684
size: 562257951
sif: "https://datasets.datalad.org/shub/KnetML/singularity-images/latest/2021-01-21-2d3c2b36-e04a2d4f/e04a2d4f2773ee1e780a4a760c965eb0.simg"
url: https://datasets.datalad.org/shub/KnetML/singularity-images/latest/2021-01-21-2d3c2b36-e04a2d4f/
recipe: https://datasets.datalad.org/shub/KnetML/singularity-images/latest/2021-01-21-2d3c2b36-e04a2d4f/Singularity
collection: KnetML/singularity-images
---

# KnetML/singularity-images:latest

```bash
$ singularity pull shub://KnetML/singularity-images:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%environment
   
   LANG=C.UTF-8
   LC_ALL=C.UTF-8
   export LANG LC_ALL
   export LD_LIBRARY_PATH=/usr/lib:/usr/lib64:/usr/local/cuda/lib64:/usr/local/cuda/lib:/opt/cudnn/lib64:$LD_LIBRARY_PATH
   export PATH=/opt/julia-0.6/bin:/usr/local/cuda/bin:$PATH
   export JULIA_PKGDIR=/workdir/.julia
   export XDG_RUNTIME_DIR="/workdir/notebooks"
   export JUPYTER=/usr/local/bin/jupyter
   export JUPYTER_PATH=/workdir/.jupyter
   export JUPYTER_DATA_DIR=/workdir/.jupyter

%runscript
exec jupyter notebook --notebook-dir=/workdir/notebooks --ip='*' --port=8888 --no-browser

%post
 
   echo "Here we are installing software and other dependencies for the container!"
   apt-get update
   apt-get install -y \
    build-essential \
    libzmq3-dev \
    pkg-config \
    python \
    python-dev \
    python-pip \
    git \
    vim \
    emacs \
    libxml2 \
    wget \
    curl \
    unzip \
    cmake \
    hdf5-tools \

    pip install jupyter
    
    mkdir -p /opt/julia-0.6.2-dev && \
    curl -s -L https://julialang-s3.julialang.org/bin/linux/x64/0.6/julia-0.6.2-linux-x86_64.tar.gz | tar -C /opt/julia-0.6.2-dev -x -z --strip-components=1 -f -
    ln -fs /opt/julia-0.6.2-dev/bin/julia /usr/bin/julia
    
    export JULIA_PKGDIR=/workdir/.julia
    
    /opt/julia-0.6.2-dev/bin/julia -e 'Pkg.init()'
    /opt/julia-0.6.2-dev/bin/julia -e 'Pkg.add("CUDAapi")'
    /opt/julia-0.6.2-dev/bin/julia -e 'Pkg.add("Knet")'
    /opt/julia-0.6.2-dev/bin/julia -e 'Pkg.add("JLD")'
    /opt/julia-0.6.2-dev/bin/julia -e 'Pkg.add("ArgParse")'
    /opt/julia-0.6.2-dev/bin/julia -e 'Pkg.add("PyCall")'
    /opt/julia-0.6.2-dev/bin/julia -e 'Pkg.add("Images")'

    export JUPYTER=/usr/local/bin/jupyter
    export JUPYTER_PATH=/workdir/.jupyter
    export JUPYTER_DATA_DIR=/workdir/.jupyter
    
    /opt/julia-0.6.2-dev/bin/julia -e 'Pkg.add("IJulia")'
    /opt/julia-0.6.2-dev/bin/julia -e 'Pkg.build("IJulia")'

    rm -rf /workdir/.julia/.cache
    rm -rf /workdir/.julia/lib

    mkdir -p /workdir/notebooks

    chmod -R 777 /workdir

    mkdir -p /opt/cudnn
    mkdir -p /usr/local/cuda
```

## Collection

 - Name: [KnetML/singularity-images](https://github.com/KnetML/singularity-images)
 - License: None

