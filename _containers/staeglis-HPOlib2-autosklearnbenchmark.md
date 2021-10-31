---
id: 5201
name: "staeglis/HPOlib2"
branch: "container"
tag: "autosklearnbenchmark"
commit: "028b5a201a1adc962ae44a9d3055dacba3aecb03"
version: "c836440ea6fae8c10b73cc5196a69424"
build_date: "2018-12-18T11:55:41.105Z"
size_mb: 1418
size: 538861599
sif: "https://datasets.datalad.org/shub/staeglis/HPOlib2/autosklearnbenchmark/2018-12-18-028b5a20-c836440e/c836440ea6fae8c10b73cc5196a69424.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/staeglis/HPOlib2/autosklearnbenchmark/2018-12-18-028b5a20-c836440e/
recipe: https://datasets.datalad.org/shub/staeglis/HPOlib2/autosklearnbenchmark/2018-12-18-028b5a20-c836440e/Singularity
collection: staeglis/HPOlib2
---

# staeglis/HPOlib2:autosklearnbenchmark

```bash
$ singularity pull shub://staeglis/HPOlib2:autosklearnbenchmark
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
    apt install libopenblas-base libopenblas-dev libblas3 liblas-c3 -y
    pip3 install scipy numpy
    pip3 install git+https://github.com/automl/ConfigSpace.git@master
    apt install python3-sklearn -y
    pip3 install git+https://github.com/staeglis/HPOlib2@container
    pip3 install pyro4
    apt install swig swig3.0 python3-jsonpickle -y
    pip3 install --upgrade pynisher==0.5.0
    pip3 install scikit-learn
    pip3 install auto-sklearn==0.4.2

%runscript
    python3 -s /usr/local/lib/python3.6/dist-packages/hpolib/container/server/abstract_benchmark.py ml.autosklearn_benchmark $@
```

## Collection

 - Name: [staeglis/HPOlib2](https://github.com/staeglis/HPOlib2)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

