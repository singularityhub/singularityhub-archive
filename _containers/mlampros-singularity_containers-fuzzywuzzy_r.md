---
id: 3668
name: "mlampros/singularity_containers"
branch: "master"
tag: "fuzzywuzzy_r"
commit: "a8162765e75f26505db1b65af95a692a058ff2f5"
version: "d0de5ebbe5cd7e272770c7f9ae3db50b"
build_date: "2019-07-25T18:03:15.203Z"
size_mb: 1409
size: 464048159
sif: "https://datasets.datalad.org/shub/mlampros/singularity_containers/fuzzywuzzy_r/2019-07-25-a8162765-d0de5ebb/d0de5ebbe5cd7e272770c7f9ae3db50b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mlampros/singularity_containers/fuzzywuzzy_r/2019-07-25-a8162765-d0de5ebb/
recipe: https://datasets.datalad.org/shub/mlampros/singularity_containers/fuzzywuzzy_r/2019-07-25-a8162765-d0de5ebb/Singularity
collection: mlampros/singularity_containers
---

# mlampros/singularity_containers:fuzzywuzzy_r

```bash
$ singularity pull shub://mlampros/singularity_containers:fuzzywuzzy_r
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

  # fuzzywuzzyR specific packages / modules / libraries
  apt-get install -y libcurl4-gnutls-dev libgit2-dev libopenblas-dev r-base-core
  apt-get install -y openssh-client openssh-server libssh-dev wget vim git nano git cmake gfortran g++ curl wget python autoconf bzip2 libtool libtool-bin python-pip python-dev pandoc qpdf libssh2-1-dev

  pip install --upgrade pip==9.0.3                               # do this because there is a problem with 'python-pip' ( SEE : https://github.com/pypa/pip/issues/5240#issuecomment-381673100 )
  pip install numpy fuzzywuzzy python-Levenshtein

  R --slave -e 'install.packages(c("devtools", "roxygen2", "testthat", "reticulate", "R6", "covr", "knitr", "rmarkdown", "fuzzywuzzyR"), repos="https://cloud.r-project.org/")'

  apt-get update

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [mlampros/singularity_containers](https://github.com/mlampros/singularity_containers)
 - License: [Other](None)

