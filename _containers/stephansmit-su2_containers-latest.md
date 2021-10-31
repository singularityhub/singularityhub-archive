---
id: 10573
name: "stephansmit/su2_containers"
branch: "master"
tag: "latest"
commit: "c4e2fbfaf6724a0c1c78278a78a88daccf2afc79"
version: "a3f902387ddfda1e639ca5bd723209d6"
build_date: "2019-08-12T11:38:47.911Z"
size_mb: 744.0
size: 283738143
sif: "https://datasets.datalad.org/shub/stephansmit/su2_containers/latest/2019-08-12-c4e2fbfa-a3f90238/a3f902387ddfda1e639ca5bd723209d6.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/stephansmit/su2_containers/latest/2019-08-12-c4e2fbfa-a3f90238/
recipe: https://datasets.datalad.org/shub/stephansmit/su2_containers/latest/2019-08-12-c4e2fbfa-a3f90238/Singularity
collection: stephansmit/su2_containers
---

# stephansmit/su2_containers:latest

```bash
$ singularity pull shub://stephansmit/su2_containers:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04
  
%post
    echo "Update apt-get"
    apt-get -y update

    echo "Install python3 and MPI"
    apt-get -y install python3 git build-essential autoconf python-dev libopenmpi-dev openmpi-common openmpi-bin

    echo "Install requirements for infiniband on surfsara"
    apt-get install -y dkms infiniband-diags libibverbs* ibacm librdmacm* libmlx4* libmlx5* mstflint libibcm.* libibmad.* libibumad* opensm srptools rdmacm-utils ibverbs-utils perftest vlan ibutils 

    echo "Clone the current master branch of SU2"
    git clone --depth=1 https://github.com/su2code/SU2

    echo "Install SU2"
    cd SU2
    autoreconf -i
    export CXXFLAGS="-O3"
    python3 preconfigure.py --enable-mpi --prefix=$PWD
    make install -j 7

    echo "Clean all the compiling objects"
    make clean
 
%runscript
     exec /SU2/bin/$1 $2
```

## Collection

 - Name: [stephansmit/su2_containers](https://github.com/stephansmit/su2_containers)
 - License: None

