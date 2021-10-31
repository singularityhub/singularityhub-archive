---
id: 2076
name: "JiaweiZhuang/Singularity_GC"
branch: "master"
tag: "latest"
commit: "d1fc7eef6b669841321950eea52f52a79fd707f5"
version: "1efd16323f148de3e3bfd007f0e9454b"
build_date: "2021-02-24T22:23:04.321Z"
size_mb: 541
size: 206532639
sif: "https://datasets.datalad.org/shub/JiaweiZhuang/Singularity_GC/latest/2021-02-24-d1fc7eef-1efd1632/1efd16323f148de3e3bfd007f0e9454b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/JiaweiZhuang/Singularity_GC/latest/2021-02-24-d1fc7eef-1efd1632/
recipe: https://datasets.datalad.org/shub/JiaweiZhuang/Singularity_GC/latest/2021-02-24-d1fc7eef-1efd1632/Singularity
collection: JiaweiZhuang/Singularity_GC
---

# JiaweiZhuang/Singularity_GC:latest

```bash
$ singularity pull shub://JiaweiZhuang/Singularity_GC:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%post
    apt-get update
    apt-get install -y git vim bc gcc gfortran libnetcdf-dev libnetcdff-dev netcdf-bin

%environment
    export NETCDF_HOME=/usr
    export NETCDF_FORTRAN_HOME=/usr

    export FC=gfortran
    export CC=gcc
    export CXX=g++

    # Tell GEOS-Chem where to find netCDF library files
    export GC_BIN=$NETCDF_HOME/bin
    export GC_INCLUDE=$NETCDF_HOME/include
    export GC_LIB=$NETCDF_HOME/lib

    # NOTE: If netCDF-Fortran was loaded as a separate module, then
    # also define these variables.  (Otherwise comment these out.)
    export GC_F_BIN=$NETCDF_FORTRAN_HOME/bin
    export GC_F_INCLUDE=$NETCDF_FORTRAN_HOME/include
    export GC_F_LIB=$NETCDF_FORTRAN_HOME/lib

    # Max out the stack memory for OpenMP
    # http://wiki.seas.harvard.edu/geos-chem/index.php/GNU_Fortran_compiler#Requesting_sufficient_stack_memory_for_GEOS-Chem
    # ulimit -s unlimited # do we need this inside container?
    export OMP_STACKSIZE=500m

    # fix Singularity + Perl error
    # https://groups.google.com/a/lbl.gov/forum/#!msg/singularity/58Xr72oDfBg/m3Y7Nr_PBAAJ
    export LANG=C

    # add color for interactive mode
    alias ls='ls --color=auto'

%runscript
    echo "Container for GEOS-Chem environment"
    echo "Please use 'singularity shell container_name' to run it interactively."
```

## Collection

 - Name: [JiaweiZhuang/Singularity_GC](https://github.com/JiaweiZhuang/Singularity_GC)
 - License: None

