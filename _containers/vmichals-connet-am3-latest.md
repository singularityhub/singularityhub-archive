---
id: 10495
name: "vmichals/connet-am3"
branch: "master"
tag: "latest"
commit: "ac46e457dbc6402bb88b39024e5671f9e659e041"
version: "91ba5ad2e971c6e6ef87be2c462e94ce"
build_date: "2019-08-31T19:40:14.885Z"
size_mb: 3659.0
size: 1795518495
sif: "https://datasets.datalad.org/shub/vmichals/connet-am3/latest/2019-08-31-ac46e457-91ba5ad2/91ba5ad2e971c6e6ef87be2c462e94ce.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/vmichals/connet-am3/latest/2019-08-31-ac46e457-91ba5ad2/
recipe: https://datasets.datalad.org/shub/vmichals/connet-am3/latest/2019-08-31-ac46e457-91ba5ad2/Singularity
collection: vmichals/connet-am3
---

# vmichals/connet-am3:latest

```bash
$ singularity pull shub://vmichals/connet-am3:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: tensorflow/tensorflow:1.13.2-gpu-py3

%post
    #apt -y update
    #apt -y upgrade
    #apt -y install vim unzip wget sudo
    #apt -y install build-essential libssl-dev libffi-dev 
    #apt -y install libsm6
    #apt -y install python3-pip python3-tk
    apt-get -y install git

    pip install --no-cache-dir opencv-python 
    pip install --no-cache-dir matplotlib ipython ipdb
    pip install --no-cache-dir scikit-learn scikit-image
    pip install --no-cache-dir tqdm pandas imageio
    pip install --no-cache-dir tables h5py
    pip install --no-cache-dir gitpython 
    pip install --no-cache-dir git+https://github.com/epistimio/orion.git@develop


%environment

%runscript
```

## Collection

 - Name: [vmichals/connet-am3](https://github.com/vmichals/connet-am3)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

