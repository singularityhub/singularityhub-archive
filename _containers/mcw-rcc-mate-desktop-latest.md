---
id: 6280
name: "mcw-rcc/mate-desktop"
branch: "master"
tag: "latest"
commit: "f979dc5d2324d18d39153d4f03261c575cde9ef7"
version: "dc435b808003f427d3b7c07b285a17bc"
build_date: "2020-06-04T14:10:26.586Z"
size_mb: 2581
size: 933707807
sif: "https://datasets.datalad.org/shub/mcw-rcc/mate-desktop/latest/2020-06-04-f979dc5d-dc435b80/dc435b808003f427d3b7c07b285a17bc.simg"
url: https://datasets.datalad.org/shub/mcw-rcc/mate-desktop/latest/2020-06-04-f979dc5d-dc435b80/
recipe: https://datasets.datalad.org/shub/mcw-rcc/mate-desktop/latest/2020-06-04-f979dc5d-dc435b80/Singularity
collection: mcw-rcc/mate-desktop
---

# mcw-rcc/mate-desktop:latest

```bash
$ singularity pull shub://mcw-rcc/mate-desktop:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:centos7

%labels
  Maintainer Matthew Flister

%help
  This container runs the MATE desktop in CentOS 7.

%apprun vncserver
  exec vncserver "${@}"

%apprun vncpasswd
  exec vncpasswd "${@}"

%apprun websockify
  exec /opt/websockify/run "${@}"

%apprun mate-session
  exec mate-session "${@}"

%environment
  export PATH=/opt/TurboVNC/bin:${PATH}

%post
  # add paths
  mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/depts /rcc/stor1/projects
  
  # Software versions
  export TURBOVNC_VERSION=2.2.1
  export WEBSOCKIFY_VERSION=0.8.0

  # Get dependencies
  yum update -y && yum upgrade -y
  yum install -y epel-release
  yum groupinstall -y "X Window System" 
  yum groupinstall -y "MATE Desktop"
  yum install -y \
    less \
    wget \
    vim 
  
  dbus-uuidgen > /etc/machine-id
  
  # Install TurboVNC https://sourceforge.net/projects/turbovnc/files/2.2.1/turbovnc-2.2.1.x86_64.rpm/download
  wget https://sourceforge.net/projects/turbovnc/files/${TURBOVNC_VERSION}/turbovnc-${TURBOVNC_VERSION}.x86_64.rpm -q
  yum install -y turbovnc-${TURBOVNC_VERSION}.x86_64.rpm
  rm -rf turbovnc-${TURBOVNC_VERSION}.x86_64.rpm

  # Install websockify
  yum install -y \
    python \
    numpy
  mkdir -p /opt/websockify
  wget https://github.com/novnc/websockify/archive/v${WEBSOCKIFY_VERSION}.tar.gz -q -O - | tar xzf - -C /opt/websockify --strip-components=1
  rm -rf v*.tar.gz
```

## Collection

 - Name: [mcw-rcc/mate-desktop](https://github.com/mcw-rcc/mate-desktop)
 - License: None

