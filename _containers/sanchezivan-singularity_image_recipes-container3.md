---
id: 9960
name: "sanchezivan/singularity_image_recipes"
branch: "master"
tag: "container3"
commit: "1b53e4373316dfc0561e75471cca0cb7b83e02c0"
version: "2009274351f7809384bd1262db5d5b97"
build_date: "2019-06-25T05:49:30.314Z"
size_mb: 3375
size: 782708767
sif: "https://datasets.datalad.org/shub/sanchezivan/singularity_image_recipes/container3/2019-06-25-1b53e437-20092743/2009274351f7809384bd1262db5d5b97.simg"
url: https://datasets.datalad.org/shub/sanchezivan/singularity_image_recipes/container3/2019-06-25-1b53e437-20092743/
recipe: https://datasets.datalad.org/shub/sanchezivan/singularity_image_recipes/container3/2019-06-25-1b53e437-20092743/Singularity
collection: sanchezivan/singularity_image_recipes
---

# sanchezivan/singularity_image_recipes:container3

```bash
$ singularity pull shub://sanchezivan/singularity_image_recipes:container3
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
   yum install -y mlocate
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
  
   cd /sensei/src
   wget https://users.nccs.gov/~pnorbert/adios-1.13.1.tar.gz
   tar zxf adios-1.13.1.tar.gz
   rm -f adios-1.13.1.tar.gz
   cd adios-1.13.1
   mkdir build
   cd build
   ../configure -prefix=/sensei/install/adios CFLAGS="-fPIC"
   make
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

