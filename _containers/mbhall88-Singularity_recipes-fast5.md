---
id: 2328
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "fast5"
commit: "3e798dfd6fcd56aa9957b0cd6c512f7039d87cef"
version: "161cf10a9eaeca33e78b6fb75548ce70"
build_date: "2020-05-15T06:50:45.744Z"
size_mb: 844
size: 403726367
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/fast5/2020-05-15-3e798dfd-161cf10a/161cf10a9eaeca33e78b6fb75548ce70.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mbhall88/Singularity_recipes/fast5/2020-05-15-3e798dfd-161cf10a/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/fast5/2020-05-15-3e798dfd-161cf10a/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:fast5

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:fast5
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: xenial
MirrorURL:  http://us.archive.ubuntu.com/ubuntu/

%environment
  PATH=/usr/local/bin:$PATH

%post
  apt-get update
  apt-get install -y software-properties-common wget
  apt-add-repository universe
  apt-get update

  # ================================
  # INSTALL FAST5 LIBRARY
  # ================================
  FAST5_VERSION=0.6.5
  apt-get install -y build-essential libhdf5-dev libpython2.7-dev \
    python2.7-minimal python-pip

  # install python dependencies for fast5 lib
  wget https://bootstrap.pypa.io/get-pip.py -O - | \
    python - && \
    pip install cython setuptools virtualenv

  # expose prerequisites settings and make available at runtime
  export HDF5_INCLUDE_DIR=/usr/include/hdf5/serial/
  export HDF5_LIB_DIR=/usr/lib/x86_64-linux-gnu/hdf5/serial/
  echo 'export HDF5_INCLUDE_DIR=/usr/include/hdf5/serial/' >> $SINGULARITY_ENVIRONMENT
  echo 'export HDF5_LIB_DIR=/usr/lib/x86_64-linux-gnu/hdf5/serial/' >> $SINGULARITY_ENVIRONMENT

  # download and install version release from GitHub
  RELEASE_URL=https://github.com/mateidavid/fast5/archive/v${FAST5_VERSION}.tar.gz
  wget "$RELEASE_URL" -O - | tar xzf -
  cd fast5-${FAST5_VERSION}/python
  python setup.py install
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

