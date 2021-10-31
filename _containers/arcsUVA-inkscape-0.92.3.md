---
id: 6866
name: "arcsUVA/inkscape"
branch: "master"
tag: "0.92.3"
commit: "27627435b603385970618f8593d3416682d613cc"
version: "301ae6b69a91723114d08b591191c3e1"
build_date: "2019-02-04T16:33:11.342Z"
size_mb: 823
size: 268333087
sif: "https://datasets.datalad.org/shub/arcsUVA/inkscape/0.92.3/2019-02-04-27627435-301ae6b6/301ae6b69a91723114d08b591191c3e1.simg"
url: https://datasets.datalad.org/shub/arcsUVA/inkscape/0.92.3/2019-02-04-27627435-301ae6b6/
recipe: https://datasets.datalad.org/shub/arcsUVA/inkscape/0.92.3/2019-02-04-27627435-301ae6b6/Singularity
collection: arcsUVA/inkscape
---

# arcsUVA/inkscape:0.92.3

```bash
$ singularity pull shub://arcsUVA/inkscape:0.92.3
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:xenial
IncludeCmd: yes

%post
    apt-get update
    apt-get -y upgrade
    apt-get -y install \
        software-properties-common \
        libcanberra-gtk-module \
        packagekit-gtk3-module \
        python-dbus \
        python3-dbus

    add-apt-repository ppa:inkscape.dev/stable
    apt-get update

    # Inkscape
    apt-get -y install inkscape

    # Pandoc
    apt-get -y install pandoc

%runscript
    exec inkscape

%help
This container provides the following applications:
    * Inkscape 0.92.3
    * Pandoc 1.16.0.2

%environment
    export LC_ALL=en_US.UTF-8

%labels
    AUTHOR khs3z@virginia.edu
```

## Collection

 - Name: [arcsUVA/inkscape](https://github.com/arcsUVA/inkscape)
 - License: None

