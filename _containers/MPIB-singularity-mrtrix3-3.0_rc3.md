---
id: 3152
name: "MPIB/singularity-mrtrix3"
branch: "master"
tag: "3.0_rc3"
commit: "faddf33e65b5151915c6e346062bf96cae5af92f"
version: "0b80755da1d6e93e27c504b1e5c4c81a"
build_date: "2021-01-01T14:07:23.788Z"
size_mb: 741
size: 248102943
sif: "https://datasets.datalad.org/shub/MPIB/singularity-mrtrix3/3.0_rc3/2021-01-01-faddf33e-0b80755d/0b80755da1d6e93e27c504b1e5c4c81a.simg"
url: https://datasets.datalad.org/shub/MPIB/singularity-mrtrix3/3.0_rc3/2021-01-01-faddf33e-0b80755d/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-mrtrix3/3.0_rc3/2021-01-01-faddf33e-0b80755d/Singularity
collection: MPIB/singularity-mrtrix3
---

# MPIB/singularity-mrtrix3:3.0_rc3

```bash
$ singularity pull shub://MPIB/singularity-mrtrix3:3.0_rc3
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: debian:9.3-slim
# Debian Stretch without manpages and other files
# usually not needed in containers

%help
This image contains mrtrix3 version 3.0_RC3.
The mrtrix3 binaries are at /opt/mrtrix3/bin/

%post
export BUILD_SOFTWARE="git"
export CONTAINER_SOFTWARE="g++ python python-numpy libeigen3-dev zlib1g-dev libqt4-opengl-dev libgl1-mesa-dev libfftw3-dev libtiff5-dev qt4-default"
export CLONE_DIR=/opt
export MRTRIX_BUILD_DIR=${CLONE_DIR}/mrtrix3
export GITHUB_REPO="https://github.com/MRtrix3/mrtrix3.git"
export MRTRIX_VERSION="3.0_RC3"

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

