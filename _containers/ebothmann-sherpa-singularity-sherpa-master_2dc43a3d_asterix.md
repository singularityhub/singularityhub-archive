---
id: 7557
name: "ebothmann/sherpa-singularity"
branch: "master"
tag: "sherpa-master_2dc43a3d_asterix"
commit: "25d5122e5d68784e678d87eadd64db3950f4ca46"
version: "6fffefb953b7a268ea1f93252e86019d"
build_date: "2019-03-07T01:18:17.350Z"
size_mb: 3715
size: 852926495
sif: "https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/sherpa-master_2dc43a3d_asterix/2019-03-07-25d5122e-6fffefb9/6fffefb953b7a268ea1f93252e86019d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ebothmann/sherpa-singularity/sherpa-master_2dc43a3d_asterix/2019-03-07-25d5122e-6fffefb9/
recipe: https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/sherpa-master_2dc43a3d_asterix/2019-03-07-25d5122e-6fffefb9/Singularity
collection: ebothmann/sherpa-singularity
---

# ebothmann/sherpa-singularity:sherpa-master_2dc43a3d_asterix

```bash
$ singularity pull shub://ebothmann/sherpa-singularity:sherpa-master_2dc43a3d_asterix
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ebothmann/sherpa-singularity:mceg


%help
A Singularity file to define an image for running Sherpa master@2dc43a3d
(called "Asterix" here to aid the memory when having many such images laying
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
    git clone https://gitlab.com/sherpa-team/sherpa.git
    cd sherpa
    git reset --hard 2dc43a3d31fcc821744ed8832bc692acd78dc848
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

