---
id: 3077
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "mummer_4.0.0beta2"
commit: "7715562a737b38b78f43a745654e5c6d6b9a9c6e"
version: "648fb9018fdc44febf1361010f2aab46"
build_date: "2020-06-04T02:45:33.509Z"
size_mb: 953
size: 368291871
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/mummer_4.0.0beta2/2020-06-04-7715562a-648fb901/648fb9018fdc44febf1361010f2aab46.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/mummer_4.0.0beta2/2020-06-04-7715562a-648fb901/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/mummer_4.0.0beta2/2020-06-04-7715562a-648fb901/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:mummer_4.0.0beta2

```bash
$ singularity pull shub://TomHarrop/singularity-containers:mummer_4.0.0beta2
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: build-essential language-pack-en software-properties-common wget

%help

    Container for mummer 4.0.0beta2
    https://github.com/mummer4/mummer/releases

%labels

    MAINTAINER "Tom Harrop"
    VERSION "mummer 4.0.0beta2"

%runscript

    exec mummer "$@"

%post

    # add apt repos
    add-apt-repository \
        "deb http://archive.ubuntu.com/ubuntu bionic main universe restricted multiverse"
    add-apt-repository \
        "deb http://archive.canonical.com/ubuntu bionic partner"
    apt update

    # install apt packages
    apt install -y \
        fig2dev \
        gnuplot \
        xfig

    # build mummer
    wget -O "mummer.tar.gz" \
        --no-check-certificate \
        https://github.com/mummer4/mummer/releases/download/v4.0.0beta2/mummer-4.0.0beta2.tar.gz
    mkdir mummer-install
    tar -zxf mummer.tar.gz \
        -C mummer-install \
        --strip-components 1
    cd mummer-install || exit 1
    ./configure && make && make install
    cd .. || exit 1
    rm -rf mummer.tar.gz mummer-install

    # rebuild libraries
    ldconfig
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

