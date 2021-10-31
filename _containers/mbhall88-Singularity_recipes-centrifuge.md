---
id: 5461
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "centrifuge"
commit: "a78d650dbf221e4014fcb11aa2fa04987af013c6"
version: "13bc12f41b20001f17e6f8811dc3eeea"
build_date: "2019-11-06T14:49:46.720Z"
size_mb: 678
size: 241152031
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/centrifuge/2019-11-06-a78d650d-13bc12f4/13bc12f41b20001f17e6f8811dc3eeea.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mbhall88/Singularity_recipes/centrifuge/2019-11-06-a78d650d-13bc12f4/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/centrifuge/2019-11-06-a78d650d-13bc12f4/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:centrifuge

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:centrifuge
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%environment
  PATH=/usr/local/bin:$PATH

%post
    apt update
    apt install -y software-properties-common
    apt-add-repository universe
    apt update
    apt install -y git wget build-essential
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT

    # ================================
    # INSTALL centrifuge
    # ================================
    VERSION="88ecab483e32f1d1b54b2e155ddb34ea5806e511"
    git clone https://github.com/infphilo/centrifuge.git
    cd centrifuge*
    git checkout "$VERSION"
    make
    make install prefix=/usr/local
    cd ~
    # need python2 for kreport
    add-apt-repository ppa:deadsnakes/ppa
    apt update
    apt install -y python2.7
    ln -s /usr/bin/python2.7 /usr/bin/python
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

