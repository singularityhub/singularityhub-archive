---
id: 6928
name: "tpall/singularity-rstudio"
branch: "debian"
tag: "1.1.463"
commit: "578d951327539a43e2f1fd17b0786db32b57f674"
version: "bba71955c1f52bbdf0967d51a1c87574"
build_date: "2020-04-07T06:00:29.685Z"
size_mb: 1361
size: 410198047
sif: "https://datasets.datalad.org/shub/tpall/singularity-rstudio/1.1.463/2020-04-07-578d9513-bba71955/bba71955c1f52bbdf0967d51a1c87574.simg"
url: https://datasets.datalad.org/shub/tpall/singularity-rstudio/1.1.463/2020-04-07-578d9513-bba71955/
recipe: https://datasets.datalad.org/shub/tpall/singularity-rstudio/1.1.463/2020-04-07-578d9513-bba71955/Singularity
collection: tpall/singularity-rstudio
---

# tpall/singularity-rstudio:1.1.463

```bash
$ singularity pull shub://tpall/singularity-rstudio:1.1.463
```

## Singularity Recipe

```singularity
BootStrap: shub
From: tpall/singularity-r@debian

%labels
  Maintainer tpall
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
  export RSTUDIO_VERSION=${RSTUDIO_VERSION:-1.1.463}
  
  ## Download and install RStudio server & dependencies
  ## Attempts to get detect latest version, otherwise falls back to version given in $VER
  apt-get update \
  && apt-get install -y --no-install-recommends \
    file \
    git \
    libapparmor1 \
    libcurl4-openssl-dev \
    libedit2 \
    libssl-dev \
    libclang-dev \
    libpq-dev \
    lsb-release \
    psmisc \
    procps \
    python-setuptools \
    sudo \
    wget \
    openssh-client \
  && wget -O libssl1.0.2.deb http://ftp.br.debian.org/debian/pool/main/o/openssl1.0/libssl1.0.2_1.0.2l-2+deb9u3_amd64.deb \
  && dpkg -i libssl1.0.2.deb \
  && rm libssl1.0.2.deb \
  && wget -O libgit2-dev.deb http://ftp.br.debian.org/debian/pool/main/libg/libgit2/libgit2-dev_0.27.7+dfsg.1-0.1_amd64.deb \
  && dpkg -i libgit2-dev.deb \
  && rm libgit2-dev.deb \
  && RSTUDIO_LATEST=$(wget --no-check-certificate -qO- https://s3.amazonaws.com/rstudio-server/current.ver) \
  && [ -z "$RSTUDIO_VERSION" ] && RSTUDIO_VERSION=$RSTUDIO_LATEST || true \
  && wget -q http://download2.rstudio.org/rstudio-server-${RSTUDIO_VERSION}-amd64.deb \
  && dpkg -i rstudio-server-${RSTUDIO_VERSION}-amd64.deb \
  && rm rstudio-server-*-amd64.deb
  
  ## Clean up
  apt-get clean \
  && rm -rf /var/lib/apt/lists/
  
  ## Add support for LDAP authentication
  wget -q https://bootstrap.pypa.io/get-pip.py \
  && python3 get-pip.py \
  && rm get-pip.py \
  && pip3 install ldap3
```

## Collection

 - Name: [tpall/singularity-rstudio](https://github.com/tpall/singularity-rstudio)
 - License: [MIT License](https://api.github.com/licenses/mit)

