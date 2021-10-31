---
id: 7283
name: "willgpaik/deformetrica_aci"
branch: "master"
tag: "latest"
commit: "7c307e23d3103a8612c8236167fde83b7e8e8972"
version: "4b4959255138893375b046fc2f301bad"
build_date: "2020-10-13T20:13:07.465Z"
size_mb: 12158.0
size: 5500391455
sif: "https://datasets.datalad.org/shub/willgpaik/deformetrica_aci/latest/2020-10-13-7c307e23-4b495925/4b4959255138893375b046fc2f301bad.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/deformetrica_aci/latest/2020-10-13-7c307e23-4b495925/
recipe: https://datasets.datalad.org/shub/willgpaik/deformetrica_aci/latest/2020-10-13-7c307e23-4b495925/Singularity
collection: willgpaik/deformetrica_aci
---

# willgpaik/deformetrica_aci:latest

```bash
$ singularity pull shub://willgpaik/deformetrica_aci:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: willgpaik/centos7_aci:gpu

%setup
  
%files

%environment
    source /opt/rh/devtoolset-8/enable
    PATH="$PATH:/opt/sw/anaconda3/bin/"
    export PATH
    PATH="/usr/local/bin/:$PATH:/usr/lib64/openmpi/bin/:/usr/local/cuda/bin"
    LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib64/openmpi/lib/:/usr/local/cuda/lib64"
    MPI_ROOT=/usr/lib64/openmpi/
    export PATH
    export LD_LIBRARY_PATH
    export MPI_ROOT
    export BOOST_ROOT=/usr/local/

%runscript
    source /opt/rh/devtoolset-8/enable
    source /opt/sw/anaconda3/etc/profile.d/conda.sh
    source activate deformetrica
    exec "$@"

%post
    PATH="/usr/local/bin/:$PATH:/usr/lib64/openmpi/bin/:/usr/local/cuda/bin"
    LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib64/openmpi/lib/:/usr/local/cuda/lib64"
    MPI_ROOT=/usr/lib64/openmpi/
    export PATH
    export LD_LIBRARY_PATH
    export MPI_ROOT
    export BOOST_ROOT=/usr/local/
    source /opt/rh/devtoolset-8/enable

    # Install Anaconda
    mkdir -p /opt/sw/
    cd /opt/sw/
    wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
    bash Anaconda3-2020.07-Linux-x86_64.sh -b -p /opt/sw/anaconda3
    source /opt/sw/anaconda3/etc/profile.d/conda.sh
    export PATH=$PATH:/opt/sw/anaconda3/bin/
    
    # Update conda
    conda update -y conda
    conda update -y anaconda

    conda create -y -n deformetrica python=3.8 numpy && source activate deformetrica
    conda install -y pytorch torchvision cudatoolkit=10.2 -c pytorch
    pip install pykeops
    pip install deformetrica
    
    cd /opt/sw/
    rm Anaconda3-2020.07-Linux-x86_64.sh
    rm -rf /opt/sw/anaconda3/pkgs/*
```

## Collection

 - Name: [willgpaik/deformetrica_aci](https://github.com/willgpaik/deformetrica_aci)
 - License: None

