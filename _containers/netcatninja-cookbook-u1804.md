---
id: 9211
name: "netcatninja/cookbook"
branch: "master"
tag: "u1804"
commit: "daedac40c52cd758b33a7fb06f1144f5e052a140"
version: "7ed92e438fb2ddbd9887ed9c6efa41ef"
build_date: "2019-05-22T09:03:51.228Z"
size_mb: 469
size: 196354079
sif: "https://datasets.datalad.org/shub/netcatninja/cookbook/u1804/2019-05-22-daedac40-7ed92e43/7ed92e438fb2ddbd9887ed9c6efa41ef.simg"
url: https://datasets.datalad.org/shub/netcatninja/cookbook/u1804/2019-05-22-daedac40-7ed92e43/
recipe: https://datasets.datalad.org/shub/netcatninja/cookbook/u1804/2019-05-22-daedac40-7ed92e43/Singularity
collection: netcatninja/cookbook
---

# netcatninja/cookbook:u1804

```bash
$ singularity pull shub://netcatninja/cookbook:u1804
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%help
    This is a simple container for testing support for Ubuntu 18.04.

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

