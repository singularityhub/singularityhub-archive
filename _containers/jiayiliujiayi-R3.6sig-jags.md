---
id: 10168
name: "jiayiliujiayi/R3.6sig"
branch: "master"
tag: "jags"
commit: "23cbb9e6f45782cbca4171bf34e5e42ebeee51ba"
version: "31d5e1f98a8cb91aab899d6ec40a0015"
build_date: "2019-07-02T23:19:22.489Z"
size_mb: 569
size: 161132575
sif: "https://datasets.datalad.org/shub/jiayiliujiayi/R3.6sig/jags/2019-07-02-23cbb9e6-31d5e1f9/31d5e1f98a8cb91aab899d6ec40a0015.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jiayiliujiayi/R3.6sig/jags/2019-07-02-23cbb9e6-31d5e1f9/
recipe: https://datasets.datalad.org/shub/jiayiliujiayi/R3.6sig/jags/2019-07-02-23cbb9e6-31d5e1f9/Singularity
collection: jiayiliujiayi/R3.6sig
---

# jiayiliujiayi/R3.6sig:jags

```bash
$ singularity pull shub://jiayiliujiayi/R3.6sig:jags
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

 - Name: [jiayiliujiayi/R3.6sig](https://github.com/jiayiliujiayi/R3.6sig)
 - License: None

