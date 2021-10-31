---
id: 15547
name: "timo-singularity/sherpa"
branch: "master"
tag: "latest"
commit: "27b1ad9a8becd1fd717c215091ce3942e50523cc"
version: "9abedc5dd073cae2aa7e1a6eeb48f20e"
build_date: "2021-04-05T19:44:22.178Z"
size_mb: 4582.0
size: 933527583
sif: "https://datasets.datalad.org/shub/timo-singularity/sherpa/latest/2021-04-05-27b1ad9a-9abedc5d/9abedc5dd073cae2aa7e1a6eeb48f20e.sif"
url: https://datasets.datalad.org/shub/timo-singularity/sherpa/latest/2021-04-05-27b1ad9a-9abedc5d/
recipe: https://datasets.datalad.org/shub/timo-singularity/sherpa/latest/2021-04-05-27b1ad9a-9abedc5d/Singularity
collection: timo-singularity/sherpa
---

# timo-singularity/sherpa:latest

```bash
$ singularity pull shub://timo-singularity/sherpa:latest
```

## Singularity Recipe

```singularity
#Bootstrap: localimage
#From: ./rivet.sif
Bootstrap: shub
From: timo-singularity/rivet

%help

  Container with Sherpa

%environment
  
  PYTHONPATH=/usr/local/lib/python3.6/site-packages:$PYTHONPATH
  export PYTHONPATH

%post

  yum -y install swig sqlite-devel

  # install lhapdf
  wget https://lhapdf.hepforge.org/downloads/?f=LHAPDF-6.3.0.tar.gz -O LHAPDF-6.3.0.tar.gz
  tar xvf LHAPDF-6.3.0.tar.gz
  rm LHAPDF-6.3.0.tar.gz
  cd LHAPDF-6.3.0
  ./configure --prefix=/usr/local
  make -j3
  make install
  
  # install Sherpa
  wget https://sherpa.hepforge.org/downloads/?f=SHERPA-MC-2.2.10.tar.gz -O SHERPA-MC-2.2.10.tar.gz
  tar xvf SHERPA-MC-2.2.10.tar.gz
  rm SHERPA-MC-2.2.10.tar.gz
  cd SHERPA-MC-2.2.10
  wget https://raw.githubusercontent.com/timo-singularity/sherpa/master/fix-memory-leak-in-python-interface.patch
  patch -p1 < fix-memory-leak-in-python-interface.patch
  ./configure --prefix=/usr/local \
    --enable-pyext \
    --enable-analysis \
    --enable-fastjet=/usr/local \
    --enable-hepmc2=/usr/local \
    --enable-lhapdf=/usr/local \
    --enable-rivet=/usr/local \
    --enable-gzip \
    --with-sqlite3=/usr
  make -j3 && make install

  ldconfig
  yum clean all
```

## Collection

 - Name: [timo-singularity/sherpa](https://github.com/timo-singularity/sherpa)
 - License: None

