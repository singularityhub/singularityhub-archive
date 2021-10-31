---
id: 5852
name: "hongchengkuan/cornell-moe-singularity"
branch: "master"
tag: "centos7"
commit: "8e4b115db3fa7fa4d847af3108f6eb0d61d263bc"
version: "c4b0d1cdf3813b37fb9e73174d869a25"
build_date: "2018-12-12T21:53:22.453Z"
size_mb: 509
size: 158187551
sif: "https://datasets.datalad.org/shub/hongchengkuan/cornell-moe-singularity/centos7/2018-12-12-8e4b115d-c4b0d1cd/c4b0d1cdf3813b37fb9e73174d869a25.simg"
url: https://datasets.datalad.org/shub/hongchengkuan/cornell-moe-singularity/centos7/2018-12-12-8e4b115d-c4b0d1cd/
recipe: https://datasets.datalad.org/shub/hongchengkuan/cornell-moe-singularity/centos7/2018-12-12-8e4b115d-c4b0d1cd/Singularity
collection: hongchengkuan/cornell-moe-singularity
---

# hongchengkuan/cornell-moe-singularity:centos7

```bash
$ singularity pull shub://hongchengkuan/cornell-moe-singularity:centos7
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:centos7.5.1804

%post
  # yum -y update && yum -y upgrade
  yum  install -y python-dev gcc cmake \
                  boost-devel doxygen \
                  openblas-devel lapack-devel 

  # apt-get install -y  python-dev gcc cmake \
  #                     libboost-all-dev python-pip doxygen \
  #                     libblas-dev liblapack-dev gfortran \
  #                     git wget octave
  #                      

  # apt-get clean
  # 
  # cd /opt
  # wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O /opt/miniconda.sh
  # bash /opt/miniconda.sh -b -p /opt/miniconda
  # rm /opt/miniconda.sh
  # echo "export PATH="/opt/miniconda/bin:$PATH"" >> $SINGULARITY_ENVIRONMENT
  # export PATH="/opt/miniconda/bin:$PATH"
  # conda install pip
  # pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

  # export MOE_CC_PATH="$(which gcc)"
  # export MOE_CXX_PATH="$(which g++)"
  # export MOE_CMAKE_OPTS="-D MOE_PYTHON_INCLUDE_DIR=/usr/include/python2.7 -D MOE_PYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython2.7.so.1.0"

  # cd /
  # mkdir /moe && cd /moe
  # git clone https://github.com/wujian16/Cornell-MOE.git
  # cd Cornell-MOE
  # pip install -r requirements.txt
  # python setup.py install
  # pip install keras
  # pip install tensorflow
  # conda install -c conda-forge oct2py

  # # Clean up
  # apt-get -y autoremove
  # rm -rvf /var/lib/apt/lists/*
```

## Collection

 - Name: [hongchengkuan/cornell-moe-singularity](https://github.com/hongchengkuan/cornell-moe-singularity)
 - License: None

