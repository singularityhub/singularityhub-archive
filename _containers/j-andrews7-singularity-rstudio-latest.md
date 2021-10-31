---
id: 13946
name: "j-andrews7/singularity-rstudio"
branch: "master"
tag: "latest"
commit: "d7c40e06c109c368c28843b2d91235b8797b7ef8"
version: "02cee3b6962613fd6d26ccdbc6fc0c97"
build_date: "2021-04-19T16:12:54.486Z"
size_mb: 1602.0
size: 498253855
sif: "https://datasets.datalad.org/shub/j-andrews7/singularity-rstudio/latest/2021-04-19-d7c40e06-02cee3b6/02cee3b6962613fd6d26ccdbc6fc0c97.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/j-andrews7/singularity-rstudio/latest/2021-04-19-d7c40e06-02cee3b6/
recipe: https://datasets.datalad.org/shub/j-andrews7/singularity-rstudio/latest/2021-04-19-d7c40e06-02cee3b6/Singularity
collection: j-andrews7/singularity-rstudio
---

# j-andrews7/singularity-rstudio:latest

```bash
$ singularity pull shub://j-andrews7/singularity-rstudio:latest
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

  # Install RStudio Server
  apt-get update
  apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    gdebi-core \
    librsvg2-dev\
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

 - Name: [j-andrews7/singularity-rstudio](https://github.com/j-andrews7/singularity-rstudio)
 - License: [MIT License](https://api.github.com/licenses/mit)

