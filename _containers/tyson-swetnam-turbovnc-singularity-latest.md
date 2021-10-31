---
id: 3853
name: "tyson-swetnam/turbovnc-singularity"
branch: "master"
tag: "latest"
commit: "41c519282372bb83b84793456b0ab8e88f7824d7"
version: "f9a919624d227a88f391a1eb022d9162"
build_date: "2021-04-13T13:42:29.693Z"
size_mb: 1591
size: 610136095
sif: "https://datasets.datalad.org/shub/tyson-swetnam/turbovnc-singularity/latest/2021-04-13-41c51928-f9a91962/f9a919624d227a88f391a1eb022d9162.simg"
url: https://datasets.datalad.org/shub/tyson-swetnam/turbovnc-singularity/latest/2021-04-13-41c51928-f9a91962/
recipe: https://datasets.datalad.org/shub/tyson-swetnam/turbovnc-singularity/latest/2021-04-13-41c51928-f9a91962/Singularity
collection: tyson-swetnam/turbovnc-singularity
---

# tyson-swetnam/turbovnc-singularity:latest

```bash
$ singularity pull shub://tyson-swetnam/turbovnc-singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/opengl:1.0-glvnd-runtime-ubuntu16.04

%labels
  Maintainer Tyson Lee Swetnam
  TurboVNC-NVIDIA

%apprun vncserver
  exec vncserver "${@}"

%apprun vncpasswd
  exec vncpasswd "${@}"

%apprun websockify
  exec /opt/websockify/run "${@}"

%runscript
  exec vncserver "${@}"

%environment
  export PATH=/opt/TurboVNC/bin:/opt/VirtualGL/bin:${PATH}

%post
  # Software versions
  export TURBOVNC_VERSION=2.1.2
  export VIRTUALGL_VERSION=2.5.2
  export LIBJPEG_VERSION=1.5.2

  # Get dependencies
  apt-get update
  apt-get install -y --no-install-recommends \
    emacs \
    vim \
    nano \
    lshw \
    lsb-release \
    bash-completion \
    kmod \
    iputils-ping \
    net-tools \
    ca-certificates \
    locales \
    curl \
    gcc \
    make \
    wget \
    ca-certificates \
    xauth \
    xfonts-base \
    xkb-data \
    x11-xkb-utils \
    xorg \
    openbox \
    libc6-dev \
    libxv1 \
    libxv1:i386 \
    mesa-utils \
    mesa-utils-extra \
    x11-apps \
    dbus-x11 \
    libglib2.0-tests \
    git \
    libxcb-keysyms1-dev \
    apt-transport-https

  # XFCE4 Desktop
  apt-get install -y --no-install-recommends \
    build-essential \
    software-properties-common \
    glib-2.0-dev \
    libgtk2.0-dev \
    libxfce4ui-1-dev \
    xfce4 \
    gtk3-engines-xfce \
    xfce4-notifyd \
    xfce4-taskmanager \
    xfce4-terminal \
    libgtk-3-bin
  add-apt-repository ppa:rebuntu16/other-stuff 
  apt-get update
  apt-get install -y xfce-theme-manager
  

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
 
  # Install VirtualGL 
  wget https://svwh.dl.sourceforge.net/project/libjpeg-turbo/${LIBJPEG_VERSION}/libjpeg-turbo-official_${LIBJPEG_VERSION}_amd64.deb 
  wget https://svwh.dl.sourceforge.net/project/virtualgl/${VIRTUALGL_VERSION}/virtualgl_${VIRTUALGL_VERSION}_amd64.deb 
  wget https://svwh.dl.sourceforge.net/project/virtualgl/${VIRTUALGL_VERSION}/virtualgl32_${VIRTUALGL_VERSION}_amd64.deb 
  dpkg -i libjpeg-turbo-official_${LIBJPEG_VERSION}_amd64.deb
  dpkg -i virtualgl_${VIRTUALGL_VERSION}_amd64.deb
  dpkg -i virtualgl32_${VIRTUALGL_VERSION}_amd64.deb
  rm -f *.deb
  
  # Install noVNC
  cd /opt
  git clone https://github.com/novnc/noVNC/

  # Install websockify
  apt-get update
  apt-get install -y --no-install-recommends \
    python \
    python-numpy
  mkdir -p /opt/websockify
  wget https://github.com/novnc/websockify/archive/master.tar.gz -q -O - | tar xzf - -C /opt/websockify --strip-components=1
  
# Install Java 8
  apt-get update && apt-get install -y --no-install-recommends \
    libgtk2.0-0:i386 libsm6:i386 \
    python-software-properties \
    default-jre default-jdk
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
  add-apt-repository -y ppa:webupd8team/java
  apt-get update
  apt-get install -y oracle-java8-installer
  rm -rf /var/lib/apt/lists/*
  rm -rf /var/cache/oracle-jdk8-installer
  # apt-get install -y openjfx
  
  # Install a couple monitoring tools
  # apt-get install -y htop tmux
  
  # in-container bind points for shared filesystems
  mkdir -p /extra /xdisk /uaopt /cm/shared /rsgrps

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [tyson-swetnam/turbovnc-singularity](https://github.com/tyson-swetnam/turbovnc-singularity)
 - License: None

