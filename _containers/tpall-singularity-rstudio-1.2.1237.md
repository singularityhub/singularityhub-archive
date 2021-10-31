---
id: 6358
name: "tpall/singularity-rstudio"
branch: "master"
tag: "1.2.1237"
commit: "2ddf606df38687091e69e39661581fac81e27b8b"
version: "cd994ae3b881764d96c599da7bca0c54"
build_date: "2019-01-30T09:02:36.663Z"
size_mb: 1282
size: 379174943
sif: "https://datasets.datalad.org/shub/tpall/singularity-rstudio/1.2.1237/2019-01-30-2ddf606d-cd994ae3/cd994ae3b881764d96c599da7bca0c54.simg"
url: https://datasets.datalad.org/shub/tpall/singularity-rstudio/1.2.1237/2019-01-30-2ddf606d-cd994ae3/
recipe: https://datasets.datalad.org/shub/tpall/singularity-rstudio/1.2.1237/2019-01-30-2ddf606d-cd994ae3/Singularity
collection: tpall/singularity-rstudio
---

# tpall/singularity-rstudio:1.2.1237

```bash
$ singularity pull shub://tpall/singularity-rstudio:1.2.1237
```

## Singularity Recipe

```singularity
BootStrap: shub
From: tpall/singularity-r:3.5.2

%labels
  Author Jeremy Nicklas
  Maintainer tpall
  RStudio_Version 1.2.1237

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
  export RSTUDIO_VERSION=1.2.1237

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

