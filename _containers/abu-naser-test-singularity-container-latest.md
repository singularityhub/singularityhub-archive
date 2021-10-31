---
id: 5266
name: "abu-naser/test-singularity-container"
branch: "master"
tag: "latest"
commit: "463c20d0b818207642e95ae62df65fe3c50a53a2"
version: "8dd5de710f41b30a26ec44a7b8ae05c4"
build_date: "2018-10-18T17:22:06.242Z"
size_mb: 1521
size: 636293151
sif: "https://datasets.datalad.org/shub/abu-naser/test-singularity-container/latest/2018-10-18-463c20d0-8dd5de71/8dd5de710f41b30a26ec44a7b8ae05c4.simg"
url: https://datasets.datalad.org/shub/abu-naser/test-singularity-container/latest/2018-10-18-463c20d0-8dd5de71/
recipe: https://datasets.datalad.org/shub/abu-naser/test-singularity-container/latest/2018-10-18-463c20d0-8dd5de71/Singularity
collection: abu-naser/test-singularity-container
---

# abu-naser/test-singularity-container:latest

```bash
$ singularity pull shub://abu-naser/test-singularity-container:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: singularityhub/ubuntu

%setup
   # make directory for test MPI program
   mkdir ${SINGULARITY_ROOTFS}/mpitestapp
   # copy test file into directory

%post
   apt-get update
   apt-get -y install build-essential g++ git wget

   # build openmpi
   mkdir /openmpi-3.1.2
   cd /openmpi-3.1.2
   wget https://download.open-mpi.org/release/open-mpi/v3.1/openmpi-3.1.2.tar.gz
   tar xf openmpi-3.1.2.tar.gz --strip-components=1
   # disable the addition of the RPATH to compiled executables
   # this allows us to override the MPI libraries to use those
   # found via LD_LIBRARY_PATH
   ./configure --prefix=/usr/local 
   make -j 4 install
   
   export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
   export PATH=/usr/local/bin:$PATH

   cd /mpitestapp
   
   
   mkdir /go
   cd /go
   wget https://dl.google.com/go/go1.11.1.linux-amd64.tar.gz
   tar -C /usr/local -xzf go1.11.1.linux-amd64.tar.gz
   export PATH=$PATH:/usr/local/go/bin
   export GOPATH=/go
   go get -v go.etcd.io/etcd
   src/go.etcd.io/etcd/build
   

%environment
   # following environment variable will be available via all Singularity actmkion commands (e.g. shell, run, exec).
   LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
   export LD_LIBRARY_PATH
   PATH=/usr/local/bin:/usr/local/go/bin:$PATH
   export PATH
   GOPATH=/go
   export GOPATH
	
%runscript
   echo "Helloooooooo!"
```

## Collection

 - Name: [abu-naser/test-singularity-container](https://github.com/abu-naser/test-singularity-container)
 - License: None

