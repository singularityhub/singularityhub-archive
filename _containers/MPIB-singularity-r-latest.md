---
id: 4167
name: "MPIB/singularity-r"
branch: "master"
tag: "latest"
commit: "2e70afd5e00bc72be7a17f51e8f2ed4495222070"
version: "47e7caff1dc9432655050c61fe8e2ef5"
build_date: "2019-04-29T20:57:13.941Z"
size_mb: 622
size: 206184479
sif: "https://datasets.datalad.org/shub/MPIB/singularity-r/latest/2019-04-29-2e70afd5-47e7caff/47e7caff1dc9432655050c61fe8e2ef5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/MPIB/singularity-r/latest/2019-04-29-2e70afd5-47e7caff/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-r/latest/2019-04-29-2e70afd5-47e7caff/Singularity
collection: MPIB/singularity-r
---

# MPIB/singularity-r:latest

```bash
$ singularity pull shub://MPIB/singularity-r:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: debian:9-slim
# Debian Stretch without manpages and other files
# usually not needed in containers.

%help

Contains R version 3.6.0

%post

# Packages needed inside the container.
export CONTAINER_SOFTWARE="gfortran g++ gcc make libcurl4-gnutls-dev"
## Set build variables.
# Packages needed only for the build process.
export BUILD_SOFTWARE="wget zlib1g-dev libbz2-dev liblzma-dev libpcre3-dev libcurl4-gnutls-dev"
# Needed for downloading source.
export R_BASE_URI="https://cran.r-project.org/src/base/R-3/"
export R_FOLDER_NAME="R-3.6.0"
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
./configure --with-readline=no --with-x=no --disable-java
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

