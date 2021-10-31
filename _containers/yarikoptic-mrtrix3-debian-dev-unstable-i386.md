---
id: 5987
name: "yarikoptic/mrtrix3"
branch: "enh-sing"
tag: "debian-dev-unstable-i386"
commit: "14e696d07d23ab64c18f5fbcaec9d253b820637f"
version: "39eb5a1c7e4d88dbc4e471a50e3d5271"
build_date: "2018-12-17T16:03:53.116Z"
size_mb: 1996
size: 710877215
sif: "https://datasets.datalad.org/shub/yarikoptic/mrtrix3/debian-dev-unstable-i386/2018-12-17-14e696d0-39eb5a1c/39eb5a1c7e4d88dbc4e471a50e3d5271.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/yarikoptic/mrtrix3/debian-dev-unstable-i386/2018-12-17-14e696d0-39eb5a1c/
recipe: https://datasets.datalad.org/shub/yarikoptic/mrtrix3/debian-dev-unstable-i386/2018-12-17-14e696d0-39eb5a1c/Singularity
collection: yarikoptic/mrtrix3
---

# yarikoptic/mrtrix3:debian-dev-unstable-i386

```bash
$ singularity pull shub://yarikoptic/mrtrix3:debian-dev-unstable-i386
```

## Singularity Recipe

```singularity
BootStrap: docker
From: i386/debian:unstable

# so if image is executed we just enter the environment
%runscript
    echo "Welcome to the Debian unstable mrtrix3 dev env. (Architecture: i386)"
    echo "Just cd to your mrtrix3 sources or"
    echo " git clone http://github.com/MRtrix3/mrtrix3"
    /bin/bash


%post
    echo "Configuring the environment"
    sed -e  's,^deb ,deb-src ,g' /etc/apt/sources.list > /etc/apt/sources.list.d/sources.list
    apt-get update
    apt-get -y install eatmydata
    # just useful little tools
    eatmydata apt-get -y install vim wget strace time ncdu gnupg curl procps netcat
    eatmydata apt-get -y build-dep mrtrix3
    # some external depends might have not been needed then
    eatmydata apt-get -y install markdown html2text rapidjson-dev libboost-python-dev git clang valgrind lintian
    chmod a+rX -R /etc/apt/sources.list.d
    rm -rf /var/lib/apt/lists/*
    apt-get clean
```

## Collection

 - Name: [yarikoptic/mrtrix3](https://github.com/yarikoptic/mrtrix3)
 - License: [Mozilla Public License 2.0](https://api.github.com/licenses/mpl-2.0)

