---
id: 3517
name: "outbackCrustacian/install_MPI_to_Vagrant"
branch: "master"
tag: "derived"
commit: "129d921c749080e5278e63ed69056c406ccb67f0"
version: "e37e50e5c6db121a522aa98275a8ca61"
build_date: "2018-07-13T21:19:59.938Z"
size_mb: 1085
size: 284086303
sif: "https://datasets.datalad.org/shub/outbackCrustacian/install_MPI_to_Vagrant/derived/2018-07-13-129d921c-e37e50e5/e37e50e5c6db121a522aa98275a8ca61.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/outbackCrustacian/install_MPI_to_Vagrant/derived/2018-07-13-129d921c-e37e50e5/
recipe: https://datasets.datalad.org/shub/outbackCrustacian/install_MPI_to_Vagrant/derived/2018-07-13-129d921c-e37e50e5/Singularity
collection: outbackCrustacian/install_MPI_to_Vagrant
---

# outbackCrustacian/install_MPI_to_Vagrant:derived

```bash
$ singularity pull shub://outbackCrustacian/install_MPI_to_Vagrant:derived
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_mpi_test_recipe:latest

%setup
   # make directory for test MPI program
   mkdir ${SINGULARITY_ROOTFS}/dmpi
   # cp pi.c ${SINGULARITY_ROOTFS}/dmpi/

%post
   yum install -y wget
   # add to local environment to build pi.c
   #export PATH=$PATH:/mpich/install/lib
   #export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich/install/lib
   env | sort
   cd /dmpi
   wget -q https://download.open-mpi.org/release/open-mpi/v3.1/openmpi-3.1.1.tar.gz
   tar xf openmpi-3.1.1.tar.gz --strip-components=1

   ./configure --prefix=/usr
   #CC=/mpich/install/bin/mpicc CXX=/mpich/install/bin/mpicxx --prefix=/usr
	make
	make install
```

## Collection

 - Name: [outbackCrustacian/install_MPI_to_Vagrant](https://github.com/outbackCrustacian/install_MPI_to_Vagrant)
 - License: None

