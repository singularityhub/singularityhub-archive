---
id: 8120
name: "ebothmann/sherpa-singularity"
branch: "master"
tag: "sherpa-2.2.6_centos6"
commit: "9ad55b8eddbb1c32e953a65b4c662e48d7e53522"
version: "c19f14138a55d0c52fca02e21463c286"
build_date: "2019-04-04T22:58:10.752Z"
size_mb: 2177
size: 539410463
sif: "https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/sherpa-2.2.6_centos6/2019-04-04-9ad55b8e-c19f1413/c19f14138a55d0c52fca02e21463c286.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ebothmann/sherpa-singularity/sherpa-2.2.6_centos6/2019-04-04-9ad55b8e-c19f1413/
recipe: https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/sherpa-2.2.6_centos6/2019-04-04-9ad55b8e-c19f1413/Singularity
collection: ebothmann/sherpa-singularity
---

# ebothmann/sherpa-singularity:sherpa-2.2.6_centos6

```bash
$ singularity pull shub://ebothmann/sherpa-singularity:sherpa-2.2.6_centos6
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ebothmann/sherpa-singularity:mceg_centos6


%help
A Singularity file to define an image for running Sherpa 2.2.6
including support for FastJet, HepMC2, LHAPDF, Rivet, OpenLoops and
BlackHat.


%labels
    Maintainer Enrico Bothmann
    Version v0.1


%runscript
    Sherpa "$@"


%files
    enable_OpenMPI


%post
    # set up build environment
    source /opt/rh/devtoolset-6/enable
    source /opt/rh/python27/enable
    source /enable_OpenMPI

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
        --enable-mpi \
        --enable-openloops=/opt/OpenLoops-2.0.0 \
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

