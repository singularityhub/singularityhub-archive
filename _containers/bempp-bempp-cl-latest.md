---
id: 11432
name: "bempp/bempp-cl"
branch: "master"
tag: "latest"
commit: "96701617b5433faa85235aebc1776194eb1b0018"
version: "168c8a264c21c26ad9b630e6cd5f00d3"
build_date: "2020-08-05T17:20:46.919Z"
size_mb: 5706.0
size: 2421104671
sif: "https://datasets.datalad.org/shub/bempp/bempp-cl/latest/2020-08-05-96701617-168c8a26/168c8a264c21c26ad9b630e6cd5f00d3.sif"
url: https://datasets.datalad.org/shub/bempp/bempp-cl/latest/2020-08-05-96701617-168c8a26/
recipe: https://datasets.datalad.org/shub/bempp/bempp-cl/latest/2020-08-05-96701617-168c8a26/Singularity
collection: bempp/bempp-cl
---

# bempp/bempp-cl:latest

```bash
$ singularity pull shub://bempp/bempp-cl:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic


%help
    A Singularity image for bempp-cl

%setup 
    echo "SETUP"

%environment
    PATH=/usr/local/bin:/opt/miniconda/envs/bempp/bin:/usr/bin:/usr/sbin:/sbin:/bin

%post

    apt-get update
    apt-get -y install software-properties-common wget gmsh git binutils build-essential

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ./miniconda.sh
    bash ./miniconda.sh -b -p /opt/miniconda
    export PATH=/opt/miniconda/bin:$PATH
    conda create --yes -n bempp python=3.7
    conda install -n bempp --yes numpy scipy matplotlib numba pytest jupyter plotly git pip
    conda install -n bempp --yes -c conda-forge pocl pyopencl fenics
    conda install -n bempp --yes "libblas=*=*mkl"
    /opt/miniconda/envs/bempp/bin/pip install meshio
    /opt/miniconda/envs/bempp/bin/pip install git+git://github.com/bempp/bempp-cl@master

    ln -s /opt/miniconda/envs/bempp/bin/python /usr/local/bin/python
    ln -s /opt/miniconda/envs/bempp/bin/ipython /usr/local/bin/ipython
    ln -s /opt/miniconda/envs/bempp/bin/jupyter /usr/local/bin/jupyter


%runscript
    exec "$@"
```

## Collection

 - Name: [bempp/bempp-cl](https://github.com/bempp/bempp-cl)
 - License: [MIT License](https://api.github.com/licenses/mit)

