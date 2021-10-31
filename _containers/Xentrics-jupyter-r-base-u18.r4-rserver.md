---
id: 13164
name: "Xentrics/jupyter-r-base"
branch: "master"
tag: "u18.r4-rserver"
commit: "088ba48beef7ca47b365cc34dae8dd6a51fc64ce"
version: "50d51f59dd9b8b7b549a62a2f5cb029451f78ba276d415823a291f72b2943e48"
build_date: "2020-09-09T14:08:48.797Z"
size_mb: 1519.57421875
size: 1593389056
sif: "https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/u18.r4-rserver/2020-09-09-088ba48b-50d51f59/50d51f59dd9b8b7b549a62a2f5cb029451f78ba276d415823a291f72b2943e48.sif"
url: https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/u18.r4-rserver/2020-09-09-088ba48b-50d51f59/
recipe: https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/u18.r4-rserver/2020-09-09-088ba48b-50d51f59/Singularity
collection: Xentrics/jupyter-r-base
---

# Xentrics/jupyter-r-base:u18.r4-rserver

```bash
$ singularity pull shub://Xentrics/jupyter-r-base:u18.r4-rserver
```

## Singularity Recipe

```singularity
BootStrap: shub
From: Xentrics/jupyter-r-base:r4
#Bootstrap: localimage
#From: Singularity.r4.sif

%labels

  LICENSE Copyright 2020 Bastian Seelbinder, 
     Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
     to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
     and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above
     copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. 
  Maintainer Bastian Seelbinder
  RStudio_Version 1.2.5019

%help
  This will run RStudio Server

%apprun rserver
  exec /usr/lib/rstudio-server/bin/rserver "${@}"

%runscript
  exec /usr/lib/rstudio-server/bin/rserver "${@}"

%environment
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
  #dpkg-reconfigure keyboard-configuration

  # first install the following packages
  apt-get install -y python3
  apt-get install -y debootstrap libarchive-dev squashfs-tools libsodium-dev
  apt-get install -y libtool m4 automake
  apt-get install -y python3-pip
  apt-get install -y nano git cmake gfortran curl wget autoconf bzip2 libtool libtool-bin sudo             # "sudo" is not installed by default in containers like docker, singularity
  apt-get install -y cryptsetup
  apt-get install -y libgtk3-nocsd0
  
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
  
  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [Xentrics/jupyter-r-base](https://github.com/Xentrics/jupyter-r-base)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

