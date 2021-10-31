---
id: 14658
name: "fenz-org/tensorflow"
branch: "master"
tag: "2.1.0-p-python-3.7"
commit: "0bb50500a5dbc5c41ba1d2be48bc7df1081f77f6"
version: "a1c01a4dcc0bcc627c19b5d42907c626ce790f13fa1cb48be4d52368930c2ba8"
build_date: "2020-10-26T22:10:42.929Z"
size_mb: 266.5546875
size: 279502848
sif: "https://datasets.datalad.org/shub/fenz-org/tensorflow/2.1.0-p-python-3.7/2020-10-26-0bb50500-a1c01a4d/a1c01a4dcc0bcc627c19b5d42907c626ce790f13fa1cb48be4d52368930c2ba8.sif"
url: https://datasets.datalad.org/shub/fenz-org/tensorflow/2.1.0-p-python-3.7/2020-10-26-0bb50500-a1c01a4d/
recipe: https://datasets.datalad.org/shub/fenz-org/tensorflow/2.1.0-p-python-3.7/2020-10-26-0bb50500-a1c01a4d/Singularity
collection: fenz-org/tensorflow
---

# fenz-org/tensorflow:2.1.0-p-python-3.7

```bash
$ singularity pull shub://fenz-org/tensorflow:2.1.0-p-python-3.7
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.7.7-slim-buster

%post
    export PATH="/usr/local/bin:/usr/local/sbin:/usr/sbin:/usr/bin:/sbin:/bin"
    export PYTHON_VERSION=3.7.7
    export PY_VER=37
    export TENSORFLOW_VERSION=2.1.0

    apt-get update
    apt-get install -y --no-install-recommends \
        wget
    apt-get clean
    rm -rf /var/lib/apt/lists/*

    cd /tmp
    wget --quiet https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-${TENSORFLOW_VERSION}-cp${PY_VER}-cp${PY_VER}m-manylinux2010_x86_64.whl
    python -m pip install \
        tensorflow_cpu-${TENSORFLOW_VERSION}-cp${PY_VER}-cp${PY_VER}m-manylinux2010_x86_64.whl
    rm tensorflow_cpu-${TENSORFLOW_VERSION}-cp${PY_VER}-cp${PY_VER}m-manylinux2010_x86_64.whl

%environment
    export PATH="/usr/local/bin:/usr/local/sbin:/usr/sbin:/usr/bin:/sbin:/bin"
    export PYTHON_VERSION=3.7.7
```

## Collection

 - Name: [fenz-org/tensorflow](https://github.com/fenz-org/tensorflow)
 - License: None

