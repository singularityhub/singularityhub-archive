---
id: 4047
name: "aeneas-wp3/use-case-3"
branch: "master"
tag: "version1"
commit: "323968e962a241c50027f3480ba7c34a92a8858c"
version: "e563c12fd8d0dde52eec2b690889919d"
build_date: "2018-08-19T16:01:34.760Z"
size_mb: 789
size: 306098207
sif: "https://datasets.datalad.org/shub/aeneas-wp3/use-case-3/version1/2018-08-19-323968e9-e563c12f/e563c12fd8d0dde52eec2b690889919d.simg"
url: https://datasets.datalad.org/shub/aeneas-wp3/use-case-3/version1/2018-08-19-323968e9-e563c12f/
recipe: https://datasets.datalad.org/shub/aeneas-wp3/use-case-3/version1/2018-08-19-323968e9-e563c12f/Singularity
collection: aeneas-wp3/use-case-3
---

# aeneas-wp3/use-case-3:version1

```bash
$ singularity pull shub://aeneas-wp3/use-case-3:version1
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: stable
MirrorURL: http://ftp.us.debian.org/debian/


%labels
  maintainer Anna Scaife <anna.scaife@manchester.ac.uk>
  package.name
  package.version 0.1.0
  package.homepage
  package.source.url
  package.source.mdm5
  package.license GPLv3


%post
    apt-get update
    apt-get -y install python2.7 python-pip
    apt-get -y install python-tk
    apt-get -y install git
    apt-get -y install libgsl-dev
    pip install numpy
    pip install matplotlib
    pip install cython
    pip install pyfits
    pip install pywcs
    cd /usr/local
    git init
    git clone https://github.com/as595/pyrmsynth.git
    cd pyrmsynth/rm_tools/
    python setup.py build_ext --inplace
    apt-get clean


%runscript
    cd /mnt
    python /usr/local/pyrmsynth/rmsynthesis.py "$@"
```

## Collection

 - Name: [aeneas-wp3/use-case-3](https://github.com/aeneas-wp3/use-case-3)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

