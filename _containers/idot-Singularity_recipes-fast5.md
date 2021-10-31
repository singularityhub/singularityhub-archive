---
id: 3766
name: "idot/Singularity_recipes"
branch: "master"
tag: "fast5"
commit: "a226658cf75f892b783a90b5b887413e1d1ef25d"
version: "37b7767fafdf7b3fe48f70970aadba2e"
build_date: "2018-07-31T11:15:57.513Z"
size_mb: 843
size: 402321439
sif: "https://datasets.datalad.org/shub/idot/Singularity_recipes/fast5/2018-07-31-a226658c-37b7767f/37b7767fafdf7b3fe48f70970aadba2e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/idot/Singularity_recipes/fast5/2018-07-31-a226658c-37b7767f/
recipe: https://datasets.datalad.org/shub/idot/Singularity_recipes/fast5/2018-07-31-a226658c-37b7767f/Singularity
collection: idot/Singularity_recipes
---

# idot/Singularity_recipes:fast5

```bash
$ singularity pull shub://idot/Singularity_recipes:fast5
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

 - Name: [idot/Singularity_recipes](https://github.com/idot/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

