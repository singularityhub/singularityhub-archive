---
id: 4007
name: "omento/singularity"
branch: "master"
tag: "bionic"
commit: "a8db86bcf785eec38cac90ad4cd002109db8ea9b"
version: "fc684ad5db98507595ca249406dd103a"
build_date: "2018-08-16T17:20:05.721Z"
size_mb: 289
size: 88789023
sif: "https://datasets.datalad.org/shub/omento/singularity/bionic/2018-08-16-a8db86bc-fc684ad5/fc684ad5db98507595ca249406dd103a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/omento/singularity/bionic/2018-08-16-a8db86bc-fc684ad5/
recipe: https://datasets.datalad.org/shub/omento/singularity/bionic/2018-08-16-a8db86bc-fc684ad5/Singularity
collection: omento/singularity
---

# omento/singularity:bionic

```bash
$ singularity pull shub://omento/singularity:bionic
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/
Include: bash vim less man-db apt-utils tzdata

%labels
    Maintainer omento

%help
A baseline container of Ubuntu 18.04 LTS Bionic Beaver

%environment
    LC_ALL=C
    LD_LIBRARY_PATH=/usr/local/lib64:/usr/local/lib:/usr/lib64:/usr/lib:/lib64:/lib
    TZ='America/New_York'

    export LC_ALL LD_LIBRARY_PATH TZ

%post
    export DEBIAN_FRONTEND=noninteractive

    ## Clean Apt cache
    apt-get clean
    rm -rf /var/cache/apt

    ## Fix Sources.list for repositories
    ## Include release | updates | security
    ## and       main | restricted | universe
    printf "deb http://us.archive.ubuntu.com/ubuntu/ bionic main restricted universe \ndeb-src http://us.archive.ubuntu.com/ubuntu/ bionic main restricted universe \ndeb http://us.archive.ubuntu.com/ubuntu/ bionic-security main restricted universe \ndeb-src http://us.archive.ubuntu.com/ubuntu/ bionic-security main restricted universe \ndeb http://us.archive.ubuntu.com/ubuntu/ bionic-updates main restricted universe \ndeb-src http://us.archive.ubuntu.com/ubuntu/ bionic-updates main restricted universe \n" > /etc/apt/sources.list

    ## Update container
    apt-get update
    apt-get -y --with-new-pkgs upgrade
    apt-get -y autoremove
    apt-get clean
    rm -rf /var/cache/apt

%test
    echo "Image Build Date: $(date)"
    echo "Ubuntu $(cat /etc/os-release | grep VERSION= | sed 's|VERSION=||' | sed 's|"||g')"

%runscript
    echo "Ubuntu $(cat /etc/os-release | grep VERSION= | sed 's|VERSION=||' | sed 's|"||g')"
    echo "Image Build Date: 16.08.2018"
```

## Collection

 - Name: [omento/singularity](https://github.com/omento/singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

