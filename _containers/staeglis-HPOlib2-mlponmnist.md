---
id: 6406
name: "staeglis/HPOlib2"
branch: "container"
tag: "mlponmnist"
commit: "7c53ecb03822e8f2bbfae3d4c78af985b3e03474"
version: "2f720c0f92997b948b7e7d79a9052c98"
build_date: "2019-03-07T14:19:11.465Z"
size_mb: 946
size: 375779359
sif: "https://datasets.datalad.org/shub/staeglis/HPOlib2/mlponmnist/2019-03-07-7c53ecb0-2f720c0f/2f720c0f92997b948b7e7d79a9052c98.simg"
url: https://datasets.datalad.org/shub/staeglis/HPOlib2/mlponmnist/2019-03-07-7c53ecb0-2f720c0f/
recipe: https://datasets.datalad.org/shub/staeglis/HPOlib2/mlponmnist/2019-03-07-7c53ecb0-2f720c0f/Singularity
collection: staeglis/HPOlib2
---

# staeglis/HPOlib2:mlponmnist

```bash
$ singularity pull shub://staeglis/HPOlib2:mlponmnist
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
MAINTAINER Stefan Staeglich

%post
    apt update -y
    apt install git -y
    apt install python3-pip python-configparser cython3 -y
    pip3 install numpy
    pip3 install git+https://github.com/automl/ConfigSpace.git@master
    apt install python3-scipy python3-sklearn -y
    pip3 install git+https://github.com/staeglis/HPOlib2@container
    apt install pyro4 python3-pyro4 -y
    pip3 install openml

    mkdir /var/lib/hpolib/
    python3 /usr/local/lib/python3.6/dist-packages/hpolib/container/util/download_data.py ml.sklearn_mlp_benchmark MLPOnMnist
    chmod -R 777 /var/lib/hpolib/

%runscript
    python3 -s /usr/local/lib/python3.6/dist-packages/hpolib/container/server/abstract_benchmark.py ml.sklearn_mlp_benchmark $@
```

## Collection

 - Name: [staeglis/HPOlib2](https://github.com/staeglis/HPOlib2)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

