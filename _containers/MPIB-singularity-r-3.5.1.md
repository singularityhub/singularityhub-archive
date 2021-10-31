---
id: 4168
name: "MPIB/singularity-r"
branch: "master"
tag: "3.5.1"
commit: "3be364a8790741a5225ba0fcccaf5dcdc0c1cc8b"
version: "d93175fd15a970f7b06d9cf79906d900"
build_date: "2020-05-10T05:59:00.325Z"
size_mb: 630
size: 208642079
sif: "https://datasets.datalad.org/shub/MPIB/singularity-r/3.5.1/2020-05-10-3be364a8-d93175fd/d93175fd15a970f7b06d9cf79906d900.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/MPIB/singularity-r/3.5.1/2020-05-10-3be364a8-d93175fd/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-r/3.5.1/2020-05-10-3be364a8-d93175fd/Singularity
collection: MPIB/singularity-r
---

# MPIB/singularity-r:3.5.1

```bash
$ singularity pull shub://MPIB/singularity-r:3.5.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: debian:9.3-slim
# Debian Stretch without manpages and other files
# usually not needed in containers.

%help

Contains R version 3.5.1

%post

# Packages needed inside the container.
export CONTAINER_SOFTWARE="gfortran g++ gcc make libcurl3-gnutls"
## Set build variables.
# Packages needed only for the build process.
export BUILD_SOFTWARE="wget zlib1g-dev libbz2-dev liblzma-dev libpcre3-dev libcurl4-gnutls-dev"
# Needed for downloading source.
export R_BASE_URI="https://cran.r-project.org/src/base/R-3/"
export R_FOLDER_NAME="R-3.5.1"
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

