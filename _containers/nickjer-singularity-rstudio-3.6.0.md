---
id: 8719
name: "nickjer/singularity-rstudio"
branch: "master"
tag: "3.6.0"
commit: "67056e57e45cb06c66609fa82b0274ab32205662"
version: "15de72ec813ae5959127d81ade7e27f0"
build_date: "2020-08-12T20:50:01.856Z"
size_mb: 1234
size: 360783903
sif: "https://datasets.datalad.org/shub/nickjer/singularity-rstudio/3.6.0/2020-08-12-67056e57-15de72ec/15de72ec813ae5959127d81ade7e27f0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/nickjer/singularity-rstudio/3.6.0/2020-08-12-67056e57-15de72ec/
recipe: https://datasets.datalad.org/shub/nickjer/singularity-rstudio/3.6.0/2020-08-12-67056e57-15de72ec/Singularity
collection: nickjer/singularity-rstudio
---

# nickjer/singularity-rstudio:3.6.0

```bash
$ singularity pull shub://nickjer/singularity-rstudio:3.6.0
```

## Singularity Recipe

```singularity
BootStrap: shub
From: nickjer/singularity-r:3.6.0

%labels
  Maintainer Jeremy Nicklas
  RStudio_Version 1.2.1335

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
  export RSTUDIO_VERSION=1.2.1335

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

