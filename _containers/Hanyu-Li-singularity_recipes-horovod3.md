---
id: 9002
name: "Hanyu-Li/singularity_recipes"
branch: "master"
tag: "horovod3"
commit: "88d48e6ae5f807ed9c93c6ccb70d510224eb18af"
version: "520ebb944357cdb28bee77cb14b4e92f"
build_date: "2019-05-10T20:18:29.510Z"
size_mb: 6128
size: 3529158687
sif: "https://datasets.datalad.org/shub/Hanyu-Li/singularity_recipes/horovod3/2019-05-10-88d48e6a-520ebb94/520ebb944357cdb28bee77cb14b4e92f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Hanyu-Li/singularity_recipes/horovod3/2019-05-10-88d48e6a-520ebb94/
recipe: https://datasets.datalad.org/shub/Hanyu-Li/singularity_recipes/horovod3/2019-05-10-88d48e6a-520ebb94/Singularity
collection: Hanyu-Li/singularity_recipes
---

# Hanyu-Li/singularity_recipes:horovod3

```bash
$ singularity pull shub://Hanyu-Li/singularity_recipes:horovod3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: uber/horovod:0.15.2-tf1.12.0-torch1.0.0-py3.5 

%help

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

%labels
Maintainer keceli
See https://github.com/uber/horovod/blob/master/Dockerfile

#------------
# Global installation
#------------
%environment
    
%post
    
 

    # pip basics
    pip --no-cache-dir --disable-pip-version-check install --upgrade setuptools 
    pip --no-cache-dir --disable-pip-version-check install numpy wheel zmq six pygments pyyaml cython gputil psutil humanize h5py tqdm scipy seaborn tables
    pip --no-cache-dir --disable-pip-version-check install  pandas scikit-image scikit-learn Pillow opencv-python
    pip --no-cache-dir --disable-pip-version-check install git+https://github.com/dask/dask.git
    
  
   # ffn
    git clone https://github.com/hanyu-li/ffn.git
```

## Collection

 - Name: [Hanyu-Li/singularity_recipes](https://github.com/Hanyu-Li/singularity_recipes)
 - License: None

