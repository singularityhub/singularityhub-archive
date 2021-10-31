---
id: 1370
name: "belledon/moe-sing"
branch: "master"
tag: "latest"
commit: "ec588254180ee0beb598b288bd8074064e531066"
version: "ddfb1d4176e10c639590b648c814cb57"
build_date: "2018-01-19T12:33:35.473Z"
size_mb: 1377
size: 474832927
sif: "https://datasets.datalad.org/shub/belledon/moe-sing/latest/2018-01-19-ec588254-ddfb1d41/ddfb1d4176e10c639590b648c814cb57.simg"
url: https://datasets.datalad.org/shub/belledon/moe-sing/latest/2018-01-19-ec588254-ddfb1d41/
recipe: https://datasets.datalad.org/shub/belledon/moe-sing/latest/2018-01-19-ec588254-ddfb1d41/Singularity
collection: belledon/moe-sing
---

# belledon/moe-sing:latest

```bash
$ singularity pull shub://belledon/moe-sing:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
  apt-get update && apt-get -y install locales
  locale-gen en_US.UTF-8
  apt-get install -y  python python-dev gcc cmake \
                      libboost-all-dev python-pip doxygen \
                      libblas-dev liblapack-dev gfortran \
                      git python-numpy python-scipy

  apt-get clean
  
  export MOE_CC_PATH="$(which gcc)"
  export MOE_CXX_PATH="$(which g++)"
  export MOE_CMAKE_OPTS="-D MOE_PYTHON_INCLUDE_DIR=/usr/include/python2.7 -D MOE_PYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython2.7.so.1.0"

  cd /
  mkdir /moe && cd /moe
  git clone https://github.com/wujian16/Cornell-MOE.git
  cd Cornell-MOE
  pip install -r requirements.txt
  python setup.py install
```

## Collection

 - Name: [belledon/moe-sing](https://github.com/belledon/moe-sing)
 - License: None

