---
id: 7128
name: "shiozaki/runscript"
branch: "master"
tag: "latest"
commit: "9b5795170a7a38d5c4ae6f6f943decc2101a4a00"
version: "110faebb83c8c369340434ac5be672e0"
build_date: "2019-02-14T08:45:05.003Z"
size_mb: 448
size: 167804959
sif: "https://datasets.datalad.org/shub/shiozaki/runscript/latest/2019-02-14-9b579517-110faebb/110faebb83c8c369340434ac5be672e0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/shiozaki/runscript/latest/2019-02-14-9b579517-110faebb/
recipe: https://datasets.datalad.org/shub/shiozaki/runscript/latest/2019-02-14-9b579517-110faebb/Singularity
collection: shiozaki/runscript
---

# shiozaki/runscript:latest

```bash
$ singularity pull shub://shiozaki/runscript:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%runscript
    /usr/bin/a.out

%environment
    export LD_LIBRARY_PATH=/usr/local/openmpi/lib:/usr/local/lib64:/usr/local/lib:/usr/local/boost/lib:/opt/intel/compilers_and_libraries_2019.2.187/linux/compiler/lib/intel64_lin:/opt/intel//compilers_and_libraries_2019.2.187/linux/mpi/intel64/libfabric/lib:/opt/intel//compilers_and_libraries_2019.2.187/linux/mpi/intel64/lib/release:/opt/intel//compilers_and_libraries_2019.2.187/linux/mpi/intel64/lib:/opt/intel/compilers_and_libraries_2019.2.187/linux/tbb/lib/intel64_lin/gcc4.7:/opt/intel/compilers_and_libraries_2019.2.187/linux/compiler/lib/intel64_lin:/opt/intel/compilers_and_libraries_2019.2.187/linux/mkl/lib/intel64_lin:/usr/local/lib:/usr/local/bagel/lib:$LD_LIBRARY_PATH
    export PATH=/usr/local/bagel/bin:$PATH
    export LD_LIBRARY_PATH=/usr/lib/libibverbs:$LD_LIBRARY_PATH

%labels
    AUTHOR shiozaki.toru@gmail.com

%post
    apt-get -y update
    apt-get -y install gcc
    apt-get -y install g++
    apt-get -y install wget
    apt-get -y install apt-transport-https

    # Taken from https://github.com/CHPC-UofU/Singularity-ubuntu-mpi
    # IB stuff, based on https://community.mellanox.com/docs/DOC-2431
    apt-get install -y dkms infiniband-diags libibverbs* ibacm librdmacm* libmlx4* libmlx5* mstflint libibcm.* libibmad.* libibumad* opensm srptools libmlx4-dev librdmacm-dev rdmacm-utils ibverbs-utils perftest vlan ibutils
    apt-get install -y libtool autoconf automake build-essential ibutils ibverbs-utils rdmacm-utils infiniband-diags perftest librdmacm-dev libibverbs-dev libmlx4-1 numactl libnuma-dev autoconf automake gcc g++ git libtool pkg-config
    apt-get install -y libnl-3-200 libnl-route-3-200 libnl-route-3-dev libnl-utils
    export LD_LIBRARY_PATH=/usr/lib/libibverbs:$LD_LIBRARY_PATH

    apt-get install -y libdapl-dev

    mkdir temp
    cd temp
    echo "Installing Intel MPI/MKL."
    wget https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
    apt-key add GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
    sh -c 'echo deb https://apt.repos.intel.com/mpi all main > /etc/apt/sources.list.d/intel-mpi.list'
    apt-get -y update
    apt-get -y install intel-mpi-2019.2-057
    echo "#include<iostream>\n #include \"mpi.h\"\n int main() { MPI_Init(0, 0); std::cout << \"hello world\" << std::endl; MPI_Finalize(); return 0; }" >> main.cc
    export LD_LIBRARY_PATH=/usr/local/openmpi/lib:/usr/local/lib64:/usr/local/lib:/usr/local/boost/lib:/opt/intel/compilers_and_libraries_2019.2.187/linux/compiler/lib/intel64_lin:/opt/intel//compilers_and_libraries_2019.2.187/linux/mpi/intel64/libfabric/lib:/opt/intel//compilers_and_libraries_2019.2.187/linux/mpi/intel64/lib/release:/opt/intel//compilers_and_libraries_2019.2.187/linux/mpi/intel64/lib:/opt/intel/compilers_and_libraries_2019.2.187/linux/tbb/lib/intel64_lin/gcc4.7:/opt/intel/compilers_and_libraries_2019.2.187/linux/compiler/lib/intel64_lin:/opt/intel/compilers_and_libraries_2019.2.187/linux/mkl/lib/intel64_lin:/usr/local/lib:/usr/local/bagel/lib:$LD_LIBRARY_PATH
    /opt/intel/impi/2019.2.187/intel64/bin/mpicxx -I/opt/intel/impi/2019.2.187/intel64/include main.cc
    cp a.out /usr/bin/
    cd ../
    rm -rf ./temp
    rm -rf /opt/intel
```

## Collection

 - Name: [shiozaki/runscript](https://github.com/shiozaki/runscript)
 - License: None

