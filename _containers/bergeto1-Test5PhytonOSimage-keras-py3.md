---
id: 4935
name: "bergeto1/Test5PhytonOSimage"
branch: "master"
tag: "keras-py3"
commit: "6896772c1fe9f708f1de0ef855aaa8e8114afd62"
version: "0eeb5c829d6f742ef3bfdd586f7e87e1"
build_date: "2018-09-21T13:10:13.153Z"
size_mb: 3260
size: 1599639583
sif: "https://datasets.datalad.org/shub/bergeto1/Test5PhytonOSimage/keras-py3/2018-09-21-6896772c-0eeb5c82/0eeb5c829d6f742ef3bfdd586f7e87e1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bergeto1/Test5PhytonOSimage/keras-py3/2018-09-21-6896772c-0eeb5c82/
recipe: https://datasets.datalad.org/shub/bergeto1/Test5PhytonOSimage/keras-py3/2018-09-21-6896772c-0eeb5c82/Singularity
collection: bergeto1/Test5PhytonOSimage
---

# bergeto1/Test5PhytonOSimage:keras-py3

```bash
$ singularity pull shub://bergeto1/Test5PhytonOSimage:keras-py3
```

## Singularity Recipe

```singularity
bootstrap:docker  
From:tensorflow/tensorflow:nightly-gpu-py3


#---------------------------------------------------------------------
%environment
#---------------------------------------------------------------------
export PATH=/bin:/usr/bin:/usr/local/bin:/usr/local/cuda/bin:
export LC_ALL=C

#---------------------------------------------------------------------
%post
#---------------------------------------------------------------------

apt-get update && apt-get -y install \
			python3-tk \

	
pip3 install --upgrade -I setuptools
pip3 install --upgrade keras 

	
pip3 install \
     jupyter \
     matplotlib \
     seaborn	\
     Image \
     scikit-learn
```

## Collection

 - Name: [bergeto1/Test5PhytonOSimage](https://github.com/bergeto1/Test5PhytonOSimage)
 - License: None

