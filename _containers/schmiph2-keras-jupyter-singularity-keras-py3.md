---
id: 4803
name: "schmiph2/keras-jupyter-singularity"
branch: "master"
tag: "keras-py3"
commit: "6172b442bdb2616395ff63d56814c06783e10966"
version: "22c9c9f0eeacbcfaa86f6a9dcc42f620"
build_date: "2021-04-13T14:00:46.645Z"
size_mb: 3260
size: 1599991839
sif: "https://datasets.datalad.org/shub/schmiph2/keras-jupyter-singularity/keras-py3/2021-04-13-6172b442-22c9c9f0/22c9c9f0eeacbcfaa86f6a9dcc42f620.simg"
url: https://datasets.datalad.org/shub/schmiph2/keras-jupyter-singularity/keras-py3/2021-04-13-6172b442-22c9c9f0/
recipe: https://datasets.datalad.org/shub/schmiph2/keras-jupyter-singularity/keras-py3/2021-04-13-6172b442-22c9c9f0/Singularity
collection: schmiph2/keras-jupyter-singularity
---

# schmiph2/keras-jupyter-singularity:keras-py3

```bash
$ singularity pull shub://schmiph2/keras-jupyter-singularity:keras-py3
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

 - Name: [schmiph2/keras-jupyter-singularity](https://github.com/schmiph2/keras-jupyter-singularity)
 - License: None

