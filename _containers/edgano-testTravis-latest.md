---
id: 4745
name: "edgano/testTravis"
branch: "master"
tag: "latest"
commit: "86156cf61f6caf62797693bf3e013070d3ae3f5e"
version: "9d2b11e0e558a20f47fad1d4b6d4715f"
build_date: "2018-09-10T20:28:05.699Z"
size_mb: 1095
size: 429301791
sif: "https://datasets.datalad.org/shub/edgano/testTravis/latest/2018-09-10-86156cf6-9d2b11e0/9d2b11e0e558a20f47fad1d4b6d4715f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/edgano/testTravis/latest/2018-09-10-86156cf6-9d2b11e0/
recipe: https://datasets.datalad.org/shub/edgano/testTravis/latest/2018-09-10-86156cf6-9d2b11e0/Singularity
collection: edgano/testTravis
---

# edgano/testTravis:latest

```bash
$ singularity pull shub://edgano/testTravis:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:debian:jessie

%labels
MAINTAINER E.GARRIGA

%environment
  CACHE_4_TCOFFEE='${TMPDIR:-/tmp}/.tcoffee/cache'
  LOCKDIR_4_TCOFFEE='${TMPDIR:-/tmp}/.tcoffee/lock'
  TMP_4_TCOFFEE='${TMPDIR:-/tmp}/.tcoffee/tmp'
  PYTHONPATH=$PYTHONPATH:/home/lib/python2.7/site-packages/

%post
  apt-get update
  apt-get install -y --no-install-recommends ed less vim-tiny wget git
  apt-get install -y --no-install-recommends python build-essential cmake curl libargtable2-0
  apt-get install -y --no-install-recommends python-biopython python-numpy ruby python-setuptools
  apt-get install -y --no-install-recommends default-jdk libpng-dev


##
# install argtable
##
  wget http://prdownloads.sourceforge.net/argtable/argtable2-13.tar.gz
  tar -zxf argtable2-13.tar.gz 
  cd argtable2-13
  ./configure
  make
  make install
  rm /argtable2-13.tar.gz
  cd /

##
# install clustal omega
##
  wget http://www.clustal.org/omega/clustal-omega-1.2.4.tar.gz
  tar -zxf clustal-omega-1.2.4.tar.gz
  cd clustal-omega-1.2.4
  ./configure
  make
  make install
  rm /clustal-omega-1.2.4.tar.gz
  cd /

##
# install mafft
##
  wget https://mafft.cbrc.jp/alignment/software/mafft-7.397-with-extensions-src.tgz
  tar xfvz mafft-7.397-with-extensions-src.tgz
  cd mafft-7.397-with-extensions/core/
  sed -i "s/PREFIX = \/usr\/local/PREFIX = \/mafft/g" Makefile 
  sed -i "s/BINDIR = \$(PREFIX)\/bin/BINDIR = \/mafft\/bin/g" Makefile
  make clean
  make
  make install
  wget http://mafft.cbrc.jp/alignment/software/newick2mafft.rb
  chmod +x newick2mafft.rb
  export "PATH=$PATH:/mafft/bin"
  export MAFFT_BINARIES=""
  cp /mafft/bin/* /bin/.
  mv /mafft-7.397-with-extensions /mafft
  rm /mafft-7.397-with-extensions-src.tgz
  cd /

    ##commit 7 sept d2fb394d980455bfd692519f9781d094836380c7 
      git clone https://github.com/cbcrg/tcoffee.git tcoffee380c7 
      cd tcoffee380c7 
      git checkout d2fb394d980455bfd692519f9781d094836380c7
      cd compile
      make t_coffee
      cp t_coffee /bin/t_coffee380c7 
      cd /
      rm -rf tcoffee380c7

    ##commit 7 sept 39e160bb6c4b1e041515f9f4e42e79b687f55572
      git clone https://github.com/cbcrg/tcoffee.git tcoffeef55572
      cd tcoffeef55572
      git checkout 39e160bb6c4b1e041515f9f4e42e79b687f55572
      cd compile
      make t_coffee
      cp t_coffee /bin/t_coffeef55572
      cd /
      rm -rf tcoffeef55572
      
      ##commit  15 jun    f5a3274df02cdbac8b6cd50bcb03d872a56e4a53
      git clone https://github.com/cbcrg/tcoffee.git tcoffee4a53
      cd tcoffee4a53
      git checkout f5a3274df02cdbac8b6cd50bcb03d872a56e4a53
      cd compile
      make t_coffee
      cp t_coffee /bin/t_coffee4a53
      cd /
      rm -rf tcoffee4a53

    ##commit 15 may 3c3d66e9797f32beaff56cf3d06522b8dd65460f 
      git clone https://github.com/cbcrg/tcoffee.git tcoffee5460f
      cd tcoffee5460f 
      git checkout 3c3d66e9797f32beaff56cf3d06522b8dd65460f 
      cd compile
      make t_coffee
      cp t_coffee /bin/t_coffee5460f
      cd /
      rm -rf tcoffee5460f

    ##commit  25 Jan    ddc7141dfb3bf6d34dd298a6a476aab2cd80cca9
      git clone https://github.com/cbcrg/tcoffee.git tcoffee0cca9
      cd tcoffee0cca9
      git checkout ddc7141dfb3bf6d34dd298a6a476aab2cd80cca9
      cd compile
      make t_coffee
      cp t_coffee /bin/t_coffee0cca9
      cd /
rm -rf tcoffee0cca9

##commit  25 Jan    1d198dbf88c07c3f3c2eaa97ec6e7ba7fe59f670
      git clone https://github.com/cbcrg/tcoffee.git tcoffeef670
      cd tcoffeef670
      git checkout 1d198dbf88c07c3f3c2eaa97ec6e7ba7fe59f670
      cd compile
      make t_coffee
      cp t_coffee /bin/t_coffeef670
      cd /
rm -rf t_coffeef670

      ##commit  25 Jan    43da1fff915641f98de4699c79b40f3d89f13fc9
      git clone https://github.com/cbcrg/tcoffee.git tcoffee3fc9
      cd tcoffee3fc9
      git checkout 43da1fff915641f98de4699c79b40f3d89f13fc9
      cd compile
      make t_coffee
      cp t_coffee /bin/t_coffee3fc9
      cd /
rm -rf tcoffee3fc9
    ##commit  20 Jan    dfe0a51f546ded3e08e384e21d24bab2854f8f8c
      git clone https://github.com/cbcrg/tcoffee.git tcoffee8f8c
      cd tcoffee8f8c
      git checkout dfe0a51f546ded3e08e384e21d24bab2854f8f8c
      cd compile
      make t_coffee
      cp t_coffee /bin/t_coffee8f8c
      cd /
      rm -rf tcoffee8f8c
```

## Collection

 - Name: [edgano/testTravis](https://github.com/edgano/testTravis)
 - License: None

