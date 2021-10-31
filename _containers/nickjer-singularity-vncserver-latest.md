---
id: 1735
name: "nickjer/singularity-vncserver"
branch: "master"
tag: "latest"
commit: "59bfc1574f3a2e2a2d2cdf10d808d2ac196dbcb6"
version: "5bb709650266421aa3e414d39c2cfbe5"
build_date: "2021-03-04T01:01:36.591Z"
size_mb: 196
size: 74645535
sif: "https://datasets.datalad.org/shub/nickjer/singularity-vncserver/latest/2021-03-04-59bfc157-5bb70965/5bb709650266421aa3e414d39c2cfbe5.simg"
url: https://datasets.datalad.org/shub/nickjer/singularity-vncserver/latest/2021-03-04-59bfc157-5bb70965/
recipe: https://datasets.datalad.org/shub/nickjer/singularity-vncserver/latest/2021-03-04-59bfc157-5bb70965/Singularity
collection: nickjer/singularity-vncserver
---

# nickjer/singularity-vncserver:latest

```bash
$ singularity pull shub://nickjer/singularity-vncserver:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels
  Maintainer Jeremy Nicklas
  TurboVNC_Version 2.1.2

%apprun vncserver
  exec vncserver "${@}"

%apprun vncpasswd
  exec vncpasswd "${@}"

%apprun websockify
  exec /opt/websockify/run "${@}"

%runscript
  exec vncserver "${@}"

%environment
  export PATH=/opt/TurboVNC/bin:${PATH}

%post
  # Software versions
  export TURBOVNC_VERSION=2.1.2

  # Get dependencies
  apt-get update
  apt-get install -y --no-install-recommends \
    locales \
    wget \
    ca-certificates \
    xauth \
    xfonts-base \
    xkb-data \
    x11-xkb-utils

  # Configure default locale
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
  locale-gen en_US.utf8
  /usr/sbin/update-locale LANG=en_US.UTF-8
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8

  # Install TurboVNC
  wget https://sourceforge.net/projects/turbovnc/files/${TURBOVNC_VERSION}/turbovnc_${TURBOVNC_VERSION}_amd64.deb -q
  dpkg -i turbovnc_${TURBOVNC_VERSION}_amd64.deb
  rm turbovnc_${TURBOVNC_VERSION}_amd64.deb

  # Install websockify
  apt-get update
  apt-get install -y --no-install-recommends \
    python \
    python-numpy
  mkdir -p /opt/websockify
  wget https://github.com/novnc/websockify/archive/master.tar.gz -q -O - | tar xzf - -C /opt/websockify --strip-components=1

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [nickjer/singularity-vncserver](https://github.com/nickjer/singularity-vncserver)
 - License: [MIT License](https://api.github.com/licenses/mit)

