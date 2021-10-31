---
id: 10306
name: "theohartsook/Singularity"
branch: "master"
tag: "latest"
commit: "964ec86a74fe71cd07d7078e423e048041fda810"
version: "ba5979754cfd27cbf925859952e384842aa66540f6bbcad4f863cfc2563e0351"
build_date: "2019-10-23T17:39:13.103Z"
size_mb: 660.68359375
size: 692776960
sif: "https://datasets.datalad.org/shub/theohartsook/Singularity/latest/2019-10-23-964ec86a-ba597975/ba5979754cfd27cbf925859952e384842aa66540f6bbcad4f863cfc2563e0351.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/theohartsook/Singularity/latest/2019-10-23-964ec86a-ba597975/
recipe: https://datasets.datalad.org/shub/theohartsook/Singularity/latest/2019-10-23-964ec86a-ba597975/Singularity
collection: theohartsook/Singularity
---

# theohartsook/Singularity:latest

```bash
$ singularity pull shub://theohartsook/Singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: bash

##### Cloudcompare via WINE ##### 
# Singularity container developed by Jonathan Greenberg (jgreenberg@unr.edu)
# edited for CloudCompare

%environment
    PATH=$PATH:/APPS/CloudCompare/bin/
    export PATH

%post
  locale-gen en_US.UTF-8
  sed -i 's/main/main restricted universe/g' /etc/apt/sources.list
  echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a /etc/apt/sources.list
  gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
  gpg -a --export E084DAB9 | apt-key add -
  apt-get update

  # Install misc. utilities:
  apt-get install -y libopenblas-dev libcurl4-openssl-dev \
  libopenmpi-dev openmpi-bin openmpi-common openmpi-doc openssh-client openssh-server \
  libssh-dev wget vim git nano git cmake gfortran g++ curl wget python autoconf bzip2 \
  libtool libtool-bin libxml2-dev p7zip-full

  # wine:
  mkdir -p /APPS /PROFILES
  chmod 0777 /APPS /PROFILES
  dpkg --add-architecture i386
  apt-get update && apt-get -y install wget less vim software-properties-common python3-software-properties apt-transport-https winbind
  wget -nc https://dl.winehq.org/wine-builds/winehq.key
  apt-key add winehq.key
  apt-add-repository https://dl.winehq.org/wine-builds/ubuntu/
  apt-get update && apt-get install -y winehq-stable winetricks # this installs Wine2
  apt-get clean
  
  # CloudCompare
  # cd ~
  wget http://www.cloudcompare.org/release/CloudCompare_v2.11.alpha_bin_x64.7z
  7z x CloudCompare_v2.11.alpha_bin_x64.7z
  mv CloudCompare_v2.11.alpha_bin_x64 /APPS/
  chmod 775 -R /APPS/CloudCompare_v2.11.alpha_bin_x64
  
# CloudCompare shortcut:  
#basename=`basename CloudCompare .exe`
  echo '#!/bin/bash
WINEDEBUG=-all wine '/APPS/CloudCompare_v2.11.alpha_bin_x64/CloudCompare.exe -SILENT '"$@"' >> /usr/local/bin/cloudcompare.CloudCompare  
chmod 755 /usr/local/bin/cloudcompare.CloudCompare

%help
This container runs CloudCompare via an emulated Windows environment. A typical run would look like:
singularity exec /pathto/gearslaboratory-gears-singularity-master-gears-lastools.simg lasinfo -h
If you have a LASTools license, set it in your environment before running singularity using e.g.:
export LAStoolsLicenseFile=/pathto/lastoolslicense.txt
```

## Collection

 - Name: [theohartsook/Singularity](https://github.com/theohartsook/Singularity)
 - License: None

