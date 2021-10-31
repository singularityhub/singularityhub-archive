---
id: 10491
name: "timkphd/stuff"
branch: "master"
tag: "386"
commit: "ab972e5b084639805287cade6198edb0f5108149"
version: "7d4c65f236755ffc1773e6246c12321bfeaf9fc69dd8db1db8ee55dac5946a74"
build_date: "2019-08-06T12:27:04.881Z"
size_mb: 292.59375
size: 306806784
sif: "https://datasets.datalad.org/shub/timkphd/stuff/386/2019-08-06-ab972e5b-7d4c65f2/7d4c65f236755ffc1773e6246c12321bfeaf9fc69dd8db1db8ee55dac5946a74.sif"
url: https://datasets.datalad.org/shub/timkphd/stuff/386/2019-08-06-ab972e5b-7d4c65f2/
recipe: https://datasets.datalad.org/shub/timkphd/stuff/386/2019-08-06-ab972e5b-7d4c65f2/Singularity
collection: timkphd/stuff
---

# timkphd/stuff:386

```bash
$ singularity pull shub://timkphd/stuff:386
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: i686/python
# Aug 06 2019 6:23 AM
%post
    apt-get -y update --fix-missing
    apt-get -y install wget
    apt-get -y install gawk
    apt-get -y install apt-transport-https

# Intalling Fortran also gives us C.    
    apt install -y gfortran 
    apt install -y g++
    apt install -y make
date

# Install editors
  apt install -y nano
  apt install -y vim


%environment
    export LC_ALL=C

%labels
    Author thkphd
```

## Collection

 - Name: [timkphd/stuff](https://github.com/timkphd/stuff)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

