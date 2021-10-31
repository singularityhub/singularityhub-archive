---
id: 9210
name: "netcatninja/cookbook"
branch: "master"
tag: "u1604"
commit: "daedac40c52cd758b33a7fb06f1144f5e052a140"
version: "b7983a7d45e3a5fae433f2447cd339a6"
build_date: "2019-10-15T14:42:29.879Z"
size_mb: 471
size: 185090079
sif: "https://datasets.datalad.org/shub/netcatninja/cookbook/u1604/2019-10-15-daedac40-b7983a7d/b7983a7d45e3a5fae433f2447cd339a6.simg"
url: https://datasets.datalad.org/shub/netcatninja/cookbook/u1604/2019-10-15-daedac40-b7983a7d/
recipe: https://datasets.datalad.org/shub/netcatninja/cookbook/u1604/2019-10-15-daedac40-b7983a7d/Singularity
collection: netcatninja/cookbook
---

# netcatninja/cookbook:u1604

```bash
$ singularity pull shub://netcatninja/cookbook:u1604
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%help
    This is a simple container for testing support for Ubuntu 16.04.

%runscript
    cat /etc/lsb-release
    
%environment
    export LANG=en_US.UTF-8
    export PATH=/usr/bin:/usr/local/sbin:/bin:/usr/local/bin:/usr/sbin:/sbin

%post
    apt-get -y update && apt-get install -y --no-install-recommends golang perl python

%labels
    Author Brie Carranza
```

## Collection

 - Name: [netcatninja/cookbook](https://github.com/netcatninja/cookbook)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

