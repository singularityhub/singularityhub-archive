---
id: 5498
name: "jtchilders/singularity_gpu_tensorflow"
branch: "master"
tag: "mpich"
commit: "87ffa359e22e106d9737a67839ab6c94b65c04a4"
version: "279aaa79712720fc63aaf853de48ba07"
build_date: "2018-11-07T13:35:08.002Z"
size_mb: 797
size: 233660447
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_gpu_tensorflow/mpich/2018-11-07-87ffa359-279aaa79/279aaa79712720fc63aaf853de48ba07.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jtchilders/singularity_gpu_tensorflow/mpich/2018-11-07-87ffa359-279aaa79/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_gpu_tensorflow/mpich/2018-11-07-87ffa359-279aaa79/Singularity
collection: jtchilders/singularity_gpu_tensorflow
---

# jtchilders/singularity_gpu_tensorflow:mpich

```bash
$ singularity pull shub://jtchilders/singularity_gpu_tensorflow:mpich
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%setup
   # make directory for test MPI program
   mkdir ${SINGULARITY_ROOTFS}/mpitestapp
   cp pi.c ${SINGULARITY_ROOTFS}/mpitestapp/
   # make directory for MPICH
   mkdir ${SINGULARITY_ROOTFS}/mpich
   cd ${SINGULARITY_ROOTFS}/mpich/
   wget -q http://www.mpich.org/static/downloads/3.2.1/mpich-3.2.1.tar.gz
   tar xf mpich-3.2.1.tar.gz --strip-components=1

%post
   # install development tools
   yum update -y
   yum groupinstall -y "Development Tools"
   yum install -y gcc
   yum install -y gcc-c++
   # yum install -y wget
   # install MPICH
   cd /mpich
   # disable the addition of the RPATH to compiled executables
   # this allows us to override the MPI libraries to use those
   # found via LD_LIBRARY_PATH
   ./configure --prefix=/mpich/install --disable-wrapper-rpath
   make -j 4 install
   # add to local environment to build pi.c
   export PATH=$PATH:/mpich/install/bin
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich/install/lib
   env | sort
   cd /mpitestapp
   mpicc -o pi -fPIC pi.c

%runscript
   /mpitestapp/pi
```

## Collection

 - Name: [jtchilders/singularity_gpu_tensorflow](https://github.com/jtchilders/singularity_gpu_tensorflow)
 - License: None

