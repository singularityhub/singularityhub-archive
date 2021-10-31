---
id: 4723
name: "cb-geo/mpm-container"
branch: "master"
tag: "latest"
commit: "9c0871b0ee74bb4c8b60e0ca4bf47ad58f699752"
version: "37d78232f165c752a9d01c0bf7d01377"
build_date: "2018-11-07T13:35:01.485Z"
size_mb: 3900
size: 1103241247
sif: "https://datasets.datalad.org/shub/cb-geo/mpm-container/latest/2018-11-07-9c0871b0-37d78232/37d78232f165c752a9d01c0bf7d01377.simg"
url: https://datasets.datalad.org/shub/cb-geo/mpm-container/latest/2018-11-07-9c0871b0-37d78232/
recipe: https://datasets.datalad.org/shub/cb-geo/mpm-container/latest/2018-11-07-9c0871b0-37d78232/Singularity
collection: cb-geo/mpm-container
---

# cb-geo/mpm-container:latest

```bash
$ singularity pull shub://cb-geo/mpm-container:latest
```

## Singularity Recipe

```singularity
BootStrap:docker
From:fedora:29

%post
dnf update -y && \
dnf remove -y vim-minimal python sqlite && \
dnf install -y boost boost-devel clang clang-analyzer clang-tools-extra cmake cppcheck eigen3-devel \
                   findutils gcc gcc-c++ git hdf5 hdf5-devel kernel-devel lcov \
                   make openmpi openmpi-devel tar tbb tbb-devel \
                   valgrind vim vtk vtk-devel wget && \
dnf clean all

git clone https://gitlab.onelab.info/gmsh/gmsh.git --depth 1
cd gmsh && mkdir build && cd build && cmake -DENABLE_BUILD_DYNAMIC=1 .. && make -j8 && make install

source /etc/profile.d/modules.sh && export MODULEPATH=$MODULEPATH:/usr/share/modulefiles && module load mpi/openmpi-x86_64

mkdir -p /research && cd /research 
git clone https://github.com/cb-geo/mpm.git
mkdir -p mpm/build
cd mpm/build 
export CXX_COMPILER=mpicxx
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=mpicxx -DCMAKE_EXPORT_COMPILE_COMMANDS=On ..
make -j8

%runscript
/research/mpm/build/mpm "$@"
```

## Collection

 - Name: [cb-geo/mpm-container](https://github.com/cb-geo/mpm-container)
 - License: None

