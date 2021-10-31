---
id: 10148
name: "cailmdaley/s2"
branch: "master"
tag: "latest"
commit: "ecc64d5ca956fda0bef6c0faa51468588dee7162"
version: "f62331ec8825ec9409a40689d35db08c"
build_date: "2019-07-04T08:37:38.271Z"
size_mb: 690
size: 233652255
sif: "https://datasets.datalad.org/shub/cailmdaley/s2/latest/2019-07-04-ecc64d5c-f62331ec/f62331ec8825ec9409a40689d35db08c.simg"
url: https://datasets.datalad.org/shub/cailmdaley/s2/latest/2019-07-04-ecc64d5c-f62331ec/
recipe: https://datasets.datalad.org/shub/cailmdaley/s2/latest/2019-07-04-ecc64d5c-f62331ec/Singularity
collection: cailmdaley/s2
---

# cailmdaley/s2:latest

```bash
$ singularity pull shub://cailmdaley/s2:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:latest

%post
   apt-get update
   apt-get install -y git cmake g++ swig python-dev ipython
   apt-get install -y libgflags-dev libgoogle-glog-dev libgtest-dev libssl-dev
   
   git clone https://github.com/google/s2geometry.git
   
   cd s2geometry && mkdir build && cd build
   cmake .. \
   -DCMAKE_INSTALL_PREFIX=/usr \
   -DWITH_GFLAGS=ON \
   -WITH_GTEST=ON -DGTEST_ROOT=/usr/src/gtest \
   -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
   -DPYTHON_LIBRARY=/usr/lib/python2.7/config-x86_64-linux-gnu/libpython2.7.so
   
   make && make install
   
%test 
   cd s2geometry/build
   make test
```

## Collection

 - Name: [cailmdaley/s2](https://github.com/cailmdaley/s2)
 - License: None

