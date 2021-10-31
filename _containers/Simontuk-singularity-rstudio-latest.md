---
id: 10664
name: "Simontuk/singularity-rstudio"
branch: "master"
tag: "latest"
commit: "0947b1f9088bb2e2282efb1ea81b378e0b83bdaf"
version: "10e90e05e0f19c3a5416ba03f8f2de988a755f66e2be0248f3fb3970707af595"
build_date: "2019-08-20T14:17:53.223Z"
size_mb: 1251.0
size: 549593088
sif: "https://datasets.datalad.org/shub/Simontuk/singularity-rstudio/latest/2019-08-20-0947b1f9-10e90e05/10e90e05e0f19c3a5416ba03f8f2de988a755f66e2be0248f3fb3970707af595.sif"
url: https://datasets.datalad.org/shub/Simontuk/singularity-rstudio/latest/2019-08-20-0947b1f9-10e90e05/
recipe: https://datasets.datalad.org/shub/Simontuk/singularity-rstudio/latest/2019-08-20-0947b1f9-10e90e05/Singularity
collection: Simontuk/singularity-rstudio
---

# Simontuk/singularity-rstudio:latest

```bash
$ singularity pull shub://Simontuk/singularity-rstudio:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: Simontuk/singularity-r

%labels
  Maintainer Simon Steiger
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
  yum update
  yum install -y \
    ca-certificates \
    wget

  wget --no-verbose \
    -O rstudio-server.rpm \
    https://download2.rstudio.org/server/centos6/x86_64/rstudio-server-rhel-${RSTUDIO_VERSION}-x86_64.rpm
  yum install -y rstudio-server.rpm
  rm -f rstudio-server.rpm

  # Add support for LDAP authentication
  yum -y install https://centos7.iuscommunity.org/ius-release.rpm
  yum -y install python36u
  yum -y install python36u-pip
  pip3.6 install ldap3

  #htop
  yum install -y htop ksh
  # Clean up
  yum clean all
```

## Collection

 - Name: [Simontuk/singularity-rstudio](https://github.com/Simontuk/singularity-rstudio)
 - License: [MIT License](https://api.github.com/licenses/mit)

