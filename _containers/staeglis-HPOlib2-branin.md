---
id: 3698
name: "staeglis/HPOlib2"
branch: "container"
tag: "branin"
commit: "683f5b497a796b74bc6862c80a526091e4266894"
version: "01934c957c1a1f8099b98fdcc31089e6"
build_date: "2018-10-16T10:25:41.317Z"
size_mb: 816
size: 318853151
sif: "https://datasets.datalad.org/shub/staeglis/HPOlib2/branin/2018-10-16-683f5b49-01934c95/01934c957c1a1f8099b98fdcc31089e6.simg"
url: https://datasets.datalad.org/shub/staeglis/HPOlib2/branin/2018-10-16-683f5b49-01934c95/
recipe: https://datasets.datalad.org/shub/staeglis/HPOlib2/branin/2018-10-16-683f5b49-01934c95/Singularity
collection: staeglis/HPOlib2
---

# staeglis/HPOlib2:branin

```bash
$ singularity pull shub://staeglis/HPOlib2:branin
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
    apt install python3-scipy python3-sklearn -y
    pip3 install git+https://github.com/staeglis/HPOlib2@container
    apt install pyro4 python3-pyro4 -y

%startscript
    echo "Test"

%runscript
    python3 -s /usr/local/lib/python3.6/dist-packages/hpolib/container/server/abstract_benchmark.py synthetic_functions.branin $@
```

## Collection

 - Name: [staeglis/HPOlib2](https://github.com/staeglis/HPOlib2)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

