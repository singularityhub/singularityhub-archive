---
id: 7298
name: "xiaozhah/WineSingularity"
branch: "master"
tag: "latest"
commit: "8e9ed0f9aba3c9aa6dead45ed1e945913b6c6601"
version: "4c46b24cd57a1af0621cf66fc1456495"
build_date: "2019-11-18T10:57:17.058Z"
size_mb: 2797
size: 371965983
sif: "https://datasets.datalad.org/shub/xiaozhah/WineSingularity/latest/2019-11-18-8e9ed0f9-4c46b24c/4c46b24cd57a1af0621cf66fc1456495.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/xiaozhah/WineSingularity/latest/2019-11-18-8e9ed0f9-4c46b24c/
recipe: https://datasets.datalad.org/shub/xiaozhah/WineSingularity/latest/2019-11-18-8e9ed0f9-4c46b24c/Singularity
collection: xiaozhah/WineSingularity
---

# xiaozhah/WineSingularity:latest

```bash
$ singularity pull shub://xiaozhah/WineSingularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04
 
%labels
  Author Zhou Xiao
  Version v1.0.5
  wine_Version 4.0
  build_date 2019 Feb 18

%runscript
  echo "Hello from the Wine container!"

%environment
  export LC_ALL=C
  export WINEDEBUG=fixme-all

%post
  apt-get update
  apt-get upgrade -y
  apt-get install -y tmux htop ranger tree nmon dstat ncdu python-pip wget zip unzip nano
  apt-get install -y xz-utils g++ gcc bison flex xvfb make cabextract software-properties-common gnupg libpng-dev libpng16-16
  apt-get autoclean
 
  cd /tmp
  wget https://dl.winehq.org/wine/source/4.0/wine-4.0.tar.xz
  tar -xvf wine-4.0.tar.xz && cd wine-4.0
  mkdir wine64-build && cd wine64-build
  ../configure --enable-win64 --without-x --without-freetype
  make && make install
  ln -s /usr/local/bin/wine64 /usr/local/bin/wine
  
  # Print wine information
  file `which wine64`

%help
    This is a wine container in Ubuntu 18.04 from Singularity!
```

## Collection

 - Name: [xiaozhah/WineSingularity](https://github.com/xiaozhah/WineSingularity)
 - License: None

