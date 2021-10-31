---
id: 503
name: "kernsuite/singularity"
branch: "master"
tag: "latest"
commit: "fc29ca21612c9b6cadc9e5654f08e617b466075f"
version: "c750b38b423a4257d8ddb18718400751"
build_date: "2018-04-10T11:55:19.442Z"
size_mb: 3447
size: 1672728607
sif: "https://datasets.datalad.org/shub/kernsuite/singularity/latest/2018-04-10-fc29ca21-c750b38b/c750b38b423a4257d8ddb18718400751.simg"
url: https://datasets.datalad.org/shub/kernsuite/singularity/latest/2018-04-10-fc29ca21-c750b38b/
recipe: https://datasets.datalad.org/shub/kernsuite/singularity/latest/2018-04-10-fc29ca21-c750b38b/Singularity
collection: kernsuite/singularity
---

# kernsuite/singularity:latest

```bash
$ singularity pull shub://kernsuite/singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
MirrorURL: http://archive.ubuntu.com/ubuntu/
OSVersion: xenial
Include: software-properties-common
%post
    add-apt-repository -s ppa:kernsuite/kern-1
    apt-add-repository multiverse
    apt-get update
    apt-get dist-upgrade -y
    apt-get install -y cassbeam python-qwt5-qt4 python-qwt5-doc tempo purify casacore-dev casacore-doc casacore-tools casarest casacore-data meqtrees-timba python-purr python-tigger python-meqtrees-cattery python-owlcat python-kittens python-pyxis python-meqtrees-timba rpfits lofar meqtrees libmeqtrees-timba0 aoflagger wsclean sagecal mt-imager oskar python-casacore obit parseltongue greatcmakecookoff sopt libcasasynthesis-dev libcasasynthesis1 libcasa-casa2 libcasa-coordinates2 libcasa-derivedmscal2 libcasa-fits2 libcasa-images2 libcasa-lattices2 libcasa-meas2 libcasa-measures2 libcasa-mirlib2 libcasa-ms2 libcasa-msfits2 libcasa-python2 libcasa-python3-2 libcasa-scimath-f2 libcasa-scimath2 libcasa-tables2 python3-casacore psrcat presto tempo2 psrchive multinest dspsr python-presto python-sourcery chgcentre python-tkp python-katversion python-katpoint python-katdal python-rfimasker python-pip python-virtualenv
    apt-get clean
    pip install --upgrade pip virtualenv
```

## Collection

 - Name: [kernsuite/singularity](https://github.com/kernsuite/singularity)
 - License: None

