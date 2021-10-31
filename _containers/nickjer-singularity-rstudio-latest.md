---
id: 1598
name: "nickjer/singularity-rstudio"
branch: "master"
tag: "latest"
commit: "d261002009b55218923d523e9b71c70ea5edd4d3"
version: "0e88886784700df35a95d59ac45cef81"
build_date: "2021-04-19T21:27:36.114Z"
size_mb: 1242.0
size: 365441055
sif: "https://datasets.datalad.org/shub/nickjer/singularity-rstudio/latest/2021-04-19-d2610020-0e888867/0e88886784700df35a95d59ac45cef81.sif"
url: https://datasets.datalad.org/shub/nickjer/singularity-rstudio/latest/2021-04-19-d2610020-0e888867/
recipe: https://datasets.datalad.org/shub/nickjer/singularity-rstudio/latest/2021-04-19-d2610020-0e888867/Singularity
collection: nickjer/singularity-rstudio
---

# nickjer/singularity-rstudio:latest

```bash
$ singularity pull shub://nickjer/singularity-rstudio:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: nickjer/singularity-r

%labels
  Maintainer Jeremy Nicklas
  RStudio_Version 1.2.5033

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
  export RSTUDIO_VERSION=1.2.5033

  # Install RStudio Server
  apt-get update
  apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    gdebi-core
  wget \
    --no-verbose \
    -O rstudio-server.deb \
    "https://download2.rstudio.org/server/trusty/amd64/rstudio-server-${RSTUDIO_VERSION}-amd64.deb"
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

