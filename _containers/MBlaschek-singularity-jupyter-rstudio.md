---
id: 11712
name: "MBlaschek/singularity-jupyter"
branch: "master"
tag: "rstudio"
commit: "dd684419b34f874b819c6ec1abefe53f4d50c75b"
version: "85cfb1895a44f3e84c5b6d7a07bdbd1004b59b197f82e43f81c27b95085e5eed"
build_date: "2020-02-28T16:27:14.068Z"
size_mb: 595.0
size: 357101568
sif: "https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/rstudio/2020-02-28-dd684419-85cfb189/85cfb1895a44f3e84c5b6d7a07bdbd1004b59b197f82e43f81c27b95085e5eed.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/MBlaschek/singularity-jupyter/rstudio/2020-02-28-dd684419-85cfb189/
recipe: https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/rstudio/2020-02-28-dd684419-85cfb189/Singularity
collection: MBlaschek/singularity-jupyter
---

# MBlaschek/singularity-jupyter:rstudio

```bash
$ singularity pull shub://MBlaschek/singularity-jupyter:rstudio
```

## Singularity Recipe

```singularity
BootStrap: shub
From: nickjer/singularity-r

%labels
  Maintainer Jeremy Nicklas
  RStudio_Version 1.2.1335

%help
  This will run RStudio Server

%apprun rserver
  exec rserver "${@}"

%runscript
  exec rserver "${@}"

%setup
  install -Dv \
    rserver/rstudio_auth.sh \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/rstudio_auth
  install -Dv \
    rserver/ldap_auth.py \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/ldap_auth

%post
  # Software versions
  export RSTUDIO_VERSION=1.2.1335

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
    "https://download2.rstudio.org/server/trusty/amd64/rstudio-server-${RSTUDIO_VERSION}-amd64.deb"

  gdebi -n rstudio-server.deb
  rm -f rstudio-server.deb

  # Add support for LDAP authentication
  pip3 install ldap3

  # Clean up
  apt clean
  rm -rf /var/lib/apt/lists/*

%startscript
  nohup rserver --auth-none 0 --auth-pam-helper rstudio_auth --www-port $RSTUDIO_PORT > /dev/null 2>&1 < /dev/null &

%environment
  export RSTUDIO_PORT=9090
  export RSTUDIO_PASSWORD="password"
  export PATH=/usr/lib/rstudio-server/bin:${PATH}
```

## Collection

 - Name: [MBlaschek/singularity-jupyter](https://github.com/MBlaschek/singularity-jupyter)
 - License: None

