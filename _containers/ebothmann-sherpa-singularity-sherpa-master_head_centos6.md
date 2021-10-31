---
id: 8502
name: "ebothmann/sherpa-singularity"
branch: "master"
tag: "sherpa-master_head_centos6"
commit: "c35dabe5e0659c8b6fb253b4ca1b3a928df70958"
version: "31a7ed19588da285d4f0e1b644dd645a"
build_date: "2019-04-29T20:57:18.375Z"
size_mb: 4539
size: 854749215
sif: "https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/sherpa-master_head_centos6/2019-04-29-c35dabe5-31a7ed19/31a7ed19588da285d4f0e1b644dd645a.simg"
url: https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/sherpa-master_head_centos6/2019-04-29-c35dabe5-31a7ed19/
recipe: https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/sherpa-master_head_centos6/2019-04-29-c35dabe5-31a7ed19/Singularity
collection: ebothmann/sherpa-singularity
---

# ebothmann/sherpa-singularity:sherpa-master_head_centos6

```bash
$ singularity pull shub://ebothmann/sherpa-singularity:sherpa-master_head_centos6
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ebothmann/sherpa-singularity:mceg_centos6


%help
A Singularity file to define an image for running Sherpa master
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
    echo Installing yum dependencies ...
    yum install -y texinfo libtool

    # set up build environment
    source /opt/rh/devtoolset-6/enable
    source /opt/rh/python27/enable
    source /enable_OpenMPI
    export PATH="/usr/local/bin:$PATH"  # such that the custom autoconf is found first

    echo Installing Sherpa
    mkdir /scratch
    cd /scratch
    git clone --branch tmp-fix-kperp-x-y-rotation https://gitlab.com/sherpa-team/sherpa.git
    cd sherpa
    autoreconf -i
    ./configure \
        --prefix=/usr/local \
        --enable-analysis \
        --enable-blackhat=/opt/blackhat-r3095 \
        --enable-fastjet=/usr/local \
        --enable-gzip \
        --enable-hepmc2=/usr/local \
        --enable-lhapdf=/usr/local \
        --enable-mpi \
        --enable-openloops=/opt/OpenLoops-2.0.0 \
        --enable-rivet=/usr/local \
        --with-libzip=install \
        CXXFLAGS="-O3"
    make -j4
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

