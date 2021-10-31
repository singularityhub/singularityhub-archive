---
id: 2046
name: "MPIB/singularity-mrtrix3"
branch: "master"
tag: "3.0_rc2"
commit: "05701f013cbd478ff2dd7f89d2896ef0f945c3fa"
version: "37537ab50680ac6bb4dc067cb03ec8b2"
build_date: "2020-03-13T09:36:15.443Z"
size_mb: 737
size: 246652959
sif: "https://datasets.datalad.org/shub/MPIB/singularity-mrtrix3/3.0_rc2/2020-03-13-05701f01-37537ab5/37537ab50680ac6bb4dc067cb03ec8b2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/MPIB/singularity-mrtrix3/3.0_rc2/2020-03-13-05701f01-37537ab5/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-mrtrix3/3.0_rc2/2020-03-13-05701f01-37537ab5/Singularity
collection: MPIB/singularity-mrtrix3
---

# MPIB/singularity-mrtrix3:3.0_rc2

```bash
$ singularity pull shub://MPIB/singularity-mrtrix3:3.0_rc2
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: debian:9.3-slim
# Debian Stretch without manpages and other files
# usually not needed in containers

%help
This image contains mrtrix3 version 3.0_RC2.
The mrtrix3 binaries are at /opt/mrtrix3/bin/

%post
export BUILD_SOFTWARE="git"
export CONTAINER_SOFTWARE="g++ python python-numpy libeigen3-dev zlib1g-dev libqt4-opengl-dev libgl1-mesa-dev libfftw3-dev libtiff5-dev qt4-default"
export CLONE_DIR=/opt
export MRTRIX_BUILD_DIR=${CLONE_DIR}/mrtrix3
export GITHUB_REPO="https://github.com/MRtrix3/mrtrix3.git"
export MRTRIX_VERSION="3.0_RC2"

apt-get update
apt-get install $BUILD_SOFTWARE $CONTAINER_SOFTWARE -y
cd $CLONE_DIR

git clone $GITHUB_REPO
cd $MRTRIX_BUILD_DIR
git checkout $MRTRIX_VERSION
python configure
python build

echo "export PATH=${MRTRIX_BUILD_DIR}/bin:$PATH" >> $SINGULARITY_ENVIRONMENT

# Cleanup
apt-get purge $BUILD_SOFTWARE -y
apt-get autoclean -y
apt-get autoremove -y
rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [MPIB/singularity-mrtrix3](https://github.com/MPIB/singularity-mrtrix3)
 - License: None

