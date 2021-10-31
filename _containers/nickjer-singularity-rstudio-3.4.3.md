---
id: 1599
name: "nickjer/singularity-rstudio"
branch: "master"
tag: "3.4.3"
commit: "de1de623ceb3c3843e0033ac21587d419b7d68fc"
version: "c345cddb2db3689597b1e2fd32af54e7"
build_date: "2021-03-12T20:00:23.855Z"
size_mb: 977
size: 305455135
sif: "https://datasets.datalad.org/shub/nickjer/singularity-rstudio/3.4.3/2021-03-12-de1de623-c345cddb/c345cddb2db3689597b1e2fd32af54e7.simg"
url: https://datasets.datalad.org/shub/nickjer/singularity-rstudio/3.4.3/2021-03-12-de1de623-c345cddb/
recipe: https://datasets.datalad.org/shub/nickjer/singularity-rstudio/3.4.3/2021-03-12-de1de623-c345cddb/Singularity
collection: nickjer/singularity-rstudio
---

# nickjer/singularity-rstudio:3.4.3

```bash
$ singularity pull shub://nickjer/singularity-rstudio:3.4.3
```

## Singularity Recipe

```singularity
BootStrap: shub
From: nickjer/singularity-r:3.4.3

%labels
  Maintainer Jeremy Nicklas
  RStudio_Version 1.1.453

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

  # Add support for LDAP authentication
  pip3 install ldap3

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [nickjer/singularity-rstudio](https://github.com/nickjer/singularity-rstudio)
 - License: [MIT License](https://api.github.com/licenses/mit)

