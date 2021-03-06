---
id: 787
name: "cokelaer/pacbio4all"
branch: "master"
tag: "v3"
commit: "a967142034928fbb13f407ff515fd5f041009278"
version: "d655c338bdd306ffe809367a99baee7d"
build_date: "2017-11-16T10:30:37.444Z"
size_mb: 2187
size: 855851039
sif: "https://datasets.datalad.org/shub/cokelaer/pacbio4all/v3/2017-11-16-a9671420-d655c338/d655c338bdd306ffe809367a99baee7d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cokelaer/pacbio4all/v3/2017-11-16-a9671420-d655c338/
recipe: https://datasets.datalad.org/shub/cokelaer/pacbio4all/v3/2017-11-16-a9671420-d655c338/Singularity
collection: cokelaer/pacbio4all
---

# cokelaer/pacbio4all:v3

```bash
$ singularity pull shub://cokelaer/pacbio4all:v3
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:17.04

# We use 17.04 to have the correct gcc compiler for some of the compilation 
# e.g. ppbam
#DistType "debian"
#MirrorURL: http://us.archive.ubuntu.com/ubuntu/
#OSVersion: xenial-updates

%labels

    AUTHOR thomas.cokelaer@pasteur.fr
    VERSION v1.0

%help

    Welcome to Pacbio-dedicated container

    (maintainer: thomas cokelaer, Institut Pasteur 2017-)
    (https://github.com/cokelaer/pacbio4all)

    Available tools: blasr, bax2bam, pbbam, hmmer, gmap, ...
    Usage: singularity exec pacbio.img samtools

    This container contains a bunch of executables related to pacbio analysis.
    You can enter the container as follows:

       singularity shell name.img

    Executables are stored in /usr/local/bin

    Or you can execute it using (for example to run blasr):

        singularity run name.img blasr

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
    # 14Nov2017
    #git reset --hard a8fe31e731ae1795c626e9f3b5c8fec4f050c5d2

    export TMPBUILD=/usr/local/
    make PREFIX=$TMPBUILD samtools
    make PREFIX=$TMPBUILD blasr   # installs boost,zlib,bzip2,htslib
    make PREFIX=$TMPBUILD bax2bam
    # make PREFIX=/tmp/mybuild bam2bax
    make PREFIX=$TMPBUILD pbh5tools
    make PREFIX=$TMPBUILD pbbam
    make PREFIX=$TMPBUILD bam2fastx
    make PREFIX=$TMPBUILD bamtools
    make PREFIX=$TMPBUILD hmmer
    make PREFIX=$TMPBUILD isoseq-core
    make PREFIX=$TMPBUILD gmap
    make PREFIX=$TMPBUILD falcon
    make PREFIX=$TMPBUILD world  # this should install many more packages
    # sbt and jre cannot be installed
    make PREFIX=$TMPBUILD pbreports
    make PREFIX=$TMPBUILD pbcommand

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

%runscript
    echo "Welcome to Pacbio-dedicated container"
    echo "Author: Thomas Cokelaer, http://github.com/cokelaer/pacbio4all"
    exec "$@"
```

## Collection

 - Name: [cokelaer/pacbio4all](https://github.com/cokelaer/pacbio4all)
 - License: None

