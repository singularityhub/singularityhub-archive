---
id: 11245
name: "MetaboIGNITER/container-camera"
branch: "develop"
tag: "latest"
commit: "44f550dc08ae1304e353b23ad453d39ef90d93bf"
version: "ae922b4003ac70a96a0fdf7a6c97d79c"
build_date: "2020-03-13T11:00:42.427Z"
size_mb: 1582.0
size: 797700127
sif: "https://datasets.datalad.org/shub/MetaboIGNITER/container-camera/latest/2020-03-13-44f550dc-ae922b40/ae922b4003ac70a96a0fdf7a6c97d79c.sif"
url: https://datasets.datalad.org/shub/MetaboIGNITER/container-camera/latest/2020-03-13-44f550dc-ae922b40/
recipe: https://datasets.datalad.org/shub/MetaboIGNITER/container-camera/latest/2020-03-13-44f550dc-ae922b40/Singularity
collection: MetaboIGNITER/container-camera
---

# MetaboIGNITER/container-camera:latest

```bash
$ singularity pull shub://MetaboIGNITER/container-camera:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: metaboigniter/container-xcms:v1.53.1
%files
scripts/*.r /usr/local/bin/
runTest1.sh /usr/local/bin/runTest1.sh
%labels
MAINTAINER PhenoMeNal-H2020 Project (phenomenal-h2020-users@googlegroups.com)
software="CAMERA"
software.version="1.33.4"
version="0.12"
description="CAMERA: Collection of annotation related methods for mass spectrometry data."
website="https://github.com/sneumann/CAMERA"
documentation="https://github.com/phnmnl/container-camera/blob/master/README.md"
license="https://github.com/phnmnl/container-camera/blob/develop/License.txt"
tags="Metabolomics"
%post


# Install packages for compilation
# R -e 'source("https://bioconductor.org/biocLite.R"); biocLite("CAMERA")' && \
apt-get -y update && apt-get -y --no-install-recommends install make gcc gfortran g++ libnetcdf-dev libxml2-dev libblas-dev liblapack-dev libssl-dev r-base-dev pkg-config git && \
R -e 'source("https://bioconductor.org/biocLite.R");biocLite(c("irlba","igraph","XML","intervals","devtools"))' && \
R -e 'library(devtools); install_github(repo="sneumann/CAMERA", ref="cbc9cdb2eba6438434c27fec5fa13c9e6fdda785")' && \
apt-get -y --purge --auto-remove remove make gcc gfortran g++ libblas-dev liblapack-dev r-base-dev libssl-dev pkg-config && \
apt-get -y clean && apt-get -y autoremove && rm -rf /var/lib/{cache,log}/ /tmp/* /var/tmp/*

# Install zip package
apt-get -y update && apt-get -y --no-install-recommends install make gcc gfortran g++ && \
R -e 'source("https://bioconductor.org/biocLite.R");biocLite(c("zip"))'

# Add scripts folder to container
# Add files for testing

chmod +x /usr/local/bin/*.r
chmod +x /usr/local/bin/runTest1.sh

%runscript
exec /bin/bash "$@"
%startscript
exec /bin/bash "$@"
```

## Collection

 - Name: [MetaboIGNITER/container-camera](https://github.com/MetaboIGNITER/container-camera)
 - License: [MIT License](https://api.github.com/licenses/mit)

