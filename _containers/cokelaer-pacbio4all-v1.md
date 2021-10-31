---
id: 578
name: "cokelaer/pacbio4all"
branch: "master"
tag: "v1"
commit: "1393bd6d318ef79dfac95f62c6e31d1f84b94b06"
version: "866e57ac4576c6d4aadbb991d7c8e460"
build_date: "2017-10-27T19:22:10.259Z"
size_mb: 2180
size: 855687199
sif: "https://datasets.datalad.org/shub/cokelaer/pacbio4all/v1/2017-10-27-1393bd6d-866e57ac/866e57ac4576c6d4aadbb991d7c8e460.simg"
url: https://datasets.datalad.org/shub/cokelaer/pacbio4all/v1/2017-10-27-1393bd6d-866e57ac/
recipe: https://datasets.datalad.org/shub/cokelaer/pacbio4all/v1/2017-10-27-1393bd6d-866e57ac/Singularity
collection: cokelaer/pacbio4all
---

# cokelaer/pacbio4all:v1

```bash
$ singularity pull shub://cokelaer/pacbio4all:v1
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:17.04

#DistType "debian"
#MirrorURL: http://us.archive.ubuntu.com/ubuntu/
#OSVersion: xenial-updates

%labels

    AUTHOR thomas.cokelaer@pasteur.fr
    VERSION v1.0

%runscript

   echo "Welcome to Pacbio-dedicated container "
   echo "(maintainer: thomas cokelaer, Institut Pasteur 2017-)"
   echo "Available tools: blasr, bax2bam, pbbam, hmmer, gmap, ..."
   echo "Usage: singularity exec pacbio.img samtools"

%help

    This container contains a bunch of executables related to pacbio analysis.
    You can enter the conatiner as follows:

       singularity shell name.img

    Executables are are stored in /usr/local/bin



%post

    apt-get -y update
    apt-get install -y wget
    apt-get install -y bzip2
    apt-get install -y vim
    apt-get install -y git
    apt-get install -y make gcc python g++ gfortran pkg-config
    apt-get install -y libfreetype6*
    #apt-get install -y libstdc++
    apt-get install -y graphviz

    git clone https://github.com/PacificBiosciences/pitchfork.git
    cd pitchfork
    git reset --hard b7bdf01f12bbd43977f140923b0144d75c863348

    export TMPBUILD=/usr/local/
    make PREFIX=$TMPBUILD samtools
    make PREFIX=$TMPBUILD blasr   # installs boost,zlib,bzip2,htslib
    make PREFIX=$TMPBUILD bax2bam
    # make PREFIX=/tmp/mybuild bam2bax
    make PREFIX=$TMPBUILD pbbam
    make PREFIX=$TMPBUILD bam2fastx
    make PREFIX=$TMPBUILD bamtools
    make PREFIX=$TMPBUILD hmmer
    make PREFIX=$TMPBUILD isoseq-core
    make PREFIX=$TMPBUILD gmap
    make PREFIX=$TMPBUILD falcon
    make PREFIX=$TMPBUILD world  # this should install many more packages
    # sbt and jre cannot be installed

    #
    #cp -r $TMPBUILD/* /usr/local/
    export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
    export PATH=/usr/local/bin:$PATH

    if [ ! -d /data ]; then mkdir /data; fi
    if [ ! -d /scripts ]; then mkdir /scripts; fi
    if [ ! -d /scratch ]; then mkdir /scratch; fi
    if [ ! -d /mounting ]; then mkdir /mounting; fi
    if [ ! -d /pasteur ]; then mkdir /pasteur; fi

    # What can be cleaned ?
    rm -rf staging
    rm -rf workspace
    rm -rf distfile


%environment
    export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
    export PATH=/usr/local/bin:$PATH
```

## Collection

 - Name: [cokelaer/pacbio4all](https://github.com/cokelaer/pacbio4all)
 - License: None

