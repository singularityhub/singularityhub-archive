---
id: 581
name: "igory1999/openmpi_3.0.0"
branch: "master"
tag: "latest"
commit: "729ee58da7f24643e7dad2f8c46528aa1233c701"
version: "92a4c1f161566694300d78c034c2804c"
build_date: "2017-10-29T15:13:28.369Z"
size_mb: 1154
size: 353554463
sif: "https://datasets.datalad.org/shub/igory1999/openmpi_3.0.0/latest/2017-10-29-729ee58d-92a4c1f1/92a4c1f161566694300d78c034c2804c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/igory1999/openmpi_3.0.0/latest/2017-10-29-729ee58d-92a4c1f1/
recipe: https://datasets.datalad.org/shub/igory1999/openmpi_3.0.0/latest/2017-10-29-729ee58d-92a4c1f1/Singularity
collection: igory1999/openmpi_3.0.0
---

# igory1999/openmpi_3.0.0:latest

```bash
$ singularity pull shub://igory1999/openmpi_3.0.0:latest
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://ftp2.scientificlinux.org/linux/scientific/7x/x86_64/os
Include: yum

%runscript
    exec echo "module load openmpi/3.0.0"
%labels
   AUTHOR ivy2@uchicago.edu
%post
   yum -y update
   yum -y install wget emacs vi make automake autoconf gcc gcc-c++ which python perl gcc-gfortran
   wget https://www.open-mpi.org/software/ompi/v3.0/downloads/openmpi-3.0.0.tar.gz
   tar xvf openmpi-3.0.0.tar.gz
   cd openmpi-3.0.0
   ./configure --enable-mpi-cxx --enable-mpi-fortran --enable-mpi-cxx-seek
   make
   make install
```

## Collection

 - Name: [igory1999/openmpi_3.0.0](https://github.com/igory1999/openmpi_3.0.0)
 - License: None

