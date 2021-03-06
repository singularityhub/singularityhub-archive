---
id: 1372
name: "bilke/singularity-recipes"
branch: "master"
tag: "centos7.ogs_6.1.0"
commit: "b40f409a736a679691f5477bedb43049841705be"
version: "3480b1cafc3793e1babeb70978cbf7e2"
build_date: "2018-01-19T14:04:59.451Z"
size_mb: None
size: 757166111
sif: "https://datasets.datalad.org/shub/bilke/singularity-recipes/centos7.ogs_6.1.0/2018-01-19-b40f409a-3480b1ca/3480b1cafc3793e1babeb70978cbf7e2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bilke/singularity-recipes/centos7.ogs_6.1.0/2018-01-19-b40f409a-3480b1ca/
recipe: https://datasets.datalad.org/shub/bilke/singularity-recipes/centos7.ogs_6.1.0/2018-01-19-b40f409a-3480b1ca/Singularity
collection: bilke/singularity-recipes
---

# bilke/singularity-recipes:centos7.ogs_6.1.0

```bash
$ singularity pull shub://bilke/singularity-recipes:centos7.ogs_6.1.0
```

## Singularity Recipe

```singularity
# GCC 5.3.1
Bootstrap: docker
From: centos/devtoolset-4-toolchain-centos7

%environment
    CC=/opt/rh/devtoolset-4/root/bin/gcc
    CXX=/opt/rh/devtoolset-4/root/bin/g++
    LD_LIBRARY_PATH=/opt/rh/devtoolset-4/root/usr/lib/gcc/x86_64-redhat-linux/5.3.1:$LD_LIBRARY_PATH
    unset HOME
    export CC CXX LD_LIBRARY_PATH

%post
    # For Conan Qt package
    #yum -y install libSM libX11 libXext libXt libGLU
    #ln -sf /usr/lib64 /usr/lib/x86_64-linux-gnu
    #ln -sf /usr/lib64/libSM.so.6 /usr/lib64/libSM.so
    #ln -sf /usr/lib64/libICE.so.6 /usr/lib64/libICE.so
    #ln -sf /usr/lib64/libX11.so.6 /usr/lib64/libX11.so
    #ln -sf /usr/lib64/libXext.so.6 /usr/lib64/libXext.so
    #ln -sf /usr/lib64/libXt.so.6 /usr/lib64/libXt.so
    #ln -sf /usr/lib64/libGLU.so.1 /usr/lib64/libGLU.so
    #ln -sf /usr/lib64/libGL.so.1 /usr/lib64/libGL.so


##############################
# release
##############################

%appinstall release
  curl https://docs.opengeosys.org/assets/releases/6.1.0/ogs-6.1.0-Linux-4.4.0-104-generic-x64.tar.gz -O
  tar xf ogs-6.1.0-Linux-4.4.0-104-generic-x64.tar.gz
  rm ogs-6.1.0-Linux-4.4.0-104-generic-x64.tar.gz

%apprun release
  $SINGULARITY_APPROOT/ogs-6.1.0-Linux-4.4.0-104-generic-x64/bin/ogs


##############################
# dev
##############################

%appenv dev
  CC=/opt/rh/devtoolset-4/root/bin/gcc
  CXX=/opt/rh/devtoolset-4/root/bin/g++
  export CC CXX

%appinstall dev
  yum -y install epel-release
  yum -y install git
  curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.rpm.sh | bash
  yum -y install git-lfs

  yum -y install python-pip unzip

  python -m pip install --upgrade pip
  python -m pip install cmake conan

  curl -L -o ninja-linux.zip https://github.com/ninja-build/ninja/releases/download/v1.8.2/ninja-linux.zip
  unzip ninja-linux.zip
  mv ninja /usr/local/bin/ninja
  rm ninja-linux.zip

  # build ogs here
  git lfs clone --branch 6.1.0 --depth=1 https://github.com/ufz/ogs
  mkdir build
  cd build
  CC=/opt/rh/devtoolset-4/root/bin/gcc cmake CXX=/opt/rh/devtoolset-4/root/bin/g++ ../ogs -G Ninja -DCMAKE_BUILD_TYPE=Release -DOGS_USE_CONAN=ON -DCMAKE_INSTALL_PREFIX=$SINGULARITY_APPROOT
  ninja -j 1 install

%apprun dev
  exec $SINGULARITY_APPROOT/bin/ogs "$@"
```

## Collection

 - Name: [bilke/singularity-recipes](https://github.com/bilke/singularity-recipes)
 - License: None

