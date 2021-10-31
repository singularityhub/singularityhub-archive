---
id: 3699
name: "dominik-handler/AP_singu"
branch: "master"
tag: "porechop"
commit: "d1ba2e26976dcd2b36ab6ebbf27d4d45e875668f"
version: "52ad41f8531031407bad5c058f22aa3c"
build_date: "2020-03-31T12:47:33.059Z"
size_mb: 523
size: 243728415
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/porechop/2020-03-31-d1ba2e26-52ad41f8/52ad41f8531031407bad5c058f22aa3c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/porechop/2020-03-31-d1ba2e26-52ad41f8/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/porechop/2020-03-31-d1ba2e26-52ad41f8/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:porechop

```bash
$ singularity pull shub://dominik-handler/AP_singu:porechop
```

## Singularity Recipe

```singularity
#porechop in singularity

BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%runscript
    porechop "$@"

%post
    apt-get -y install wget

    apt-get update
    apt-get -y install build-essential
    apt-get -y install python3.5
    apt-get -y install git-core 

    apt-get -y install python3-setuptools
    easy_install3 pip

    git clone https://github.com/rrwick/Porechop.git
    cd Porechop
    python3 setup.py install
   
    mkdir /groups
    mkdir /scratch
    mkdir /scratch-ii2
    mkdir /clustertmp

%test
    porechop -h
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

