---
id: 7873
name: "vmichals/singularity"
branch: "master"
tag: "cunet"
commit: "df5009aa4533a2abac2c122e1320999d2a2990e8"
version: "5ba6cdab0cfc30fa4bfbd6a076a546e4"
build_date: "2019-03-20T20:52:06.723Z"
size_mb: 2577
size: 1074929695
sif: "https://datasets.datalad.org/shub/vmichals/singularity/cunet/2019-03-20-df5009aa-5ba6cdab/5ba6cdab0cfc30fa4bfbd6a076a546e4.simg"
url: https://datasets.datalad.org/shub/vmichals/singularity/cunet/2019-03-20-df5009aa-5ba6cdab/
recipe: https://datasets.datalad.org/shub/vmichals/singularity/cunet/2019-03-20-df5009aa-5ba6cdab/Singularity
collection: vmichals/singularity
---

# vmichals/singularity:cunet

```bash
$ singularity pull shub://vmichals/singularity:cunet
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

# To run in this shell pointing to the data in deepglobe, you can execute
# singularity shell -B /network/tmp1/sankarak/deepglobe/:data superresolution.sif
# from inside the Mila cluster
#
# Note that this recipe can only be built on a machine where you are root, the
# build command is
# shell -B $HOME/conditional_unet:/home $SCRATCH/images/conditional_unet.sif

%post
    apt -y update
    apt -y upgrade
    apt -y install software-properties-common
    apt -y install vim unzip wget sudo
    add-apt-repository ppa:ubuntugis/ubuntugis-unstable
    apt -y update
    apt -y install build-essential libssl-dev libffi-dev python3-dev
    apt -y install libsm6
    apt -y install python3-pip python3-tk
    pip3 install --no-cache-dir numpy opencv-python Pillow
    apt -y install gdal-bin libgdal-dev
    pip3 install --no-cache-dir torch torchvision matplotlib ipython ipdb
    pip3 install --no-cache-dir scikit-learn scikit-image # osgeo
    pip3 install --no-cache-dir tiffile sklearn imutils gpustat pandas pyarrow
    pip3 install --no-cache-dir --global-option=build_ext --global-option="-I/usr/include/gdal" GDAL==`gdal-config --version`


%environment

%runscript
```

## Collection

 - Name: [vmichals/singularity](https://github.com/vmichals/singularity)
 - License: None

