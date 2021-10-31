---
id: 10667
name: "pvrqualitasag/quagzws-sidef"
branch: "master"
tag: "latest"
commit: "5bd428c5d0d95443140e7149f028615768f502eb"
version: "3bf70b1de93e644be1b6fb2dbfff97b0"
build_date: "2020-09-03T08:33:32.236Z"
size_mb: 3209.0
size: 1505898527
sif: "https://datasets.datalad.org/shub/pvrqualitasag/quagzws-sidef/latest/2020-09-03-5bd428c5-3bf70b1d/3bf70b1de93e644be1b6fb2dbfff97b0.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/pvrqualitasag/quagzws-sidef/latest/2020-09-03-5bd428c5-3bf70b1d/
recipe: https://datasets.datalad.org/shub/pvrqualitasag/quagzws-sidef/latest/2020-09-03-5bd428c5-3bf70b1d/Singularity
collection: pvrqualitasag/quagzws-sidef
---

# pvrqualitasag/quagzws-sidef:latest

```bash
$ singularity pull shub://pvrqualitasag/quagzws-sidef:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/

%post
  sed -i 's/main/main restricted universe/g' /etc/apt/sources.list
  apt-get update

  # install softwaree properties commons for add-apt-repository
  apt-get install -y software-properties-common apt-utils
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 
  add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'
  apt-get update

  # Install libraries and other pre-requisites
  apt-get install -y build-essential xserver-xorg-dev freeglut3 freeglut3-dev libopenmpi-dev openmpi-bin openmpi-common openssh-client openssh-server libssh-dev libgit2-dev libssl-dev libxml2-dev libfreetype6-dev libmagick++-dev ftp screen curl man vim less locales time rsync gawk sudo tzdata git ssmtp mailutils cargo dos2unix doxygen wget sshpass htop nano
  apt-get update

  # Install R, Python, pandas and gnuplot
  apt-get install -y r-base r-base-core r-recommended python python-pip python-numpy python-pandas python-dev python3-pip pandoc gnuplot 
  apt-get update
  

  # Install jula from git
  curl -sSL "https://julialang-s3.julialang.org/bin/linux/x64/1.1/julia-1.1.1-linux-x86_64.tar.gz" > julia.tar.gz 
  mkdir -p /opt/julia 
  tar -C /opt/julia -zxf julia.tar.gz 
  rm -f julia.tar.gz

  # install OpenJDK 8 (LTS) from https://adoptopenjdk.net
  curl -sSL "https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u222-b10/OpenJDK8U-jdk_x64_linux_hotspot_8u222b10.tar.gz" > openjdk8.tar.gz
  mkdir -p /opt/openjdk
  tar -C /opt/openjdk -xf openjdk8.tar.gz
  rm -f openjdk8.tar.gz

  # numpy and pandas for py3
  /usr/bin/pip3 install pandas
  /usr/bin/pip3 install numpy

  # dconf and gnuplot problem
  mkdir -p /run/user/501
  chmod -R 777 /run/user
  
  # locales
  locale-gen en_US.UTF-8
  locale-gen de_CH.UTF-8

  # timezone
  echo 'Europe/Berlin' > /etc/timezone

  # hostname
  echo '1-htz.quagzws.com' > /etc/hostname

%environment
  export PATH=${PATH}:/opt/openjdk/jdk8u222-b10/bin:/qualstorzws01/data_projekte/linuxBin
  export TZ=$(cat /etc/timezone)
```

## Collection

 - Name: [pvrqualitasag/quagzws-sidef](https://github.com/pvrqualitasag/quagzws-sidef)
 - License: None

