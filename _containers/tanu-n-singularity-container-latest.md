---
id: 5268
name: "tanu-n/singularity-container"
branch: "master"
tag: "latest"
commit: "fd06a4d39166193d69fafc1a73dc5df4b55c32b5"
version: "489e204ad1ad057ce78f2e8c9cee3628"
build_date: "2018-10-19T18:21:08.379Z"
size_mb: 1521
size: 636284959
sif: "https://datasets.datalad.org/shub/tanu-n/singularity-container/latest/2018-10-19-fd06a4d3-489e204a/489e204ad1ad057ce78f2e8c9cee3628.simg"
url: https://datasets.datalad.org/shub/tanu-n/singularity-container/latest/2018-10-19-fd06a4d3-489e204a/
recipe: https://datasets.datalad.org/shub/tanu-n/singularity-container/latest/2018-10-19-fd06a4d3-489e204a/Singularity
collection: tanu-n/singularity-container
---

# tanu-n/singularity-container:latest

```bash
$ singularity pull shub://tanu-n/singularity-container:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: singularityhub/ubuntu

%setup
   # make directory for test MPI program
   mkdir ${SINGULARITY_ROOTFS}/mpitestapp
   # copy test file into directory
   cp get_key.sh ${SINGULARITY_ROOTFS}/mpitestapp/ 

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

 - Name: [tanu-n/singularity-container](https://github.com/tanu-n/singularity-container)
 - License: None

