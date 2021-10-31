---
id: 2265
name: "phgenomics-singularity/stacks"
branch: "master"
tag: "latest"
commit: "ed0b74dd5edf1ad0b8dbc5a297d7ad14f3ccc36e"
version: "5cade36e8b887776482ab8b20263155f"
build_date: "2020-09-24T18:33:55.869Z"
size_mb: 876
size: 230219807
sif: "https://datasets.datalad.org/shub/phgenomics-singularity/stacks/latest/2020-09-24-ed0b74dd-5cade36e/5cade36e8b887776482ab8b20263155f.simg"
url: https://datasets.datalad.org/shub/phgenomics-singularity/stacks/latest/2020-09-24-ed0b74dd-5cade36e/
recipe: https://datasets.datalad.org/shub/phgenomics-singularity/stacks/latest/2020-09-24-ed0b74dd-5cade36e/Singularity
collection: phgenomics-singularity/stacks
---

# phgenomics-singularity/stacks:latest

```bash
$ singularity pull shub://phgenomics-singularity/stacks:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:trusty-20170817

%help
A Singularity image for Stacks v2.0b

%labels
Maintainer Anders Goncalves da Silva
Build 1.0
Stacks v2.0b (with SparseHash)

%post

  STACKS_VERSION=2.0b

  sudo locale-gen en_US.UTF-8
  sudo update-locale

  sudo apt-get --yes update
  sudo apt-get --yes install build-essential autoconf automake wget git zlib1g-dev libbz2-dev libncurses5-dev curl unzip
  sudo apt-get --yes install libdbd-mysql-perl

  sudo apt-get --yes install software-properties-common
  sudo add-apt-repository --yes ppa:ubuntu-toolchain-r/test
  sudo apt-get --yes update
  sudo apt-get --yes install g++-4.9

  cd /tmp

  echo "Installing Stacks"

  STACKS_URL="http://catchenlab.life.illinois.edu/stacks/source/stacks-${STACKS_VERSION}.tar.gz"
  STACKS_ZIP=stacks.tar.gz
  wget -O ${STACKS_ZIP} "${STACKS_URL}"
  tar xf ${STACKS_ZIP}
  cd stacks-${STACKS_VERSION}
  CC=gcc-4.9 CXX=g++-4.9 ./configure --enable-sparsehash
  make -j4
  sudo make install
  sudo mkdir /tests
  sudo mv tests/* /tests

  echo "Sorting some env variables..."
  sudo echo 'LANGUAGE="en_US:en"' >> $SINGULARITY_ENVIRONMENT
  sudo echo 'LC_ALL="en_US.UTF-8"' >> $SINGULARITY_ENVIRONMENT
  sudo echo 'LC_CTYPE="UTF-8"' >> $SINGULARITY_ENVIRONMENT
  sudo echo 'LANG="en_US.UTF-8"' >>  $SINGULARITY_ENVIRONMENT

  echo "Done"

%runscript
  echo "Welcome to STACKS 2.0b" >&2
  exec "$@"

%test
  echo "Testing STACKS"
  # gstacks --version
  # populations --version
  # for testfile in $(ls /tests/*.t);
  # do
  #   bash ${testfile};
  # done
```

## Collection

 - Name: [phgenomics-singularity/stacks](https://github.com/phgenomics-singularity/stacks)
 - License: None

