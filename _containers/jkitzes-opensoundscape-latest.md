---
id: 4886
name: "jkitzes/opensoundscape"
branch: "develop"
tag: "latest"
commit: "c23bac4b50043cd115cd9d1eb5c531925ad0881d"
version: "d457227e472aa076fafdfaeee252037d"
build_date: "2018-10-11T09:24:02.437Z"
size_mb: 2222
size: 754700319
sif: "https://datasets.datalad.org/shub/jkitzes/opensoundscape/latest/2018-10-11-c23bac4b-d457227e/d457227e472aa076fafdfaeee252037d.simg"
url: https://datasets.datalad.org/shub/jkitzes/opensoundscape/latest/2018-10-11-c23bac4b-d457227e/
recipe: https://datasets.datalad.org/shub/jkitzes/opensoundscape/latest/2018-10-11-c23bac4b-d457227e/Singularity
collection: jkitzes/opensoundscape
---

# jkitzes/opensoundscape:latest

```bash
$ singularity pull shub://jkitzes/opensoundscape:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: archlinux/base

%setup
    mkdir -p ${SINGULARITY_ROOTFS}/opt/opensoundscape
    cp -rv . ${SINGULARITY_ROOTFS}/opt/opensoundscape

%labels
    AUTHOR moore0557@gmail.com

%post
    pacman -Syyu --noconfirm
    pacman -S python python-pip libsamplerate git gcc python-pandas python-numpy \
        python-matplotlib python-docopt python-scipy python-pymongo python-progressbar \
        python-pytest tk mongodb mongodb-tools opencv hdf5 gtk3 python-scikit-learn \
        --noconfirm
    pip install -r /opt/opensoundscape/requirements.txt

%apprun opensoundscape
    python /opt/opensoundscape/opensoundscape.py $*

%appenv opensoundscape
    export MPLBACKEND="TkAgg"

%apprun mongodb
    mongod $*
```

## Collection

 - Name: [jkitzes/opensoundscape](https://github.com/jkitzes/opensoundscape)
 - License: None

