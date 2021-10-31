---
id: 3667
name: "mlampros/singularity_containers"
branch: "master"
tag: "rgf_r"
commit: "6b047e8f8e520cbdc55cf29b346c1984ec4a1d14"
version: "d9b527d4e7995927310d4408d74791d1"
build_date: "2020-04-03T08:39:43.989Z"
size_mb: 1577
size: 549335071
sif: "https://datasets.datalad.org/shub/mlampros/singularity_containers/rgf_r/2020-04-03-6b047e8f-d9b527d4/d9b527d4e7995927310d4408d74791d1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mlampros/singularity_containers/rgf_r/2020-04-03-6b047e8f-d9b527d4/
recipe: https://datasets.datalad.org/shub/mlampros/singularity_containers/rgf_r/2020-04-03-6b047e8f-d9b527d4/Singularity
collection: mlampros/singularity_containers
---

# mlampros/singularity_containers:rgf_r

```bash
$ singularity pull shub://mlampros/singularity_containers:rgf_r
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
  apt-get -y update && apt-get -y dist-upgrade
  apt-get install -y python3
  apt-get install -y debootstrap libarchive-dev squashfs-tools
  apt-get install -y libtool m4 automake && apt-get install -y python3-pip
  apt-get install -y nano git cmake gfortran curl wget autoconf bzip2 libtool libtool-bin sudo             # "sudo" is not installed by default in containers like docker, singularity
  pip3 install --upgrade setuptools
  pip3 install -U numpy
  pip3 install --upgrade scipy
  pip3 install -U scikit-learn

  sudo pip3 install rgf_python                                                                             # requires "sudo" [ system-wide installation ]

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

  # RGF specific packages / modules / libraries
  apt-get install -y libcurl4-gnutls-dev libgit2-dev libopenblas-dev r-base-core
  apt-get install -y openssh-client openssh-server libssh-dev wget vim git gfortran autoconf pandoc qpdf libssh2-1-dev

  R --slave -e 'install.packages(c("devtools", "roxygen2", "testthat", "Matrix", "reticulate", "R6", "covr", "knitr", "rmarkdown"), repos="https://cloud.r-project.org/")'
  R --slave -e 'devtools::install_github("mlampros/RGF")'

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [mlampros/singularity_containers](https://github.com/mlampros/singularity_containers)
 - License: [Other](None)

