---
id: 6357
name: "tpall/singularity-rstudio"
branch: "master"
tag: "1.2.1226"
commit: "2ddf606df38687091e69e39661581fac81e27b8b"
version: "309a5f7be67bc2cd6b6f3c0c4ce37456"
build_date: "2019-01-30T09:02:36.671Z"
size_mb: 1282
size: 379179039
sif: "https://datasets.datalad.org/shub/tpall/singularity-rstudio/1.2.1226/2019-01-30-2ddf606d-309a5f7b/309a5f7be67bc2cd6b6f3c0c4ce37456.simg"
url: https://datasets.datalad.org/shub/tpall/singularity-rstudio/1.2.1226/2019-01-30-2ddf606d-309a5f7b/
recipe: https://datasets.datalad.org/shub/tpall/singularity-rstudio/1.2.1226/2019-01-30-2ddf606d-309a5f7b/Singularity
collection: tpall/singularity-rstudio
---

# tpall/singularity-rstudio:1.2.1226

```bash
$ singularity pull shub://tpall/singularity-rstudio:1.2.1226
```

## Singularity Recipe

```singularity
BootStrap: shub
From: tpall/singularity-r:3.5.2

%labels
  Author Jeremy Nicklas
  Maintainer tpall
  RStudio_Version 1.2.1226

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
  export RSTUDIO_VERSION=1.2.1226

  # Install RStudio Server
  apt-get update
  apt-get install -y \
    ca-certificates \
    wget \
    gdebi-core
  wget \
    --no-verbose \
    -O rstudio-server.deb \
    "https://s3.amazonaws.com/rstudio-ide-build/server/trusty/amd64/rstudio-server-${RSTUDIO_VERSION}-amd64.deb"
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

 - Name: [tpall/singularity-rstudio](https://github.com/tpall/singularity-rstudio)
 - License: [MIT License](https://api.github.com/licenses/mit)

