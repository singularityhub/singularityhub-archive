---
id: 7893
name: "ebothmann/sherpa-singularity"
branch: "master"
tag: "sherpa-rel-2-2-7_68ab0c9c5_caesar"
commit: "a3a9ccd9c80b8bdb4d9b76ce0341d7ff84ea7c9e"
version: "23357766fc4b47574fb01fdc4f52bd70"
build_date: "2019-03-22T14:10:54.744Z"
size_mb: 3582
size: 804380703
sif: "https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/sherpa-rel-2-2-7_68ab0c9c5_caesar/2019-03-22-a3a9ccd9-23357766/23357766fc4b47574fb01fdc4f52bd70.simg"
url: https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/sherpa-rel-2-2-7_68ab0c9c5_caesar/2019-03-22-a3a9ccd9-23357766/
recipe: https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/sherpa-rel-2-2-7_68ab0c9c5_caesar/2019-03-22-a3a9ccd9-23357766/Singularity
collection: ebothmann/sherpa-singularity
---

# ebothmann/sherpa-singularity:sherpa-rel-2-2-7_68ab0c9c5_caesar

```bash
$ singularity pull shub://ebothmann/sherpa-singularity:sherpa-rel-2-2-7_68ab0c9c5_caesar
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ebothmann/sherpa-singularity:mceg


%help
A Singularity file to define an image for running Sherpa rel-2-2-7@68ab0c9c
(called "Caesar" here to aid the memory when having many such images laying
around) including support for FastJet, HepMC2, LHAPDF, Rivet, OpenLoops and
BlackHat.


%labels
    Maintainer Enrico Bothmann
    Version v0.1


%runscript
    Sherpa "$@"


%post
    echo Installing yum dependencies ...
    yum install -y texinfo

    echo Installing Sherpa
    mkdir /scratch
    cd /scratch
    git clone --branch rel-2-2-7 https://gitlab.com/sherpa-team/sherpa.git
    cd sherpa
    git reset --hard 68ab0c9c5459d2c4ebc463d04388eefb9493bb24
    autoreconf -i
    ./configure \
        --prefix=/usr/local \
        --enable-analysis \
        --enable-blackhat=/opt/blackhat-r3095 \
        --enable-fastjet=/usr/local \
        --enable-hepmc2=/usr/local \
        --enable-lhapdf=/usr/local \
        --enable-openloops=/opt/OpenLoops-2.0.0 \
        --enable-rivet=/usr/local \
        --with-sqlite3=install \
        CXXFLAGS="-O3 --std=c++11"
    make -j
    make install

    cd /
    rm -rf /scratch
    ldconfig
    yum erase -y texinfo perl-Text-Unidecode perl-libintl
    yum clean all
```

## Collection

 - Name: [ebothmann/sherpa-singularity](https://github.com/ebothmann/sherpa-singularity)
 - License: None

