---
id: 7593
name: "ebothmann/sherpa-singularity"
branch: "master"
tag: "sherpa-rel-2-2-7_12338b5d_bossix"
commit: "7db59d2ce8facf56b012f1ccdc281617fac8e2d8"
version: "cc2379246e024246822263655b95fe72"
build_date: "2019-03-06T12:46:33.877Z"
size_mb: 3530
size: 797069343
sif: "https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/sherpa-rel-2-2-7_12338b5d_bossix/2019-03-06-7db59d2c-cc237924/cc2379246e024246822263655b95fe72.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ebothmann/sherpa-singularity/sherpa-rel-2-2-7_12338b5d_bossix/2019-03-06-7db59d2c-cc237924/
recipe: https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/sherpa-rel-2-2-7_12338b5d_bossix/2019-03-06-7db59d2c-cc237924/Singularity
collection: ebothmann/sherpa-singularity
---

# ebothmann/sherpa-singularity:sherpa-rel-2-2-7_12338b5d_bossix

```bash
$ singularity pull shub://ebothmann/sherpa-singularity:sherpa-rel-2-2-7_12338b5d_bossix
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ebothmann/sherpa-singularity:mceg


%help
A Singularity file to define an image for running Sherpa rel-2-2-7@12338b5d
(called "Bossix" here to aid the memory when having many such images laying
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
    git reset --hard 12338b5d86b5c837925f98f4a182aae02131dd6a
    autoreconf -i
    ./configure \
        --prefix=/usr/local \
        --enable-analysis \
        --enable-blackhat=/opt/blackhat-r3095 \
        --enable-fastjet=/usr/local \
        --enable-hepmc2=/usr/local \
        --enable-lhapdf=/usr/local \
        --enable-openloops=/opt/OpenLoops-1.3.1 \
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

