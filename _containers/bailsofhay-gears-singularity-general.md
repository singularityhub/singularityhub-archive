---
id: 1246
name: "bailsofhay/gears-singularity"
branch: "master"
tag: "general"
commit: "65f4ce9f2e276ee6cc11ef503fa639b175cfdccf"
version: "1a477d8464e63eaba5359e2213faf82e"
build_date: "2018-01-10T06:32:44.540Z"
size_mb: 2060
size: 649392159
sif: "https://datasets.datalad.org/shub/bailsofhay/gears-singularity/general/2018-01-10-65f4ce9f-1a477d84/1a477d8464e63eaba5359e2213faf82e.simg"
url: https://datasets.datalad.org/shub/bailsofhay/gears-singularity/general/2018-01-10-65f4ce9f-1a477d84/
recipe: https://datasets.datalad.org/shub/bailsofhay/gears-singularity/general/2018-01-10-65f4ce9f-1a477d84/Singularity
collection: bailsofhay/gears-singularity
---

# bailsofhay/gears-singularity:general

```bash
$ singularity pull shub://bailsofhay/gears-singularity:general
```

## Singularity Recipe

```singularity
BootStrap: debootstrap 
OSVersion: xenial 
MirrorURL: http://archive.ubuntu.com/ubuntu/ 
Include: bash

# First working attempt.  Build with:
%post
  locale-gen en_US.UTF-8
  sed -i 's/main/main restricted universe/g' /etc/apt/sources.list
  echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a /etc/apt/sources.list
  gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
  gpg -a --export E084DAB9 | apt-key add -
  apt-get update
 
 # Install R, openmpi, misc. utilities:
  apt-get install -y libopenblas-dev r-base-core r-base-dev libcurl4-openssl-dev libopenmpi-dev openmpi-bin openmpi-common openmpi-doc openssh-client openssh-server libssh-dev wget vim git nano git cmake gfortran g++ curl wget python autoconf bzip2 libtool libtool-bin libxml2-dev

  # GDAL et al.: 
  apt-get install -y libgdal-dev libproj-dev 

  #GRASS GIS:
  apt-get install -y software-properties-common python-software-properties
  add-apt-repository ppa:ubuntugis/ppa
  apt-get update
  apt-get install -y grass libgdal-dev libproj-dev gdal-bin python-gdal python3-gdal
  
  # Miscellaneous other installs
  apt-get install -y libudunits2-dev
  
  apt-get clean
  
  # Install required R packages
  R --slave -e 'install.packages(c("doMPI","XML","raster","rgdal","rgeos","RStoolbox","devtools","sf"), repos="https://cloud.r-project.org/")'
  
  # Install latest GDALUtils:
  R --slave -e 'install.packages(c("gdalUtils"), repos="http://R-Forge.R-project.org")'
  R --slave -e 'install.packages(c("spatial.tools"), repos="http://R-Forge.R-project.org")'
```

## Collection

 - Name: [bailsofhay/gears-singularity](https://github.com/bailsofhay/gears-singularity)
 - License: None

