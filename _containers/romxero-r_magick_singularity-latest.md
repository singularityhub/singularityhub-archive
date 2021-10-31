---
id: 15919
name: "romxero/r_magick_singularity"
branch: "main"
tag: "latest"
commit: "883fe97735bf6241a90b28ed6ecc5232d3a12a6c"
version: "40b1b6fb38a460afe134d8edd48ec62872516b095ba686571782139a91354b6c"
build_date: "2021-04-20T00:06:35.461Z"
size_mb: 738.25390625
size: 774115328
sif: "https://datasets.datalad.org/shub/romxero/r_magick_singularity/latest/2021-04-20-883fe977-40b1b6fb/40b1b6fb38a460afe134d8edd48ec62872516b095ba686571782139a91354b6c.sif"
url: https://datasets.datalad.org/shub/romxero/r_magick_singularity/latest/2021-04-20-883fe977-40b1b6fb/
recipe: https://datasets.datalad.org/shub/romxero/r_magick_singularity/latest/2021-04-20-883fe977-40b1b6fb/Singularity
collection: romxero/r_magick_singularity
---

# romxero/r_magick_singularity:latest

```bash
$ singularity pull shub://romxero/r_magick_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Author "Randall Cab White - rcwhite@stanford.edu"


#############
#%setup
############

#Downlaod packages
%post
  apt-get -ym update
    ln -fs /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
    apt-get install -y tzdata
    dpkg-reconfigure --frontend noninteractive tzdata


          apt-get -ymq install wget libatlas3-base curl make tar gzip gfortran gcc g++ git cmake build-essential libreadline-dev libx11-dev libxt-dev libbz2-dev liblzma-dev \
          ca-certificates libcairo2 unzip zip libtcl8.6 ucf libtk8.6 libpcre3-dev libpcre++-dev libcurl4-openssl-dev  autotools-dev  automake autoconf autogen pkg-config libgtk-3-dev sqlite3 libsqlite3-dev libudunits2-dev \
           software-properties-common build-essential ca-certificates \
            git make cmake wget unzip libtool automake \
            zlib1g-dev libsqlite3-dev pkg-config sqlite3 \
            libcharls-dev libopenjp2-7-dev libcairo2-dev \

  apt-get -ymq install wget libatlas3-base curl make tar gzip default-jdk default-jre build-essential imagemagick libmagick++-dev git-all libssl-dev libpcre2-dev
  cd /
  wget https://cran.r-project.org/src/base/R-4/R-4.0.2.tar.gz
  tar zxvf R-4.0.2.tar.gz
  cd R*
  ./configure
  make -j4
  make install
  make clean
%environment
  export IMAGE_NAME="gcc"
#%runscript
#       /firefox/firefox-bin


#
```

## Collection

 - Name: [romxero/r_magick_singularity](https://github.com/romxero/r_magick_singularity)
 - License: None

