---
id: 8994
name: "netcatninja/cookbook"
branch: "master"
tag: "glibc"
commit: "74cb540ddadd29dae318e4b8b9c8c4d070143d2f"
version: "d555c0609467b1479adf45ae01ff06bf"
build_date: "2019-05-10T10:48:53.386Z"
size_mb: 119
size: 55762975
sif: "https://datasets.datalad.org/shub/netcatninja/cookbook/glibc/2019-05-10-74cb540d-d555c060/d555c0609467b1479adf45ae01ff06bf.simg"
url: https://datasets.datalad.org/shub/netcatninja/cookbook/glibc/2019-05-10-74cb540d-d555c060/
recipe: https://datasets.datalad.org/shub/netcatninja/cookbook/glibc/2019-05-10-74cb540d-d555c060/Singularity
collection: netcatninja/cookbook
---

# netcatninja/cookbook:glibc

```bash
$ singularity pull shub://netcatninja/cookbook:glibc
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%help
    Start with a newer version of glibc. 

%runscript
    ldd --version | head -n 1
    
%environment
    export LANG=en_US.UTF-8
    export PATH=/usr/bin:/usr/local/sbin:/bin:/usr/local/bin:/usr/sbin:/sbin

%post
    apt-get -y update && apt-get install -y --no-install-recommends  \
    libc-bin 

%labels
    Author Brie Carranza
```

## Collection

 - Name: [netcatninja/cookbook](https://github.com/netcatninja/cookbook)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

