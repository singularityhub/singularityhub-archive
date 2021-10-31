---
id: 7866
name: "staeglis/HPOlib2"
branch: "container"
tag: "cartpolebasegpu"
commit: "31833c0d0e1f4bcfc9abee213ed39f27f4c956d1"
version: "aeac720c3c8f1792d7eed16213d4e043"
build_date: "2019-03-20T16:44:42.974Z"
size_mb: 4814
size: 2537947167
sif: "https://datasets.datalad.org/shub/staeglis/HPOlib2/cartpolebasegpu/2019-03-20-31833c0d-aeac720c/aeac720c3c8f1792d7eed16213d4e043.simg"
url: https://datasets.datalad.org/shub/staeglis/HPOlib2/cartpolebasegpu/2019-03-20-31833c0d-aeac720c/
recipe: https://datasets.datalad.org/shub/staeglis/HPOlib2/cartpolebasegpu/2019-03-20-31833c0d-aeac720c/Singularity
collection: staeglis/HPOlib2
---

# staeglis/HPOlib2:cartpolebasegpu

```bash
$ singularity pull shub://staeglis/HPOlib2:cartpolebasegpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

%labels
MAINTAINER Stefan Staeglich

%post
    apt update -y
    apt install git -y
    apt install python3-pip python3-numpy python-configparser cython3 -y
    pip3 install git+https://github.com/automl/ConfigSpace.git@master
    apt install python3-sklearn -y
    pip3 install scikit-learn==0.19.1 scipy==0.19.1
    pip3 install git+https://github.com/staeglis/HPOlib2@container
    pip3 install pyro4
    pip3 install recommonmark
    pip3 install tensorflow-gpu==1.12.0 gym==0.10.9 tensorforce==0.4.3

%runscript
    python3 -s /usr/local/lib/python3.5/dist-packages/hpolib/container/server/abstract_benchmark.py rl.cartpole $@
```

## Collection

 - Name: [staeglis/HPOlib2](https://github.com/staeglis/HPOlib2)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

