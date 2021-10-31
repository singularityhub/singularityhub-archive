---
id: 9626
name: "sanchezivan/singularity_image_recipes"
branch: "master"
tag: "cooley3"
commit: "bb1e805cf567c177333bd4084bd8e1ab2415b528"
version: "11379030b2a0c3343872472a25af50d2"
build_date: "2019-06-07T11:19:42.267Z"
size_mb: 3045
size: 868220959
sif: "https://datasets.datalad.org/shub/sanchezivan/singularity_image_recipes/cooley3/2019-06-07-bb1e805c-11379030/11379030b2a0c3343872472a25af50d2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sanchezivan/singularity_image_recipes/cooley3/2019-06-07-bb1e805c-11379030/
recipe: https://datasets.datalad.org/shub/sanchezivan/singularity_image_recipes/cooley3/2019-06-07-bb1e805c-11379030/Singularity
collection: sanchezivan/singularity_image_recipes
---

# sanchezivan/singularity_image_recipes:cooley3

```bash
$ singularity pull shub://sanchezivan/singularity_image_recipes:cooley3
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
   mkdir ${SINGULARITY_ROOTFS}/myapp
   # copy the hello world example from the github to 
   # the app directory
   # cp /hello_world.cpp ${SINGULARITY_ROOTFS}/myapp/
   mkdir ${SINGULARITY_ROOTFS}/config
   cp adiosconfig ${SINGULARITY_ROOTFS}/config/adiosconfig
 
%post
   # post is run after entering the container env. 
   
   # need to install some development tools to
   # build our code
   yum update -y
   yum groupinstall -y "Development Tools"
   yum install -y gcc g++
   yum install sudo -y
    
    # This installs CMake 3.12.3 as well as command wget
   yum install -y ncurses-devel
   yum install -y wget
   wget https://cmake.org/files/v3.12/cmake-3.12.3.tar.gz
   tar zxvf cmake-3.*
   cd cmake-3.12.3
   ./bootstrap --prefix=/usr/local
   make -j$(nproc)
   make install
   cd ..

   # Installs VTK
   git clone git://vtk.org/VTK.git VTK
   mkdir VTK-build
   cd VTK-build
   yum install  xorg-x11-server-Xorg xorg-x11-xauth xorg-x11-apps -y
   yum install -y libXt-devel
   yum install -y freeglut-devel
   cmake  -DVTK_BUILD_TESTING:STRING=OFF ../VTK
   make
   cp vtk-config.cmake VTKConfig.cmake
   cd ..
   
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
    
   
   #Installing ADIOS
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
   
   # Installing SENSEI
   git clone https://github.com/Kitware/sensei.git
   cd sensei/
   echo "set_property(TARGET parallel3d PROPERTY C_STANDARD 99)" >> CMakeLists.txt
   mkdir build
   cd build/
   cmake -DENABLE_SENSEI=ON -DENABLE_ADIOS=ON -DVTK_DIR=OFF -DADIOS_DIR=/root/adios-1.13.1/build  ..
   make 
   make install

   yum install -y vim
   # enter directory where source file was copied
   cd /myapp
   
   # build
   # g++ -o hello_world hello_world.cpp

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
   export PATH=$PATH:/myapp
```

## Collection

 - Name: [sanchezivan/singularity_image_recipes](https://github.com/sanchezivan/singularity_image_recipes)
 - License: None

