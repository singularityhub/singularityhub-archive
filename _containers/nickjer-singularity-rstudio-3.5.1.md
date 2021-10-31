---
id: 3409
name: "nickjer/singularity-rstudio"
branch: "master"
tag: "3.5.1"
commit: "dde88ab26f6d40b8337fd08a8128dabe8de15f05"
version: "5957efe5d7829f4d2a9d26a9d8c855e9"
build_date: "2021-02-07T15:39:50.414Z"
size_mb: 995
size: 310886431
sif: "https://datasets.datalad.org/shub/nickjer/singularity-rstudio/3.5.1/2021-02-07-dde88ab2-5957efe5/5957efe5d7829f4d2a9d26a9d8c855e9.simg"
url: https://datasets.datalad.org/shub/nickjer/singularity-rstudio/3.5.1/2021-02-07-dde88ab2-5957efe5/
recipe: https://datasets.datalad.org/shub/nickjer/singularity-rstudio/3.5.1/2021-02-07-dde88ab2-5957efe5/Singularity
collection: nickjer/singularity-rstudio
---

# nickjer/singularity-rstudio:3.5.1

```bash
$ singularity pull shub://nickjer/singularity-rstudio:3.5.1
```

## Singularity Recipe

```singularity
BootStrap: shub
From: nickjer/singularity-r:3.5.1

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

