---
id: 5177
name: "staeglis/HPOlib2"
branch: "container"
tag: "forrester"
commit: "0c04586a3575800d104a56ee3de570fa05c07536"
version: "6ede0acacb9b053192abcc4c231e37d1"
build_date: "2018-10-11T09:24:01.566Z"
size_mb: 816
size: 318816287
sif: "https://datasets.datalad.org/shub/staeglis/HPOlib2/forrester/2018-10-11-0c04586a-6ede0aca/6ede0acacb9b053192abcc4c231e37d1.simg"
url: https://datasets.datalad.org/shub/staeglis/HPOlib2/forrester/2018-10-11-0c04586a-6ede0aca/
recipe: https://datasets.datalad.org/shub/staeglis/HPOlib2/forrester/2018-10-11-0c04586a-6ede0aca/Singularity
collection: staeglis/HPOlib2
---

# staeglis/HPOlib2:forrester

```bash
$ singularity pull shub://staeglis/HPOlib2:forrester
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
    pip3 install openml
    pip3 install git+https://github.com/staeglis/HPOlib2@container
    apt install pyro4 python3-pyro4 -y

%runscript
    python3 -s /usr/local/lib/python3.6/dist-packages/hpolib/container/server/abstract_benchmark.py synthetic_functions $@
```

## Collection

 - Name: [staeglis/HPOlib2](https://github.com/staeglis/HPOlib2)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

