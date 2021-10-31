---
id: 6055
name: "nickjer/singularity-rstudio"
branch: "master"
tag: "3.5.2"
commit: "0b6126d8a79c641345f0435f3cf3fa3d018329b5"
version: "605d75473a063ca2c5f884b881d24c27"
build_date: "2020-08-12T20:49:47.202Z"
size_mb: 996
size: 311226399
sif: "https://datasets.datalad.org/shub/nickjer/singularity-rstudio/3.5.2/2020-08-12-0b6126d8-605d7547/605d75473a063ca2c5f884b881d24c27.simg"
url: https://datasets.datalad.org/shub/nickjer/singularity-rstudio/3.5.2/2020-08-12-0b6126d8-605d7547/
recipe: https://datasets.datalad.org/shub/nickjer/singularity-rstudio/3.5.2/2020-08-12-0b6126d8-605d7547/Singularity
collection: nickjer/singularity-rstudio
---

# nickjer/singularity-rstudio:3.5.2

```bash
$ singularity pull shub://nickjer/singularity-rstudio:3.5.2
```

## Singularity Recipe

```singularity
BootStrap: shub
From: nickjer/singularity-r:3.5.2

%labels
  Maintainer Jeremy Nicklas
  RStudio_Version 1.1.463

%help
  This will run RStudio Server

%apprun rserver
  exec rserver "${@}"

%runscript
  exec rserver "${@}"

%environment
  export PATH=/usr/lib/rstudio-server/bin:${PATH}

%setup
  install -Dv \
    rstudio_auth.sh \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/rstudio_auth
  install -Dv \
    ldap_auth.py \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/ldap_auth

%post
  # Software versions
  export RSTUDIO_VERSION=1.1.463

  # Install RStudio Server
  apt-get update
  apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    gdebi-core
  wget \
    --no-verbose \
    -O rstudio-server.deb \
    "https://download2.rstudio.org/rstudio-server-${RSTUDIO_VERSION}-amd64.deb"
  gdebi -n rstudio-server.deb
  rm -f rstudio-server.deb

  # Add support for LDAP authentication
  wget \
    --no-verbose \
    -O get-pip.py \
    "https://bootstrap.pypa.io/get-pip.py"
  python3 get-pip.py
  rm -f get-pip.py
  pip3 install ldap3

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [nickjer/singularity-rstudio](https://github.com/nickjer/singularity-rstudio)
 - License: [MIT License](https://api.github.com/licenses/mit)

