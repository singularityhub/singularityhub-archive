---
id: 5178
name: "staeglis/HPOlib2"
branch: "container"
tag: "cartpolebase"
commit: "7e50130e13842be1c1575ad3f829408d452791b7"
version: "0c3cc5905a791632f5d9e96061f9ccff"
build_date: "2019-02-05T11:03:50.420Z"
size_mb: 1366
size: 527597599
sif: "https://datasets.datalad.org/shub/staeglis/HPOlib2/cartpolebase/2019-02-05-7e50130e-0c3cc590/0c3cc5905a791632f5d9e96061f9ccff.simg"
url: https://datasets.datalad.org/shub/staeglis/HPOlib2/cartpolebase/2019-02-05-7e50130e-0c3cc590/
recipe: https://datasets.datalad.org/shub/staeglis/HPOlib2/cartpolebase/2019-02-05-7e50130e-0c3cc590/Singularity
collection: staeglis/HPOlib2
---

# staeglis/HPOlib2:cartpolebase

```bash
$ singularity pull shub://staeglis/HPOlib2:cartpolebase
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
    apt install python3-pip python3-numpy python-configparser cython3 -y
    pip3 install git+https://github.com/automl/ConfigSpace.git@master
    apt install python3-sklearn -y
    pip3 install scikit-learn==0.19.1 scipy==0.19.1
    pip3 install git+https://github.com/staeglis/HPOlib2@container
    pip3 install pyro4
    pip3 install recommonmark
    pip3 install tensorflow==1.12.0 gym==0.10.9 tensorforce==0.4.3

%runscript
    python3 -s /usr/local/lib/python3.6/dist-packages/hpolib/container/server/abstract_benchmark.py rl.cartpole $@
```

## Collection

 - Name: [staeglis/HPOlib2](https://github.com/staeglis/HPOlib2)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

