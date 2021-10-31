---
id: 1779
name: "MPIB/singularity-r"
branch: "master"
tag: "2.15.3"
commit: "f78d0c24151ce07b84b9a489a2364efb0eacff52"
version: "a989dacb0465ea14e3e29628c18b7348"
build_date: "2018-08-23T18:25:58.004Z"
size_mb: 579
size: 189870111
sif: "https://datasets.datalad.org/shub/MPIB/singularity-r/2.15.3/2018-08-23-f78d0c24-a989dacb/a989dacb0465ea14e3e29628c18b7348.simg"
url: https://datasets.datalad.org/shub/MPIB/singularity-r/2.15.3/2018-08-23-f78d0c24-a989dacb/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-r/2.15.3/2018-08-23-f78d0c24-a989dacb/Singularity
collection: MPIB/singularity-r
---

# MPIB/singularity-r:2.15.3

```bash
$ singularity pull shub://MPIB/singularity-r:2.15.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: debian:9.3-slim
# Debian Stretch without manpages and other files
# usually not needed in containers.

%help

Contains R version 2.15.3.

%post

# Packages needed inside the container.
export CONTAINER_SOFTWARE="gfortran g++ gcc make libcurl3-gnutls"
## Set build variables.
# Packages needed only for the build process.
export BUILD_SOFTWARE="wget libcurl4-gnutls-dev"
# Needed for downloading source.
export R_BASE_URI="https://cran.r-project.org/src/base/R-2/"
export R_FOLDER_NAME="R-2.15.3"
export R_PACKAGE_NAME="${R_FOLDER_NAME}.tar.gz"
# Set paths to facilitate the build process.
export BUILDHOME="/tmp"

# Install build and run requirements.
apt-get update
apt-get install $BUILD_SOFTWARE $CONTAINER_SOFTWARE -y

# Get R Package
wget ${R_BASE_URI}${R_PACKAGE_NAME}
tar -xf $R_PACKAGE_NAME

# Build R
cd $R_FOLDER_NAME
./configure --with-readline=no --with-x=no
make
make install

# Removing installation overhead.
 
cd
rm -rf /tmp/*
apt-get purge $BUILD_SOFTWARE -y
apt-get autoclean -y
apt-get autoremove -y
rm -rf /var/lib/apt/lists/*

%test

# Can we call R?
R --version
```

## Collection

 - Name: [MPIB/singularity-r](https://github.com/MPIB/singularity-r)
 - License: None

