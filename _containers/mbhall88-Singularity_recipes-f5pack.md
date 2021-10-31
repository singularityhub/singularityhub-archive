---
id: 5462
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "f5pack"
commit: "8df7771a981a19074c76bc57b1074f5381e3e8f8"
version: "321f7862e7c34167764c00dd32d417cc"
build_date: "2018-11-05T14:28:46.688Z"
size_mb: 839
size: 399806495
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/f5pack/2018-11-05-8df7771a-321f7862/321f7862e7c34167764c00dd32d417cc.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/f5pack/2018-11-05-8df7771a-321f7862/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/f5pack/2018-11-05-8df7771a-321f7862/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:f5pack

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:f5pack
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
  VERSION="0.6.5"
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
  RELEASE_URL=https://github.com/mateidavid/fast5/archive/v"$VERSION".tar.gz
  wget "$RELEASE_URL" -O - | tar xzf -
  cd fast5-"$VERSION"/python
  python setup.py install
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

