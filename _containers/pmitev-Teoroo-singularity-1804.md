---
id: 9055
name: "pmitev/Teoroo-singularity"
branch: "master"
tag: "1804"
commit: "421c7122194ed9b4d85e23d4006bcbac903158a2"
version: "0959ee852dba5de22eb031a9ed753285"
build_date: "2020-10-03T09:14:01.703Z"
size_mb: 2595
size: 874893343
sif: "https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/1804/2020-10-03-421c7122-0959ee85/0959ee852dba5de22eb031a9ed753285.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pmitev/Teoroo-singularity/1804/2020-10-03-421c7122-0959ee85/
recipe: https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/1804/2020-10-03-421c7122-0959ee85/Singularity
collection: pmitev/Teoroo-singularity
---

# pmitev/Teoroo-singularity:1804

```bash
$ singularity pull shub://pmitev/Teoroo-singularity:1804
```

## Singularity Recipe

```singularity
Bootstrap:  docker
From: ubuntu:18.04

%runscript
  export PATH=/usr/local/bin:$PATH
  export XDG_RUNTIME_DIR=/tmp/.run_$(uuidgen)
  /bin/bash

%setup


%files

%environment
  export PYTHONNOUSERSITE=True
%post
  apt-get update && apt-get install -y \
    bash-completion \
    build-essential \
    bzip2 \
    csh \
    curl \
    cython \
    elinks \
    evince \
    expect \
    gawk \
    gfortran \
    git \
    gnuplot \
    libgmp3-dev \
    grace \
    gv \
    htop \
    imagemagick \
    inkscape \
    libopenblas-dev \
    libnuma1 \
    locales \
    lsof \
    mc \
    ncdu \
    netcat-openbsd \
    nload \
    octave \
    pandoc \
    pbzip2 \
    pv \
    python3-dev python3-pip python3-tk \
    rsh-client \
    screen \
    spyder \
    sqlite \
    sqlitebrowser \
    openssh-client \
    units \
    uuid-runtime \
    vim \
    wget \
    xclip \
&& rm -rf /var/lib/apt/lists/*

  locale-gen en_US.UTF-8 &&  update-locale

  apt-get update && apt-get install -y python3-pip python-pip

  /usr/bin/env python3 -m  pip install --no-cache-dir --upgrade pip
  /usr/bin/env python3 -m  pip install --no-cache-dir --upgrade ase
  /usr/bin/env python3 -m  pip install --no-cache-dir --upgrade nglview
  /usr/bin/env python3 -m  pip install --no-cache-dir --upgrade pymatgen
  /usr/bin/env python3 -m  pip install --no-cache-dir --upgrade phonopy
  /usr/bin/env python3 -m  pip install --no-cache-dir --upgrade jupyter
  /usr/bin/env python3 -m  pip install --no-cache-dir --upgrade notebook
  /usr/bin/env python3 -m  pip install --no-cache-dir --upgrade metakernel
  /usr/bin/env python3 -m  pip install --no-cache-dir --upgrade gnuplot_kernel
  /usr/bin/env python3 -m  pip install --no-cache-dir --upgrade fortran-magic
  /usr/bin/env python3 -m  pip install --no-cache-dir --upgrade lxml
  /usr/bin/env python3 -m  pip install --no-cache-dir --upgrade pandoc
  /usr/bin/env python3 -m  pip install --no-cache-dir --upgrade ipywidgets
  /usr/bin/env python3 -m  pip install --no-cache-dir --upgrade ipykernel
  /usr/bin/env python3 -m  pip install --no-cache-dir --upgrade gmpy
  /usr/bin/env python3 -m  ipykernel install

  /usr/bin/env python3 -m  pip install --upgrade jupyter_contrib_nbextensions
  jupyter contrib nbextension install --system
  jupyter nbextension enable codefolding/main

  /usr/bin/env python3 -m  pip install --upgrade jupyter_nbextensions_configurator
  jupyter nbextensions_configurator enable --system

  jupyter-nbextension enable nglview --py --sys-prefix
```

## Collection

 - Name: [pmitev/Teoroo-singularity](https://github.com/pmitev/Teoroo-singularity)
 - License: None

