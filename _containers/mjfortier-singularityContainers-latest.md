---
id: 10207
name: "mjfortier/singularityContainers"
branch: "master"
tag: "latest"
commit: "6388cbdfccd0e922d68c9c50d06b5d914c98c079"
version: "fd95e92cf1294f8f82db4fe7cdf11a0b"
build_date: "2019-07-03T23:18:03.546Z"
size_mb: 1706
size: 501133343
sif: "https://datasets.datalad.org/shub/mjfortier/singularityContainers/latest/2019-07-03-6388cbdf-fd95e92c/fd95e92cf1294f8f82db4fe7cdf11a0b.simg"
url: https://datasets.datalad.org/shub/mjfortier/singularityContainers/latest/2019-07-03-6388cbdf-fd95e92c/
recipe: https://datasets.datalad.org/shub/mjfortier/singularityContainers/latest/2019-07-03-6388cbdf-fd95e92c/Singularity
collection: mjfortier/singularityContainers
---

# mjfortier/singularityContainers:latest

```bash
$ singularity pull shub://mjfortier/singularityContainers:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:latest

%labels
  CREATOR Matthew Fortier
  PURPOSE To provide containerization of CLASSIC functionality
  VERSION 0.1


%post
  apt update
  apt install vim make curl git libnetcdff-dev git zip unzip python3 gfortran netcdf-bin nano zlib1g mpich doxygen gedit python3 nco ncview libopenmpi-dev -y -f -m


  mkdir /temp && cd /temp
  curl -L --output cont.zip "https://github.com/mjfortier/singularityContainers/archive/master.zip"
  unzip cont.zip
  mkdir -p /para_netcdf_hdf-4.6.3
  cp -R singularityContainers-master/para_netcdf_hdf-4.6.3/* /para_netcdf_hdf-4.6.3/
  cd /para_netcdf_hdf-4.6.3/setup
  ./setup_netcdf.sh
  cd /para_netcdf_hdf-4.6.3
  ./dobuild.mpi
  cd /
  chmod 777 -R /para_netcdf_hdf-4.6.3

  mkdir -p /packages
  curl -o /packages/cdo-1.9.6.tar.gz "https://code.mpimet.mpg.de/attachments/download/19299/cdo-1.9.6.tar.gz"
  cd /packages
  tar -xzvf cdo-1.9.6.tar.gz cdo-1.9.6/
  rm cdo-1.9.6.tar.gz
  cd cdo-1.9.6
  ./configure
  make && make install




%runscript
  cd /packages
```

## Collection

 - Name: [mjfortier/singularityContainers](https://github.com/mjfortier/singularityContainers)
 - License: None

