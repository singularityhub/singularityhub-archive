---
id: 7261
name: "tpall/singularity-rstudio"
branch: "debian"
tag: "latest"
commit: "5bad941a1f3376f87e8ba47599358b6fa8d5e633"
version: "9a27dad6e7c5260369a1f175883c613c"
build_date: "2020-06-02T01:36:05.792Z"
size_mb: 1017
size: 347762719
sif: "https://datasets.datalad.org/shub/tpall/singularity-rstudio/latest/2020-06-02-5bad941a-9a27dad6/9a27dad6e7c5260369a1f175883c613c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/tpall/singularity-rstudio/latest/2020-06-02-5bad941a-9a27dad6/
recipe: https://datasets.datalad.org/shub/tpall/singularity-rstudio/latest/2020-06-02-5bad941a-9a27dad6/Singularity
collection: tpall/singularity-rstudio
---

# tpall/singularity-rstudio:latest

```bash
$ singularity pull shub://tpall/singularity-rstudio:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: tpall/singularity-r@debian

%labels
  Maintainer tpall
  RStudio_Version 1.2.1256

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
  export RSTUDIO_VERSION=${RSTUDIO_VERSION:-1.2.1256}
  
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
  && wget -q https://s3.amazonaws.com/rstudio-ide-build/server/debian9/x86_64/rstudio-server-${RSTUDIO_VERSION}-amd64.deb \
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

