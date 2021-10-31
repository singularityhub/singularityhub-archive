---
id: 11350
name: "willgpaik/r_aci"
branch: "master"
tag: "inla"
commit: "2fe88d76e3b39fdf4c1d92eb55c573262b60c94c"
version: "cc228d99f39f0e7f90d83e88f0b84d066bab32bbf306cf06af396cad769e2f9a"
build_date: "2019-11-04T15:55:49.292Z"
size_mb: 2506.0
size: 1545617408
sif: "https://datasets.datalad.org/shub/willgpaik/r_aci/inla/2019-11-04-2fe88d76-cc228d99/cc228d99f39f0e7f90d83e88f0b84d066bab32bbf306cf06af396cad769e2f9a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/r_aci/inla/2019-11-04-2fe88d76-cc228d99/
recipe: https://datasets.datalad.org/shub/willgpaik/r_aci/inla/2019-11-04-2fe88d76-cc228d99/Singularity
collection: willgpaik/r_aci
---

# willgpaik/r_aci:inla

```bash
$ singularity pull shub://willgpaik/r_aci:inla
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: willgpaik/r_aci:latest

%setup

%files

%environment
  source /opt/rh/devtoolset-8/enable
  export PATH=$PATH:/opt/sw/r/bin:/opt/sw/dep/bin
  export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/sw/dep/lib
  export CPATH=$CPATH:/opt/sw/include

%runscript

%post
  source /opt/rh/devtoolset-8/enable
  export PATH=$PATH:/opt/sw/r/bin
  
  yum -y install udunits2-devel proj-devel proj-epsg proj-nad
  yum -y update
  
  mkdir -p /opt/sw/dep
  
  cd /tmp
  
  # Install GDAL
  wget https://github.com/OSGeo/gdal/archive/v2.1.0.tar.gz
  tar -xf v2.1.0.tar.gz
  cd gdal-2.1.0/gdal
  ./configure --prefix=/opt/sw/dep
  make -j 2 && make install
  
  cd /tmp
  
  # Install GEOS
  wget http://download.osgeo.org/geos/geos-3.6.2.tar.bz2
  tar -xf geos-3.6.2.tar.bz2
  cd geos-3.6.2
  ./configure --prefix=/opt/sw/dep
  make -j 2 && make install
  
  cd /tmp
  rm -rf v2.1.0.tar.gz gdal-2.1.0 geos-3.6.2.tar.bz2 geos-3.6.2
  
  export PATH=$PATH:/opt/sw/dep/bin
  export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/sw/dep/lib
  export CPATH=$CPATH:/opt/sw/include
  
  R --vanilla -e "install.packages('sf', repos='http://lib.stat.cmu.edu/R/CRAN/')"
  R --vanilla -e "install.packages('INLA', repos=c(repo='http://lib.stat.cmu.edu/R/CRAN/', INLA='https://inla.r-inla-download.org/R/stable'), dep=TRUE)"
```

## Collection

 - Name: [willgpaik/r_aci](https://github.com/willgpaik/r_aci)
 - License: None

