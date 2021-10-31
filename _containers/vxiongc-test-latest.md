---
id: 4049
name: "vxiongc/test"
branch: "master"
tag: "latest"
commit: "e320218ea69f2ba649a51ad7bdd42cea82a12158"
version: "247b38e95e2ced2af3a434445abf49ae"
build_date: "2018-08-17T19:45:46.296Z"
size_mb: 295
size: 86765599
sif: "https://datasets.datalad.org/shub/vxiongc/test/latest/2018-08-17-e320218e-247b38e9/247b38e95e2ced2af3a434445abf49ae.simg"
url: https://datasets.datalad.org/shub/vxiongc/test/latest/2018-08-17-e320218e-247b38e9/
recipe: https://datasets.datalad.org/shub/vxiongc/test/latest/2018-08-17-e320218e-247b38e9/Singularity
collection: vxiongc/test
---

# vxiongc/test:latest

```bash
$ singularity pull shub://vxiongc/test:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ISU-HPC/centos7-base

### Container help  ###
%help
Quick diag testsuite

### Create diag directories ###
%setup
mkdir -p ${SINGULARITY_ROOTFS}/diag
mkdir -p ${SINGULARITY_ROOTFS}/diag/bin
mkdir -p ${SINGULARITY_ROOTFS}/diag/lib

### Put diags in /diag/* ###
%files
dgemm /diag/bin
libiomp5.so /diag/lib

mpi_diag /diag/bin
libmpi.so.0 /diag/lib
libpciaccess.so.0 /diag/lib

### Dgemm app ###
%apprun dgemm
printf "Running Dgemm Test\n"
/diag/bin/dgemm

%appenv dgemm
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/diag/lib
#################

### MPI app ###
%apprun mpi
printf "Running MPI Test\n"
/diag/bin/mpi_diag

%appenv mpi
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/diag/lib
#################

### Default library path ##
%environment
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/diag/lib

%post

%check

### Run all diags ###
%runscript
printf "Running Dgemm Test\n"
/diag/bin/dgemm
printf "\nRunning MPI Test\n"
/diag/bin/mpi_diag

%labels
Maintainer vxiong
Version v0.01
```

## Collection

 - Name: [vxiongc/test](https://github.com/vxiongc/test)
 - License: None

