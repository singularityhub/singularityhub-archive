---
id: 2429
name: "ucr-singularity/ml-anaconda-3"
branch: "master"
tag: "latest"
commit: "4f9142d3defb77e1a02783bb9ba33110da28e3dc"
version: "ef37689b027341f2ef67174583f3e246"
build_date: "2019-11-06T19:43:52.894Z"
size_mb: 5670
size: 3085008927
sif: "https://datasets.datalad.org/shub/ucr-singularity/ml-anaconda-3/latest/2019-11-06-4f9142d3-ef37689b/ef37689b027341f2ef67174583f3e246.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ucr-singularity/ml-anaconda-3/latest/2019-11-06-4f9142d3-ef37689b/
recipe: https://datasets.datalad.org/shub/ucr-singularity/ml-anaconda-3/latest/2019-11-06-4f9142d3-ef37689b/Singularity
collection: ucr-singularity/ml-anaconda-3
---

# ucr-singularity/ml-anaconda-3:latest

```bash
$ singularity pull shub://ucr-singularity/ml-anaconda-3:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

%environment

  PATH=/opt/conda/bin:$PATH
  export PATH
  
%post
  
    # Update list of packages
    apt-get update
    # Install dependencies
    apt-get install -y --no-install-recommends build-essential cmake git curl vim ca-certificates libjpeg-dev libpng-dev
    # Clean up
    rm -rf /var/lib/apt/lists/*
    
    # Install miniconda
    cd /opt
    curl -o /opt/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    chmod +x /opt/miniconda.sh
    /opt/miniconda.sh -b -p /opt/conda 
    rm /opt/miniconda.sh
    /opt/conda/bin/conda install numpy pyyaml scipy ipython mkl mkl-include
    /opt/conda/bin/conda install -c soumith magma-cuda90
    /opt/conda/bin/conda clean -ya
    
    # Install the released version of Pytorch.
    /opt/conda/bin/conda install pytorch torchvision cuda90 -c pytorch

    echo 'export PATH=/opt/conda/bin:$PATH' >>$SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [ucr-singularity/ml-anaconda-3](https://github.com/ucr-singularity/ml-anaconda-3)
 - License: None

