---
id: 15362
name: "saviodot/singularity-rstudio"
branch: "master"
tag: "latest"
commit: "8aa01c98d774f17fffe7a4a179183617f21ee731"
version: "5419a7aa09fa0263ebefa409e6b2cd74"
build_date: "2021-02-04T01:03:55.740Z"
size_mb: 1457.0
size: 450580511
sif: "https://datasets.datalad.org/shub/saviodot/singularity-rstudio/latest/2021-02-04-8aa01c98-5419a7aa/5419a7aa09fa0263ebefa409e6b2cd74.sif"
url: https://datasets.datalad.org/shub/saviodot/singularity-rstudio/latest/2021-02-04-8aa01c98-5419a7aa/
recipe: https://datasets.datalad.org/shub/saviodot/singularity-rstudio/latest/2021-02-04-8aa01c98-5419a7aa/Singularity
collection: saviodot/singularity-rstudio
---

# saviodot/singularity-rstudio:latest

```bash
$ singularity pull shub://saviodot/singularity-rstudio:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: j-andrews7/singularity-r

%labels
  Maintainer Jared Andrews
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

  # Install RStudio Server, added libgit2-dev
  add-apt-repository ppa:cran/libgit2
  apt-get update
  apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    gdebi-core \
    libssh2-1-dev \
    libgit2-dev \
    libproj-dev
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
  python3.8 get-pip.py
  rm -f get-pip.py
  python3.8 -m pip install ldap3
  python3.8 -m pip install numpy 
  python3.8 -m pip install MACS2

  # Disable session timeout
  echo "session-timeout-minutes=0" > /etc/rstudio/rsession.conf

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [saviodot/singularity-rstudio](https://github.com/saviodot/singularity-rstudio)
 - License: [MIT License](https://api.github.com/licenses/mit)

