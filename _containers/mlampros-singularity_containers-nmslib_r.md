---
id: 3669
name: "mlampros/singularity_containers"
branch: "master"
tag: "nmslib_r"
commit: "7d59533db19f4eed46bc376fe8a9533c4e966d9a"
version: "f22f19a9e54e556d2645c255b2c130a8"
build_date: "2018-07-25T23:56:14.679Z"
size_mb: 1938
size: 648126495
sif: "https://datasets.datalad.org/shub/mlampros/singularity_containers/nmslib_r/2018-07-25-7d59533d-f22f19a9/f22f19a9e54e556d2645c255b2c130a8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mlampros/singularity_containers/nmslib_r/2018-07-25-7d59533d-f22f19a9/
recipe: https://datasets.datalad.org/shub/mlampros/singularity_containers/nmslib_r/2018-07-25-7d59533d-f22f19a9/Singularity
collection: mlampros/singularity_containers
---

# mlampros/singularity_containers:nmslib_r

```bash
$ singularity pull shub://mlampros/singularity_containers:nmslib_r
```

## Singularity Recipe

```singularity
BootStrap: shub
From: nickjer/singularity-r:3.5.1

%labels

  LICENSE Copyright 2018 Jeremy Nicklas, Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), 
                                         to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
                                         and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above
                                         copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. 
  Maintainer Mouselimis Lampros
  NOTES  Modification of the initial .def file ( Singularity.3.5.1 ) found in https://github.com/nickjer/singularity-rstudio/blob/master/Singularity.3.5.1
  RStudio_Version 1.1.453

%help
  This will run RStudio Server


%apprun rserver
  exec rserver "${@}"


%runscript
  exec rserver "${@}"


%environment
  export PATH=/usr/lib/rstudio-server/bin:${PATH}


%post

  # to solve the "locale.Error: unsupported locale setting" error [https://stackoverflow.com/questions/14547631/python-locale-error-unsupported-locale-setting ]
  export LC_ALL=C

  # first install the following packages
  apt-get -y update && apt-get -y upgrade
  apt-get install -y python3-pip
  pip3 install --upgrade pip==9.0.3 setuptools wheel
  apt-get install -y python3
  apt-get install -y debootstrap libarchive-dev squashfs-tools
  apt-get install -y libtool m4 automake
  pip3 install -U numpy
  pip3 install --upgrade scipy
  apt-get install -y cmake
  pip3 install --upgrade pybind11
  pip3 install nmslib
  apt-get update

  # Software versions
  export RSTUDIO_VERSION=1.1.453

  # Install RStudio Server
  apt-get update
  apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    gdebi-core \
    python3-pip
  wget \
    --no-verbose \
    -O rstudio-server.deb \
    "https://download2.rstudio.org/rstudio-server-${RSTUDIO_VERSION}-amd64.deb"
  gdebi -n rstudio-server.deb
  rm -f rstudio-server.deb

  # nmslibR specific packages / modules / libraries
  apt-get install -y libcurl4-gnutls-dev libgit2-dev libopenblas-dev r-base-core
  apt-get install -y openssh-client openssh-server libssh-dev wget vim git nano git cmake gfortran g++ curl wget autoconf bzip2 libtool libtool-bin pandoc qpdf libssh2-1-dev
  apt-get install -y libboost-all-dev libgsl-dev libeigen3-dev cmake

  R --slave -e 'install.packages(c("devtools", "roxygen2", "Rcpp", "reticulate", "R6", "Matrix", "KernelKnn", "utils", "RcppArmadillo", "testthat", "covr", "knitr", "rmarkdown"), repos="https://cloud.r-project.org/")'
  R --slave -e 'devtools::install_github("mlampros/nmslibR")'

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [mlampros/singularity_containers](https://github.com/mlampros/singularity_containers)
 - License: [Other](None)

