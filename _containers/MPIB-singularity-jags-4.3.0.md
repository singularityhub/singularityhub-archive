---
id: 5233
name: "MPIB/singularity-jags"
branch: "master"
tag: "4.3.0"
commit: "028b096dff29865e50c0f495e13633922622ce61"
version: "40c581695b1421269a3a9faf3575dce7"
build_date: "2020-03-13T09:37:05.684Z"
size_mb: 569
size: 161103903
sif: "https://datasets.datalad.org/shub/MPIB/singularity-jags/4.3.0/2020-03-13-028b096d-40c58169/40c581695b1421269a3a9faf3575dce7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/MPIB/singularity-jags/4.3.0/2020-03-13-028b096d-40c58169/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-jags/4.3.0/2020-03-13-028b096d-40c58169/Singularity
collection: MPIB/singularity-jags
---

# MPIB/singularity-jags:4.3.0

```bash
$ singularity pull shub://MPIB/singularity-jags:4.3.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: debian:stable-slim

%help

Contains JAGS version 4.3.0

%post

apt-get update

# Packages needed inside the container.
export CONTAINER_SOFTWARE="gcc g++ gfortran make libcurl3-gnutls libopenblas-base"
## Set build variables.
# Packages needed only for the build process.
export BUILD_SOFTWARE="curl libblas-dev liblapack-dev"
# Needed for downloading source.
export JAGS_VERSION=4.3.0
export JAGS_BASE_URI="https://sourceforge.net/projects/mcmc-jags/files/JAGS/4.x/Source/"
export JAGS_FOLDER_NAME="JAGS-$JAGS_VERSION"
export JAGS_PACKAGE_NAME="${JAGS_FOLDER_NAME}.tar.gz"
# Set paths to facilitate the build process.
export BUILDHOME="/tmp"

# Install build and run requirements.
apt-get update
apt-get install $BUILD_SOFTWARE $CONTAINER_SOFTWARE -y

# Get JAGS source package
curl -L -o "$JAGS_PACKAGE_NAME" ${JAGS_BASE_URI}${JAGS_PACKAGE_NAME}"/download#"
tar -xf "$JAGS_PACKAGE_NAME"

# Build JAGS
cd "$JAGS_FOLDER_NAME"
./configure
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

# Can we call JAGS?
echo exit | jags
```

## Collection

 - Name: [MPIB/singularity-jags](https://github.com/MPIB/singularity-jags)
 - License: None

