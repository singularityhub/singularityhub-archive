---
id: 5105
name: "marcc-hpc/cdo"
branch: "master"
tag: "latest"
commit: "da61ef06f843d2a5dbc9d00d88b5eeafcf4f1c9f"
version: "2f90055c474047f2b671c6978bf342ce"
build_date: "2020-05-06T02:34:20.579Z"
size_mb: 3633
size: 811122719
sif: "https://datasets.datalad.org/shub/marcc-hpc/cdo/latest/2020-05-06-da61ef06-2f90055c/2f90055c474047f2b671c6978bf342ce.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/marcc-hpc/cdo/latest/2020-05-06-da61ef06-2f90055c/
recipe: https://datasets.datalad.org/shub/marcc-hpc/cdo/latest/2020-05-06-da61ef06-2f90055c/Singularity
collection: marcc-hpc/cdo
---

# marcc-hpc/cdo:latest

```bash
$ singularity pull shub://marcc-hpc/cdo:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest

%environment
# use bash as default shell
SHELL=/bin/bash
export SHELL
LD_LIBRARY_PATH="/usr/local/lib:$LD_LIBRARY_PATH"
export LD_LIBRARY_PATH

%setup
# runs on host - the path to the image is $SINGULARITY_ROOTFS

%post

# post-setup script
yum -y install wget which # i like to download and know where things are
yum -y install vim libjpeg-turbo-devel mesa-libGL-devel freeglut-devel
yum -y groupinstall "Development Tools" # standard set
yum -y install epel-release
yum -y install netcdf-devel cmake3
yum -y install ncview
yum -y install fftw3-devel
yum -y install libxml2-devel
yum -y install boost-devel
yum -y install cairo-devel pango-devel
yum -y install python-jinja2

# 
# 5 components: cdo, jasper, eccodes, proj4, and magics
wget https://code.mpimet.mpg.de/attachments/download/18264/cdo-1.9.5.tar.gz
wget http://www.ece.uvic.ca/~frodo/jasper/software/jasper-2.0.14.tar.gz
wget https://confluence.ecmwf.int/download/attachments/45757960/eccodes-2.9.0-Source.tar.gz
wget http://download.osgeo.org/proj/proj-5.2.0.tar.gz
wget https://confluence.ecmwf.int/download/attachments/3473464/Magics-3.2.0-Source.tar.gz

# 
# extract
tar xf cdo-1.9.5.tar.gz
tar xf jasper-2.0.14.tar.gz
tar xf eccodes-2.9.0-Source.tar.gz
tar xf proj-5.2.0.tar.gz
tar xf Magics-3.2.0-Source.tar.gz

# build jasper
cd jasper-2.0.14
mkdir -p build;  cd build
cmake3 -G "Unix Makefiles" ..
make && make install
cd ../..

# build ecccodes 
cd eccodes-2.9.0-Source
mkdir -p build ; cd build
cmake3 ../
make ; # ctest3
make install
cd ../..

# build proj4 for magics
cd proj-5.2.0
./configure
make && make install
cd ../..

# build magics
cd Magics-3.2.0-Source
mkdir -p build ; cd build
cmake3 ../
make ; # ctest3
make install
cd ../..

# 
cd cdo-1.9.5
ln -s /usr/local/include/magics/magics_api.h /usr/include/magics_api.h
ln -s /usr/local/include/magics/magics_config.h /usr/include/magics_config.h
ln -s /usr/local/include/magics/magics.h /usr/include/magics.h
CXXFLAGS=-fopenmp ./configure --with-netcdf --with-eccodes --with-fftw3 --with-magics --with-xml2
make && make install
```

## Collection

 - Name: [marcc-hpc/cdo](https://github.com/marcc-hpc/cdo)
 - License: None

