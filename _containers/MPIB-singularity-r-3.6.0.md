---
id: 8712
name: "MPIB/singularity-r"
branch: "master"
tag: "3.6.0"
commit: "53b54713e83d9db9fcf09bcb00a5fee10406715b"
version: "79f13aa3f9c14a772b3647065fada3f8"
build_date: "2019-04-29T20:57:13.949Z"
size_mb: 622
size: 206176287
sif: "https://datasets.datalad.org/shub/MPIB/singularity-r/3.6.0/2019-04-29-53b54713-79f13aa3/79f13aa3f9c14a772b3647065fada3f8.simg"
url: https://datasets.datalad.org/shub/MPIB/singularity-r/3.6.0/2019-04-29-53b54713-79f13aa3/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-r/3.6.0/2019-04-29-53b54713-79f13aa3/Singularity
collection: MPIB/singularity-r
---

# MPIB/singularity-r:3.6.0

```bash
$ singularity pull shub://MPIB/singularity-r:3.6.0
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

