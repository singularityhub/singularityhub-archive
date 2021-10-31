---
id: 13487
name: "Grayson3455/My-tigar"
branch: "master"
tag: "def"
commit: "270ffe59396fa17191b169a0d49c25713ff57c35"
version: "1ed5ea87ee7a7e28963cda5326662ef7f913a9f3ae6df882be446148b1a369bd"
build_date: "2020-12-18T21:56:27.396Z"
size_mb: 710.96875
size: 745504768
sif: "https://datasets.datalad.org/shub/Grayson3455/My-tigar/def/2020-12-18-270ffe59-1ed5ea87/1ed5ea87ee7a7e28963cda5326662ef7f913a9f3ae6df882be446148b1a369bd.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/Grayson3455/My-tigar/def/2020-12-18-270ffe59-1ed5ea87/
recipe: https://datasets.datalad.org/shub/Grayson3455/My-tigar/def/2020-12-18-270ffe59-1ed5ea87/Singularity
collection: Grayson3455/My-tigar
---

# Grayson3455/My-tigar:def

```bash
$ singularity pull shub://Grayson3455/My-tigar:def
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: quay.io/fenicsproject/stable:current

####### Notes #######
#
# This is a Singularity recipe that adds TSFC, tIGAr, and igakit to a
# Docker container with the current stable version of FEniCS.  (TSFC is not
# strictly required for tIGAr, but may be useful for some complicated
# variational forms.)
#
# To build an image from this recipe, use the following command (on a
# system where you have sudo access):
#
# $ sudo singularity build image.simg singularity-recipe.def
#
# "image.simg" may be replaced with the desired file name for the image.
# This image will be usable with later versions of singularity, but is NOT
# necessarily backwards-compatible with earlier versions.  
#
# On some systems, it may be necessary to mount a custom home
# directory at runtime (with the -H option), to avoid conficts with
# software installed in your home directory (which is mounted by default).
#
#####################

%post
    apt-get -y install libgfortran3
    pip3 install git+https://github.com/blechta/tsfc.git@2018.1.0
    pip3 install git+https://github.com/blechta/COFFEE.git@2018.1.0
    pip3 install git+https://github.com/blechta/FInAT.git@2018.1.0
    pip3 install singledispatch networkx pulp
    pip3 install git+https://github.com/Grayson3455/My-tigar.git
    pip3 install https://bitbucket.org/dalcinl/igakit/get/master.tar.gz
    pip3 install --force-reinstall scipy
```

## Collection

 - Name: [Grayson3455/My-tigar](https://github.com/Grayson3455/My-tigar)
 - License: [GNU Lesser General Public License v3.0](https://api.github.com/licenses/lgpl-3.0)

