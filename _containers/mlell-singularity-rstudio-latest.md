---
id: 14813
name: "mlell/singularity-rstudio"
branch: "master"
tag: "latest"
commit: "16c60d16c33653f19f8a9d433383e157a6b1450f"
version: "368b0aff17e9e14e1e0c6699bbb72fc2"
build_date: "2021-01-23T10:04:04.695Z"
size_mb: 3532.0
size: 1002545183
sif: "https://datasets.datalad.org/shub/mlell/singularity-rstudio/latest/2021-01-23-16c60d16-368b0aff/368b0aff17e9e14e1e0c6699bbb72fc2.sif"
url: https://datasets.datalad.org/shub/mlell/singularity-rstudio/latest/2021-01-23-16c60d16-368b0aff/
recipe: https://datasets.datalad.org/shub/mlell/singularity-rstudio/latest/2021-01-23-16c60d16-368b0aff/Singularity
collection: mlell/singularity-rstudio
---

# mlell/singularity-rstudio:latest

```bash
$ singularity pull shub://mlell/singularity-rstudio:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: mlell/singularity-r

%labels
  Maintainer Moritz Lell
  RStudio_Version 1.3.1056

%help
  This container features R linked to OpenBLAS and RStudio Server.

  While running this container manually is possible, it is recommended to 
  use the scripts `cexec` and `rstudio`, which are deployed along with this
  container file, as they offer settings for reproducable project paths and
  the possibility to run multiple RStudio Server sessions in the same
  directory.

  Host and port of RStudio server can be set by calling RStudio like this:
  `rserver --www-address <HOST> --www-port <PORT>`. For HOST, 127.0.0.1 is
  recommended, as this container provides no encryption of the connection to
  RStudio.

  When RStudio Server is run on a publicly accessable server, user
  authentication could be nessecary. This image provides different means of
  authentication, which can be chosen from by calling RStudio like this:
  `rserver --auth-none 0 --auth-pam-helper XXXX`, where XXXX is one of

  * rstudio_auth: The password is read from an environment variable named
    `RSTUDIO_PASSWORD` that can be set by the user

  * rstudio_auth_file: The password is read from a file whose path is defined
    by the environment variable `RSTUDIO_PASSWORD_FILE`, which can be set by
    the user. The password file can be created using the tool `rstudio_passwd`
    that is included in this container.

  * auth_ldap: User authentication is delegated to an LDAP server.
    call `singularity <CONTAINER> run help_ldap_auth` for more info.

  On a publicly accessable server, the HTTP connection to RStudio Server 
  must be encrypted by the user, as RStudio Server Community Edition only
  provides unencrypted HTTP access. The easiest ad-hoc solution would be an
  SSH tunnel `ssh -L 127.0.0.1:PORT:127.0.0.1:PORT USER@SERVER (note that some
  machines resolve `localhost` to the IPv6 address ::1 and not to the IPv4 
  127.0.0.1 which might cause confusion). Another possibility is a HTTPS server
  acting as a reverse proxy as described in
  https://support.rstudio.com/hc/en-us/articles/200552326-Running-RStudio-Server-with-a-Proxy

%apprun rserver
  exec rserver "${@}"
%apphelp rserver
  RStudio Server. See run-help of this container for general usage information
  and rserver --help for a reference of all command line arguments

%apprun rstudio_passwd
  exec /usr/lib/rstudio-server/bin/rstudio_passwd "${@}"

%apphelp rstudio_passwd
  Save a password to access RStudio Server via the browser. Execute
  `rstudio_passwd --help` for more information.

%apprun help_ldap_auth
  exec /usr/lib/rstudio-server-bin/ldap_auth --help
%apphelp help_ldap_auth
  Further information on how to use the LDAP authentication with RStudio
  Server.

%runscript
  exec rserver "${@}"

%environment
  export PATH=/usr/lib/rstudio-server/bin:${PATH}

%setup
  install -Dv \
    rstudio_auth.sh \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/rstudio_auth
  install -Dv \
    rstudio_auth_file.py \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/rstudio_auth_file
  install -Dv \
    ldap_auth.py \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/ldap_auth
  install -Dv \
    rstudio_passwd.py \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/rstudio_passwd
  install -Dv \
    find_port \
    ${SINGULARITY_ROOTFS}/usr/bin

%post
  # Software versions
  export RSTUDIO_VERSION=1.3.1056

  # Install RStudio Server
  apt-get update
  apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    gdebi-core
  wget \
    --no-verbose \
    -O rstudio-server.deb \
    "https://download2.rstudio.org/server/bionic/amd64/rstudio-server-${RSTUDIO_VERSION}-amd64.deb"
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

  apt-get install -y libxml2-dev git

  # Do not let OpenBLAS launch a thread per core, that exhausts resource
  # limits when running many workers on machines with many cores
  # RStudio server does not honor environment variables, so I need to
  # set it here in addition to the environment variable already present in the
  # base image.
  echo "OMP_NUM_THREADS=1" >> /etc/R/Renviron.site

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [mlell/singularity-rstudio](https://github.com/mlell/singularity-rstudio)
 - License: [Other](None)

