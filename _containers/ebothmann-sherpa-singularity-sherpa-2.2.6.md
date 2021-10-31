---
id: 7558
name: "ebothmann/sherpa-singularity"
branch: "master"
tag: "sherpa-2.2.6"
commit: "5ef41abf41b1977bf13a875aba63b80f8acfad3d"
version: "5fc642c00b456574ec4c53bb26c3b81c"
build_date: "2019-03-01T19:49:13.735Z"
size_mb: 3529
size: 796880927
sif: "https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/sherpa-2.2.6/2019-03-01-5ef41abf-5fc642c0/5fc642c00b456574ec4c53bb26c3b81c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ebothmann/sherpa-singularity/sherpa-2.2.6/2019-03-01-5ef41abf-5fc642c0/
recipe: https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/sherpa-2.2.6/2019-03-01-5ef41abf-5fc642c0/Singularity
collection: ebothmann/sherpa-singularity
---

# ebothmann/sherpa-singularity:sherpa-2.2.6

```bash
$ singularity pull shub://ebothmann/sherpa-singularity:sherpa-2.2.6
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ebothmann/sherpa-singularity:mceg


%help
A Singularity file to define an image for running Sherpa 2.2.6
including support for FastJet, HepMC2, LHAPDF, Rivet, OpenLoops and
BlackHat.


%labels
    Maintainer Enrico Bothmann
    Version v0.1


%runscript
    Sherpa "$@"


%post
    echo Installing Sherpa
    mkdir /scratch
    cd /scratch
    wget https://sherpa.hepforge.org/downloads/?f=SHERPA-MC-2.2.6.tar.gz -O- | tar xz
    cd SHERPA-MC-2.2.6
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
    make -j && make install

    cd /
    rm -rf /scratch
    ldconfig
```

## Collection

 - Name: [ebothmann/sherpa-singularity](https://github.com/ebothmann/sherpa-singularity)
 - License: None

