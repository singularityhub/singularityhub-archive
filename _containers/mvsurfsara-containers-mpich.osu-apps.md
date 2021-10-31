---
id: 10042
name: "mvsurfsara/containers"
branch: "master"
tag: "mpich.osu-apps"
commit: "718abb804f51a3d9d542960b95590f6bbf91879a"
version: "544b6f7d2543aac00029225a6bc81800"
build_date: "2019-07-02T23:19:20.632Z"
size_mb: 997
size: 290877471
sif: "https://datasets.datalad.org/shub/mvsurfsara/containers/mpich.osu-apps/2019-07-02-718abb80-544b6f7d/544b6f7d2543aac00029225a6bc81800.simg"
url: https://datasets.datalad.org/shub/mvsurfsara/containers/mpich.osu-apps/2019-07-02-718abb80-544b6f7d/
recipe: https://datasets.datalad.org/shub/mvsurfsara/containers/mpich.osu-apps/2019-07-02-718abb80-544b6f7d/Singularity
collection: mvsurfsara/containers
---

# mvsurfsara/containers:mpich.osu-apps

```bash
$ singularity pull shub://mvsurfsara/containers:mpich.osu-apps
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest

%setup
   echo ${SINGULARITY_ROOTFS}
   mkdir ${SINGULARITY_ROOTFS}/container

%post
   yum update -y
   yum groupinstall -y "Development Tools"
   yum install -y gcc
   yum install -y gcc-c++
   yum install -y wget
   yum install -y git
   yum install -y ca-certificates

   yum groupinstall -y "Infiniband Support"
   yum install -y infiniband-diags
   yum install -y perftest
   yum install -y qperf
   yum install -y opensm

# Installing MPICH
   MPI_VERSION=3.2.1

   cd /container
   wget http://www.mpich.org/static/downloads/${MPI_VERSION}/mpich-${MPI_VERSION}.tar.gz
   tar xvf mpich-${MPI_VERSION}.tar.gz
   rm -f mpich-${MPI_VERSION}.tar.gz
   cd mpich-${MPI_VERSION}
   mkdir -p /container/mpi
   ./configure --prefix=/container/mpi
   make -j 4 install

# Installing OSU
   OSU_VERSION=5.6.1

   cd /container
   wget http://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-${OSU_VERSION}.tar.gz
   tar xvf osu-micro-benchmarks-${OSU_VERSION}.tar.gz
   rm -f osu-micro-benchmarks-${OSU_VERSION}.tar.gz
   cd osu-micro-benchmarks-${OSU_VERSION}
   ./configure --prefix=/container CC=/container/mpi/bin/mpicc CXX=/container/mpi/bin/mpicxx
   make
   make install

%apprun osu_allgather
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_allgather
%apprun osu_allgatherv
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_allgatherv
%apprun osu_allreduce
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_allreduce
%apprun osu_alltoall
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_alltoall
%apprun osu_alltoallv
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_alltoallv
%apprun osu_barrier
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_barrier
%apprun osu_bcast
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_bcast
%apprun osu_gather
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_gather
%apprun osu_gatherv
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_gatherv
%apprun osu_iallgather
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_iallgather
%apprun osu_iallgatherv
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_iallgatherv
%apprun osu_iallreduce
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_iallreduce
%apprun osu_ialltoall
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_ialltoall
%apprun osu_ialltoallv
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_ialltoallv
%apprun osu_ialltoallw
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_ialltoallw
%apprun osu_ibarrier
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_ibarrier
%apprun osu_ibcast
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_ibcast
%apprun osu_igather
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_igather
%apprun osu_igatherv
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_igatherv
%apprun osu_ireduce
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_ireduce
%apprun osu_iscatter
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_iscatter
%apprun osu_iscatterv
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_iscatterv
%apprun osu_reduce
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_reduce
%apprun osu_reduce_scatter
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_reduce_scatter
%apprun osu_scatter
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_scatter
%apprun osu_scatterv
   /container/libexec/osu-micro-benchmarks/mpi/collective/osu_scatterv
```

## Collection

 - Name: [mvsurfsara/containers](https://github.com/mvsurfsara/containers)
 - License: None

