---
id: 3401
name: "mikemhenry/cme-lab-images"
branch: "master"
tag: "hoomd"
commit: "c8af97dff5c8a02387f3884601ec832eb2044883"
version: "1a05ae007bd07ec517a743fa721433be"
build_date: "2018-07-05T15:14:04.837Z"
size_mb: 2578
size: 1432645663
sif: "https://datasets.datalad.org/shub/mikemhenry/cme-lab-images/hoomd/2018-07-05-c8af97df-1a05ae00/1a05ae007bd07ec517a743fa721433be.simg"
url: https://datasets.datalad.org/shub/mikemhenry/cme-lab-images/hoomd/2018-07-05-c8af97df-1a05ae00/
recipe: https://datasets.datalad.org/shub/mikemhenry/cme-lab-images/hoomd/2018-07-05-c8af97df-1a05ae00/Singularity
collection: mikemhenry/cme-lab-images
---

# mikemhenry/cme-lab-images:hoomd

```bash
$ singularity pull shub://mikemhenry/cme-lab-images:hoomd
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: shub://singularity-hub.org/mikemhenry/cme-lab-images:cuda80
#Bootstrap: localimage
#From: cuda80.simg 
%help
Base HOOMD image used in CME-Lab workflows.

http://coen.boisestate.edu/cmelab/

%setup

%files

%labels
  Maintainer Mike Henry
  Maintaine_rEmail mikehenry@boisestate.edu
  Version v0.01

%environment
  export SOFTWARE_ROOT=/opt/hoomd
  export PYTHONPATH=$PYTHONPATH:${SOFTWARE_ROOT}/lib/python

%post

#### hoomd
  export HOOMD_TAG=v2.3.2
  # Need to figure out how to export envars from other layers
  CONDA_DIR="/opt/conda"
  PATH="$CONDA_DIR/bin:$PATH"
  # Hoomd system deps
  apt-get update && apt-get install -y --no-install-recommends git cmake
 
  
  # Hoomd python deps
  pip install numpy~=1.14

  # Hoomd
  export SOFTWARE_ROOT=/opt/hoomd
  git clone --recursive https://bitbucket.org/glotzer/hoomd-blue
  cd hoomd-blue
  git checkout  $HOOMD_TAG
  mkdir build
  cd build
  export CXX="$(command -v g++)"
  export CC="$(command -v gcc)"
  cmake ../ -DCMAKE_INSTALL_PREFIX=${SOFTWARE_ROOT}/lib/python \
            -DENABLE_CUDA=ON \
            -DDISABLE_SQLITE=ON \
            -DSINGLE_PRECISION=ON
  make -j3
  make install

%runscript



%test
```

## Collection

 - Name: [mikemhenry/cme-lab-images](https://github.com/mikemhenry/cme-lab-images)
 - License: None

