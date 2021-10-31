---
id: 10050
name: "sanchezivan/singularity_image_recipes"
branch: "master"
tag: "container4"
commit: "b82626ffe60ece25fe92c2a7e13822f03c3eef3d"
version: "b953d3b1c688b83b526863c38d2cef07"
build_date: "2019-07-30T16:20:08.326Z"
size_mb: 3701
size: 893407263
sif: "https://datasets.datalad.org/shub/sanchezivan/singularity_image_recipes/container4/2019-07-30-b82626ff-b953d3b1/b953d3b1c688b83b526863c38d2cef07.simg"
url: https://datasets.datalad.org/shub/sanchezivan/singularity_image_recipes/container4/2019-07-30-b82626ff-b953d3b1/
recipe: https://datasets.datalad.org/shub/sanchezivan/singularity_image_recipes/container4/2019-07-30-b82626ff-b953d3b1/Singularity
collection: sanchezivan/singularity_image_recipes
---

# sanchezivan/singularity_image_recipes:container4

```bash
$ singularity pull shub://sanchezivan/singularity_image_recipes:container4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%setup
   # setup is run after the base 'centos' image is
   # downloaded and upacked but before entering the 
   # container environment
   
   # this is the path on the local system to 
   # what will become your container's root directory
   echo ${SINGULARITY_ROOTFS}
   # create a directory for your application
   #
   # copy the hello world example from the github to 
   # the app directory
   # cp /hello_world.cpp ${SINGULARITY_ROOTFS}/myapp/
   

%post
   # post is run after entering the container env. 

   # directory structure:
   # /sensei
   # /sensei/build
   # /sensei/src
   # /sensei/install

   # build directory structure
   mkdir /sensei
   mkdir /sensei/build
   mkdir /sensei/src
   mkdir /sensei/install
   
   # need to install some development tools to
   # build our code
   yum update -y
   yum groupinstall -y "Development Tools"
   yum install -y gcc g++
   yum install -y sudo
   yum install -y ncurses-devel
   yum install -y wget
   yum install -y xorg-x11-server-Xorg xorg-x11-xauth xorg-x11-apps 
   yum install -y libXt-devel
   yum install -y freeglut-devel
   yum install -y vim
   yum install -y automake

   # CMake 3.12.3
 
   cd /sensei/src
   wget https://cmake.org/files/v3.12/cmake-3.12.3.tar.gz
   tar xzf cmake-3.12.3.tar.gz
   rm cmake-3.12.3.tar.gz
   cd cmake-3.12.3
   ./bootstrap --prefix=/sensei/install/cmake
   make -j8
   make install

   # add cmake binaries to the path
   export PATH=/sensei/install/cmake/bin:$PATH


   # MPICH
   
   cd /sensei/src
   wget -q http://www.mpich.org/static/downloads/3.2.1/mpich-3.2.1.tar.gz
   tar xzf mpich-3.2.1.tar.gz
   rm mpich-3.2.1.tar.gz
   
   cd mpich-3.2.1
   # disable the addition of the RPATH to compiled executables
   # this allows us to override the MPI libraries to use those
   # found via LD_LIBRARY_PATH
   ./configure --prefix=/usr/local/mpich/install --disable-wrapper-rpath
   make -j8 
   make install
   # add to local environment
   export PATH=/usr/local/mpich/install/bin:$PATH
   export LD_LIBRARY_PATH=/usr/local/mpich/install/lib:$LD_LIBRARY_PATH


   # ADIOS

   # build flexpath first, according to ADIOS manual
   cd /sensei/build
   mkdir chaos
   cd chaos
   wget https://gtkorvo.github.io/korvo_bootstrap.pl
   perl ./korvo_bootstrap.pl adios-1.13.1 /sensei/install/chaos
   mv korvo_build_config korvo_build_config.bak
   awk '{ gsub("^korvogithub configure", "korvogithub configure --disable-shared CFLAGS=\"-fPIC\""); \
          gsub("^korvogithub cmake", "korvogithub cmake -DBUILD_SHARED_LIBS=OFF -DBUILD_SHARED_STATIC=STATIC \
         -DCMAKE_C_FLAGS=-fPIC -DCMAKE_CXX_FLAGS=-fPIC"); print $0}' \
         korvo_build_config.bak > korvo_build_config
   perl ./korvo_build.pl
     
   # get ADIOS source
   cd /sensei/src
   wget https://users.nccs.gov/~pnorbert/adios-1.13.1.tar.gz
   tar zxf adios-1.13.1.tar.gz
   rm -f adios-1.13.1.tar.gz
   
   # configure, build and install
   cd /sensei/build
   mkdir adios
   cd adios
   /sensei/src/adios-1.13.1/configure --prefix=/sensei/install/adios --with-flexpath=/sensei/install/chaos CFLAGS="-fPIC"     
   make -j8
   make install

   
   # VTK

   cd /sensei/src
   wget https://www.vtk.org/files/release/8.2/VTK-8.2.0.tar.gz
   tar xzf VTK-8.2.0.tar.gz
   rm VTK-8.2.0.tar.gz

   cd /sensei/build
   mkdir vtk
   cd vtk

   cmake \
     -DCMAKE_INSTALL_PREFIX=/sensei/install/vtk \
   /sensei/src/VTK-8.2.0
   
   make -j8
   make install 
   
   
   # SENSEI

   cd /sensei/src
   git clone https://gitlab.kitware.com/sensei/sensei.git
   cd sensei
   git checkout v2.1.1

   cd /sensei/build
   mkdir sensei
   cd sensei

   cmake \
     -DENABLE_SENSEI=ON \
     -DENABLE_ADIOS=ON \
     -DENABLE_PARALLEL3D=OFF \
     -DENABLE_VTK_IO=ON \
     -DENABLE_VTK_MPI=OFF \
     -DCMAKE_INSTALL_PREFIX=/sensei/install/sensei \
     -DVTK_DIR=/sensei/install/vtk/lib64/cmake/vtk-8.2 \
     -DADIOS_DIR=/sensei/install/adios \
   /sensei/src/sensei
   
   make -j8
   make install
   
%runscript
   # run script
   # /myapp/hello_world

%environment
   # can define runtime environment variables here
   # these vars will be set during calls to 'shell'
   # or 'exec' or 'run' but will not be set during
   # the previous 'post' section of the recipe file
   # so, if you need them, define them there as well
   
   export PATH=/usr/local/mpich/install/bin/:/sensei/install/sensei/bin:${PATH}
   export LD_LIBRARY_PATH=/usr/local/mpich/install/lib/:/sensei/install/vtk/lib64:${LD_LIBRARY_PATH}
   #export PATH=$PATH:/myapp
```

## Collection

 - Name: [sanchezivan/singularity_image_recipes](https://github.com/sanchezivan/singularity_image_recipes)
 - License: None

