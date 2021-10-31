---
id: 7723
name: "scrim-network/container-dev"
branch: "master"
tag: "singularity"
commit: "87d8661bc350c52ed1413f372ec389f5e7b12baf"
version: "aa956840a4e7dff480fb3c0c0ef3a60b"
build_date: "2019-03-13T03:34:53.280Z"
size_mb: 4266
size: 2425896991
sif: "https://datasets.datalad.org/shub/scrim-network/container-dev/singularity/2019-03-13-87d8661b-aa956840/aa956840a4e7dff480fb3c0c0ef3a60b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/scrim-network/container-dev/singularity/2019-03-13-87d8661b-aa956840/
recipe: https://datasets.datalad.org/shub/scrim-network/container-dev/singularity/2019-03-13-87d8661b-aa956840/Singularity
collection: scrim-network/container-dev
---

# scrim-network/container-dev:singularity

```bash
$ singularity pull shub://scrim-network/container-dev:singularity
```

## Singularity Recipe

```singularity
# Last modified 25 November 2018 by Robert Nicholas <ren10@psu.edu>.

BootStrap: debootstrap
OSVersion: stretch
MirrorURL: http://ftp.us.debian.org/debian/


%runscript

    exec /bin/bash "$@"


%environment

    export PS1="\n[singularity:$SINGULARITY_CONTAINER] \w \$ "


%post

    # fix package sources
    echo "deb http://ftp.debian.org/debian stretch main contrib non-free" > /etc/apt/sources.list
    echo "deb http://ftp.debian.org/debian stretch-backports main contrib non-free" >> /etc/apt/sources.list
    echo "deb http://deb.debian.org/debian-security/ stretch/updates main contrib non-free" >> /etc/apt/sources.list
    echo "deb http://deb.debian.org/debian stretch-updates main contrib non-free" >> /etc/apt/sources.list

    # upgrade packages in base image
    DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y dist-upgrade

    # install additional packages
    DEBIAN_FRONTEND=noninteractive apt-get -y install joe mc wget htop pandoc pandoc-citeproc texlive-latex-recommended r-base octave gnuplot imagemagick julia ncl-ncarg cdo nco build-essential

    # clean up orphaned packages
    DEBIAN_FRONTEND=noninteractive apt-get -y autoremove

    # create a few ACI-specific directories within the container
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/group
    mkdir -p /gpfs/scratch
    mkdir -p /var/spool/torque
```

## Collection

 - Name: [scrim-network/container-dev](https://github.com/scrim-network/container-dev)
 - License: None

