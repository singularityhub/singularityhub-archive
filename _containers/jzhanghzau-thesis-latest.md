---
id: 12341
name: "jzhanghzau/thesis"
branch: "master"
tag: "latest"
commit: "1e0613fca16f6d6b7c90766e06454a19d5ae2211"
version: "eb74668a3c6662f50c321d0134a0f40e555eee50ff6ede4578848536c61eebba"
build_date: "2020-02-24T13:46:30.660Z"
size_mb: 3953.11328125
size: 4145139712
sif: "https://datasets.datalad.org/shub/jzhanghzau/thesis/latest/2020-02-24-1e0613fc-eb74668a/eb74668a3c6662f50c321d0134a0f40e555eee50ff6ede4578848536c61eebba.sif"
url: https://datasets.datalad.org/shub/jzhanghzau/thesis/latest/2020-02-24-1e0613fc-eb74668a/
recipe: https://datasets.datalad.org/shub/jzhanghzau/thesis/latest/2020-02-24-1e0613fc-eb74668a/Singularity
collection: jzhanghzau/thesis
---

# jzhanghzau/thesis:latest

```bash
$ singularity pull shub://jzhanghzau/thesis:latest
```

## Singularity Recipe

```singularity
bootstrap:docker 
From:continuumio/miniconda3

%runscript
    exec echo "haha!"
%post
    apt-get update && apt-get install -y git wget python3-dev python3-pip
    /opt/conda/bin/conda install -c ankurankan pgmpy
    /opt/conda/bin/conda install pip
    /opt/conda/bin/pip install bnlearn
    /opt/conda/bin/conda install -c conda-forge networkx
    /opt/conda/bin/conda install numpy matplotlib scikit-learn 
    /opt/conda/bin/conda install -c conda-forge tensorflow
    /opt/conda/bin/conda install -c anaconda pandas
    /opt/conda/bin/conda install -c conda-forge keras
    /opt/conda/bin/conda install -c anaconda psutil
    /opt/conda/bin/conda install -c conda-forge xgboost
    /opt/conda/bin/conda install -c anaconda simplejson
    /opt/conda/bin/conda install -c conda-forge librosa
```

## Collection

 - Name: [jzhanghzau/thesis](https://github.com/jzhanghzau/thesis)
 - License: None

