---
id: 14225
name: "Xentrics/jupyter-r-base"
branch: "master"
tag: "geo2rnaseq"
commit: "a864f7e6815100a75b488e5f828543fa5d988003"
version: "8f0b9db640a3a3883c85ef425ee824a9aa75110550f244054dbfe75899ce6912"
build_date: "2021-02-17T17:51:14.540Z"
size_mb: 1041.12890625
size: 1091702784
sif: "https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/geo2rnaseq/2021-02-17-a864f7e6-8f0b9db6/8f0b9db640a3a3883c85ef425ee824a9aa75110550f244054dbfe75899ce6912.sif"
url: https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/geo2rnaseq/2021-02-17-a864f7e6-8f0b9db6/
recipe: https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/geo2rnaseq/2021-02-17-a864f7e6-8f0b9db6/Singularity
collection: Xentrics/jupyter-r-base
---

# Xentrics/jupyter-r-base:geo2rnaseq

```bash
$ singularity pull shub://Xentrics/jupyter-r-base:geo2rnaseq
```

## Singularity Recipe

```singularity
BootStrap: shub
From: Xentrics/jupyter-r-base:r3.6.3


%labels
  LICENSE Copyright 2020 Bastian Seelbinder, 
     Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
     to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
     and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above
     copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. 
  Maintainer Bastian Seelbinder

%help
  This will run RStudio Server with GEO2RNAseq installed

%apprun rserver
  exec /usr/lib/rstudio-server/bin/rserver "${@}"

%runscript
  exec /usr/lib/rstudio-server/bin/rserver "${@}"

%environment
  export PATH=/usr/lib/rstudio-server/bin:${PATH}
  export LC_ALL=C.UTF-8
  export LANG=C.UTF-8

%post

  # to solve the "locale.Error: unsupported locale setting" error [https://stackoverflow.com/questions/14547631/python-locale-error-unsupported-locale-setting ]
  export LC_ALL=C.UTF-8
  export LANG=C.UTF-8
  
  # select default keyboard layout
  echo "XKBMODEL='pc105'" >> /etc/default/keyboard
  echo "XKBLAYOUT='de'"  >> /etc/default/keyboard
  echo "XKBVARIANT=''"  >> /etc/default/keyboard
  echo "XKBOPTIONS=''"  >> /etc/default/keyboard
  echo "BACKSPACE='guess'"  >> /etc/default/keyboard
  
  apt-get -y update
  DEBIAN_FRONTEND=noninteractive apt-get -y install keyboard-configuration
  DEBIAN_FRONTEND=noninteractive apt-get -y install console-setup

  # first install the following packages
  apt-get -y update && apt-get -y dist-upgrade
  apt-get install -y python3
  apt-get install -y debootstrap libarchive-dev squashfs-tools
  apt-get install -y libtool m4 automake
  apt-get install -y python3-pip
  apt-get install -y nano git cmake gfortran curl wget autoconf bzip2 libtool libtool-bin sudo             # "sudo" is not installed by default in containers like docker, singularity
  apt-get install -y libgtk3-nocsd0
  
  # geo2rnaseq related
  apt install -y samtools tophat hisat2 fastqc sortmerna sra-toolkit trimmomatic pandoc
  apt install -y perl perl-base default-jre openjdk-8-jre
  
  pip3 install multiqc==1.7
  
  
  
  echo "options(repos = c(CRAN = 'https://cloud.r-project.org/'), download.file.method = 'libcurl')" >> /usr/lib/R/etc/Rprofile.site

  # Install Core R packages
  export R_LIBS_USER="/usr/local/lib/R/site-library" # make sure packages go here
  R --vanilla -e 'options("Ncpus"=10); install.packages(c("BiocManager", "devtools"), repos="https://cloud.r-project.org", Ncpus = 10)'
  
  # Install GEO2RNAseq from source
  R --vanilla -e 'options("Ncpus"=10); devtools::install_bitbucket("Xentrics/geo2rnaseq", dependencies=TRUE)'
  
  
  

  # Software versions
  export RSTUDIO_VERSION=1.2.5019

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
    "https://download2.rstudio.org/server/bionic/amd64/rstudio-server-${RSTUDIO_VERSION}-amd64.deb"
  gdebi -n rstudio-server.deb
  rm -f rstudio-server.deb

  # R package specific libraries
  apt-get install -y libcurl4-gnutls-dev libgit2-dev libopenblas-dev r-base-core libfontconfig1-dev libcairo2-dev
  apt-get install -y openssh-client openssh-server libssh-dev wget vim git gfortran autoconf pandoc qpdf libssh2-1-dev
  
  

  # cleanup
  rm -rf /var/lib/apt/lists/*

  
  # Install additional packages for more convinient use
  R --vanilla -e 'BiocManager::install(c("tidyverse", "magrittr", "readxl", "writexl"), Ncpus = 10)'
```

## Collection

 - Name: [Xentrics/jupyter-r-base](https://github.com/Xentrics/jupyter-r-base)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

