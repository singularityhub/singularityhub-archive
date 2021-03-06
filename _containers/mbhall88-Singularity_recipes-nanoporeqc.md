---
id: 1951
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "nanoporeqc"
commit: "985a10c7fdaf88e538c1ac99fe6fa01c8c0a9814"
version: "e310be8fd3b50d5c0c130f8799f8a0ad"
build_date: "2020-05-15T06:42:25.398Z"
size_mb: 1605
size: 617533471
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/nanoporeqc/2020-05-15-985a10c7-e310be8f/e310be8fd3b50d5c0c130f8799f8a0ad.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mbhall88/Singularity_recipes/nanoporeqc/2020-05-15-985a10c7-e310be8f/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/nanoporeqc/2020-05-15-985a10c7-e310be8f/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:nanoporeqc

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:nanoporeqc
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: xenial
MirrorURL:  http://us.archive.ubuntu.com/ubuntu/

%help
  A container to hold quality control tools and their dependencies for analysing
  nanopore data.
  Run `singularity exec nanoporeqc.simg` followed by any of the following:
    - pistis
    - porechop
    - filtlong
    - minimap2
    - samtools
    - NanoLyse
    - NanoStat
    - centrifuge

%environment
  PATH=/usr/local/bin:$PATH

%post
  # ================================
  # INSTALL core dependencies
  # ================================
  apt-get update
  apt-get install -y software-properties-common wget
  apt-add-repository universe
  apt-get update
  apt-get install -y build-essential manpages-dev make zlib1g-dev checkinstall libssl-dev libbz2-dev 
  export LC_ALL=C.UTF-8
  export LANG=C.UTF-8
  echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
  echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT

  # ================================
  # INSTALL python 3.6
  # ================================
  PY_VERSION=3.6.4
  PY_URL=https://www.python.org/ftp/python/${PY_VERSION}/Python-${PY_VERSION}.tgz
  cd /opt
  wget "$PY_URL" -O - | tar -xzf -
  cd Python-${PY_VERSION}
  ./configure
  make
  make install
  cd ~

  # ================================
  # INSTALL latest pistis release (v0.3.3)
  # ================================
  pip3 install pistis

  # ================================
  # INSTALL porechop
  # ================================
  PORECHOP_VERSION=0.2.4
  PORECHOP_URL=https://github.com/rrwick/Porechop/archive/v${PORECHOP_VERSION}.tar.gz
  apt-get install python3-setuptools python3-pkg-resources
  wget "$PORECHOP_URL"
  tar xzf v${PORECHOP_VERSION}.tar.gz
  rm v${PORECHOP_VERSION}.tar.gz
  cd Porechop-${PORECHOP_VERSION}
  python3 setup.py install
  cd ~

  # ================================
  # INSTALL filtlong
  # ================================
  FILTLONG_VERSION=0.2.0
  FILTLONG_URL=https://github.com/rrwick/Filtlong/archive/v${FILTLONG_VERSION}.tar.gz
  wget "$FILTLONG_URL"
  tar xzf v${FILTLONG_VERSION}.tar.gz
  rm v${FILTLONG_VERSION}.tar.gz
  cd Filtlong-${FILTLONG_VERSION}
  make -j
  cp bin/filtlong /usr/local/bin
  cd ~

  # ================================
  # INSTALL minimap2
  # ================================
  MM2_VERSION=2.12
  MM2_URL=https://github.com/lh3/minimap2/releases/download/v${MM2_VERSION}/minimap2-${MM2_VERSION}_x64-linux.tar.bz2
  wget "$MM2_URL" -O - | tar -jxvf -
  cp ./minimap2-${MM2_VERSION}_x64-linux/minimap2 /usr/local/bin

  # ================================
  # INSTALL samtools
  # ================================
  SAMTOOLS_VERSION=1.7
  SAMTOOLS_URL=https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2
  apt-get install -y libncurses5-dev libbz2-dev liblzma-dev
  wget "$SAMTOOLS_URL" -O - | tar -jxvf -
  cd samtools-${SAMTOOLS_VERSION}
  ./configure
  make
  make install
  cd ~

  # ================================
  # INSTALL nanolyse
  # ================================
  pip3 install NanoLyse

  # ================================
  # INSTALL nanostats
  # ================================
  pip3 install nanostat

  # ================================
  # INSTALL centrifuge
  # ================================
  apt-get install -y git
  # use their github repository as the releases dont seem to be very up to date at the moment
  git clone https://github.com/infphilo/centrifuge
  cd centrifuge
  # go to version 1.0.3-beta
  git reset --hard 95178872de36bc10ce83b55397417050eac52e65
  make
  make install prefix=/usr/local
  cd ~
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

