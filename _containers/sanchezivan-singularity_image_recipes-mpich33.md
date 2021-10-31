---
id: 9323
name: "sanchezivan/singularity_image_recipes"
branch: "master"
tag: "mpich33"
commit: "da8c885dde34aa9a3925f2617734a022cdcb328f"
version: "732ab7780103eb9f20e2ed7ecc542c02"
build_date: "2019-05-25T06:40:09.481Z"
size_mb: 756
size: 257978399
sif: "https://datasets.datalad.org/shub/sanchezivan/singularity_image_recipes/mpich33/2019-05-25-da8c885d-732ab778/732ab7780103eb9f20e2ed7ecc542c02.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sanchezivan/singularity_image_recipes/mpich33/2019-05-25-da8c885d-732ab778/
recipe: https://datasets.datalad.org/shub/sanchezivan/singularity_image_recipes/mpich33/2019-05-25-da8c885d-732ab778/Singularity
collection: sanchezivan/singularity_image_recipes
---

# sanchezivan/singularity_image_recipes:mpich33

```bash
$ singularity pull shub://sanchezivan/singularity_image_recipes:mpich33
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%setup
   # make directory for test MPI program
   mkdir ${SINGULARITY_ROOTFS}/mpitestapp
   cp example_codes/pi.c ${SINGULARITY_ROOTFS}/mpitestapp/

%post
   # install development tools
   yum update -y
   yum groupinstall -y "Development Tools"
   yum install -y gcc gcc-c++ wget
   yum install -y epel-release
   yum install -y python-pip
   yum update -y
   pip install numpy

   
   # install MPICH
   wget -q http://www.mpich.org/static/downloads/3.2.1/mpich-3.2.1.tar.gz
   tar xf mpich-3.2.1.tar.gz
   rm mpich-3.2.1.tar.gz
   cd mpich-3.2.1
   # disable the addition of the RPATH to compiled executables
   # this allows us to override the MPI libraries to use those
   # found via LD_LIBRARY_PATH
   ./configure --prefix=/usr/local/mpich/install --disable-wrapper-rpath
   make -j 4 install
   # add to local environment to build pi.c
   export PATH=$PATH:/usr/local/mpich//install/bin
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/mpich//install/lib
   env | sort
   cd ..
   rm -rf mpich-3.2.1

%environment
   export PATH=/usr/local/mpich/install/bin/:${PATH}
   export LD_LIBRARY_PATH=/usr/local/mpich/install/lib/:${LD_LIBRARY_PATH}

%runscript
   /mpitestapp/pi
```

## Collection

 - Name: [sanchezivan/singularity_image_recipes](https://github.com/sanchezivan/singularity_image_recipes)
 - License: None

