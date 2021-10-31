---
id: 2129
name: "MPIB/singularity-r"
branch: "master"
tag: "3.4.4"
commit: "f78d0c24151ce07b84b9a489a2364efb0eacff52"
version: "098d74fa1a13970e2bf41e4a549e61f8"
build_date: "2018-08-23T18:25:58.018Z"
size_mb: 609
size: 206528543
sif: "https://datasets.datalad.org/shub/MPIB/singularity-r/3.4.4/2018-08-23-f78d0c24-098d74fa/098d74fa1a13970e2bf41e4a549e61f8.simg"
url: https://datasets.datalad.org/shub/MPIB/singularity-r/3.4.4/2018-08-23-f78d0c24-098d74fa/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-r/3.4.4/2018-08-23-f78d0c24-098d74fa/Singularity
collection: MPIB/singularity-r
---

# MPIB/singularity-r:3.4.4

```bash
$ singularity pull shub://MPIB/singularity-r:3.4.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: debian:9.3-slim
# Debian Stretch without manpages and other files
# usually not needed in containers.

%help

Contains R version 3.4.4.

%post

# Packages needed inside the container.
export CONTAINER_SOFTWARE="gfortran g++ gcc make libcurl3-gnutls"
## Set build variables.
# Packages needed only for the build process.
export BUILD_SOFTWARE="wget zlib1g-dev libbz2-dev liblzma-dev libpcre3-dev libcurl4-gnutls-dev"
# Needed for downloading source.
export R_BASE_URI="https://cran.r-project.org/src/base/R-3/"
export R_FOLDER_NAME="R-3.4.4"
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

