---
id: 9835
name: "sanchezivan/singularity_image_recipes"
branch: "master"
tag: "container2"
commit: "7bdc6864a79e53900d8d87caf0f246a77ef89d8b"
version: "d3b1007bbc6ed9bf07262cdd11be10d8"
build_date: "2019-06-18T22:10:58.550Z"
size_mb: 3385
size: 786952223
sif: "https://datasets.datalad.org/shub/sanchezivan/singularity_image_recipes/container2/2019-06-18-7bdc6864-d3b1007b/d3b1007bbc6ed9bf07262cdd11be10d8.simg"
url: https://datasets.datalad.org/shub/sanchezivan/singularity_image_recipes/container2/2019-06-18-7bdc6864-d3b1007b/
recipe: https://datasets.datalad.org/shub/sanchezivan/singularity_image_recipes/container2/2019-06-18-7bdc6864-d3b1007b/Singularity
collection: sanchezivan/singularity_image_recipes
---

# sanchezivan/singularity_image_recipes:container2

```bash
$ singularity pull shub://sanchezivan/singularity_image_recipes:container2
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
   
   # silvio
   # why this?
   #mkdir ${SINGULARITY_ROOTFS}/config

   # silvio
   # do we need this line?
   #cp adiosconfig ${SINGULARITY_ROOTFS}/config/adiosconfig


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
   yum install -y automake
   yum install -y vim
   yum install -y mlocate


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

   #cmake -DENABLE_SENSEI=ON -DENABLE_ADIOS=ON -DVTK_DIR=OFF -DADIOS_DIR=/root/adios-1.13.1/build  ..

   cmake \
     -DENABLE_SENSEI=ON \
     -DENABLE_PARALLEL3D=OFF \
     -DENABLE_VTK_IO=ON \
     -DENABLE_VTK_MPI=OFF \
     -DCMAKE_INSTALL_PREFIX=/sensei/install/sensei \
     -DVTK_DIR=/sensei/install/vtk/lib64/cmake/vtk-8.2 \
   /sensei/src/sensei
 
   make -j8
   make install
   
   
          
   # ADIOS
   # Silvio
   # no adios for now

   cd /sensei/src
   wget https://users.nccs.gov/~pnorbert/adios-1.13.1.tar.gz
   tar zxf adios-1.13.1.tar.gz
   
   cd adios-1.13.1
   wget http://ftp.gnu.org/gnu/automake/automake-1.13.tar.gz
   tar xf automake-1.13.tar.gz
   cd automake-1.13
   ./configure
   make
   make install
   cd ..
   
   # This installs MXML (needed to complete ADIOS installation)
   wget https://github.com/michaelrsweet/mxml/releases/download/release-2.9/mxml-2.9.tar.gz
   tar xf mxml-2.9.tar.gz
   cd mxml-2.9
   ./configure
   make
   make install
   cd ..
   mkdir build
   cd build
   ../configure -prefix=/root/adios-1.13.1/build CFLAGS="-fPIC"
   make
   make install
   
   updatedb


%runscript
   # run script
   # /myapp/hello_world

%environment
   # can define runtime environment variables here
   # these vars will be set during calls to 'shell'
   # or 'exec' or 'run' but will not be set during
   # the previous 'post' section of the recipe file
   # so, if you need them, define them there as well
   
   export PATH=/usr/local/mpich/install/bin/:${PATH}
   export LD_LIBRARY_PATH=/usr/local/mpich/install/lib/:${LD_LIBRARY_PATH}
   #export PATH=$PATH:/myapp
```

## Collection

 - Name: [sanchezivan/singularity_image_recipes](https://github.com/sanchezivan/singularity_image_recipes)
 - License: None

