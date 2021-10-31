---
id: 5393
name: "hongchengkuan/cornell-moe-singularity"
branch: "master"
tag: "latest"
commit: "8670926cb0e95e19fd75bda81c0450d9fa3a0635"
version: "c28cef5a534de1a831d430205172df81"
build_date: "2018-12-04T00:53:19.983Z"
size_mb: 3617
size: 1365577759
sif: "https://datasets.datalad.org/shub/hongchengkuan/cornell-moe-singularity/latest/2018-12-04-8670926c-c28cef5a/c28cef5a534de1a831d430205172df81.simg"
url: https://datasets.datalad.org/shub/hongchengkuan/cornell-moe-singularity/latest/2018-12-04-8670926c-c28cef5a/
recipe: https://datasets.datalad.org/shub/hongchengkuan/cornell-moe-singularity/latest/2018-12-04-8670926c-c28cef5a/Singularity
collection: hongchengkuan/cornell-moe-singularity
---

# hongchengkuan/cornell-moe-singularity:latest

```bash
$ singularity pull shub://hongchengkuan/cornell-moe-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
  apt-get update && apt-get -y install locales
  locale-gen en_US.UTF-8
  apt-get install -y  python-dev gcc cmake \
                      libboost-all-dev python-pip doxygen \
                      libblas-dev liblapack-dev gfortran \
                      git wget octave
                       

  apt-get clean
  
  cd /opt
  wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O /opt/miniconda.sh
  bash /opt/miniconda.sh -b -p /opt/miniconda
  rm /opt/miniconda.sh
  echo "export PATH="/opt/miniconda/bin:$PATH"" >> $SINGULARITY_ENVIRONMENT
  export PATH="/opt/miniconda/bin:$PATH"
  conda install pip
  pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

  export MOE_CC_PATH="$(which gcc)"
  export MOE_CXX_PATH="$(which g++)"
  export MOE_CMAKE_OPTS="-D MOE_PYTHON_INCLUDE_DIR=/usr/include/python2.7 -D MOE_PYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython2.7.so.1.0"

  cd /
  mkdir /moe && cd /moe
  git clone https://github.com/wujian16/Cornell-MOE.git
  cd Cornell-MOE
  pip install -r requirements.txt
  python setup.py install
  pip install keras
  pip install tensorflow
  conda install -c conda-forge oct2py

  # Clean up
  apt-get -y autoremove
  rm -rvf /var/lib/apt/lists/*
```

## Collection

 - Name: [hongchengkuan/cornell-moe-singularity](https://github.com/hongchengkuan/cornell-moe-singularity)
 - License: None

