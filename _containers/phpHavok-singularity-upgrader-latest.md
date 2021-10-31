---
id: 6259
name: "phpHavok/singularity-upgrader"
branch: "master"
tag: "latest"
commit: "e20e84020c9699cf31a63e4b437f139325512661"
version: "db30719ec9c9b6e23d7f861811d32447"
build_date: "2019-01-16T07:21:14.386Z"
size_mb: 1309
size: 519229471
sif: "https://datasets.datalad.org/shub/phpHavok/singularity-upgrader/latest/2019-01-16-e20e8402-db30719e/db30719ec9c9b6e23d7f861811d32447.simg"
url: https://datasets.datalad.org/shub/phpHavok/singularity-upgrader/latest/2019-01-16-e20e8402-db30719e/
recipe: https://datasets.datalad.org/shub/phpHavok/singularity-upgrader/latest/2019-01-16-e20e8402-db30719e/Singularity
collection: phpHavok/singularity-upgrader
---

# phpHavok/singularity-upgrader:latest

```bash
$ singularity pull shub://phpHavok/singularity-upgrader:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: singularityhub/centos

%labels
    Maintainer Jacob Chappell <chappellind@gmail.com>
    Version 1.0

%environment
    export GOPATH="/tmp/singularity-upgrader"
    export PATH="/usr/local/go/bin:$PATH"

%post
    yum -y update
    yum -y groupinstall 'Development Tools'
    yum -y install git libseccomp-devel libuuid-devel \
        openssl-devel squashfs-tools wget
    wget https://dl.google.com/go/go1.11.linux-amd64.tar.gz
    tar -C /usr/local -xzf go1.11.linux-amd64.tar.gz

%runscript
    if [ $# -lt 2 ]; then
        echo "Error: missing arguments"
        exit 1
    fi
    mkdir -p $GOPATH/src/github.com/sylabs
    cd $GOPATH/src/github.com/sylabs
    git clone https://github.com/sylabs/singularity
    cd $GOPATH/src/github.com/sylabs/singularity
    git checkout "$1"
    if [ $? -ne 0 ]; then
        echo "Error: invalid version tag"
        exit 1
    fi
    if [ ! -d "$2" ]; then
        echo "Error: prefix path is invalid, is it mounted?"
        exit 1
    fi
    if [ -z "$3" ]; then
        ./mconfig --prefix="$2"
    else
        if [ ! -d "$3" ]; then
            echo "Error: state dir is invalid, is it mounted?"
            exit 1
        fi
        ./mconfig --prefix="$2" --localstatedir="$3"
    fi
    make -C builddir
    make -C builddir install

%help
This container will build an upgraded (configurable) version of Singularity 3.0
or higher. Use this container if you want to upgrade your system version of
Singularity without installing all of the dependencies on your system. You must
have write access to whatever PREFIX directory you choose to install
Singularity into. It's recommended to run the container as root if you're
performing a system installation.

Usage: singularity run IMAGE TAG PREFIX [STATEDIR]

    IMAGE       This Singularity image file to run.
    TAG         The tag or branch of Singularity to build.
    PREFIX      The prefix directory to build into.
    STATEDIR    An optional directory for state files. Defaults to PREFIX.

Examples:

    # Install Singularity v3.0.2 in /opt/singularity on your host system.
    singularity run -B /opt/singularity IMAGE v3.0.2 /opt/singularity
```

## Collection

 - Name: [phpHavok/singularity-upgrader](https://github.com/phpHavok/singularity-upgrader)
 - License: None

