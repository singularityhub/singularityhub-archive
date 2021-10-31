---
id: 8696
name: "netcatninja/glibc"
branch: "master"
tag: "latest"
commit: "1a5ecb57949e9d6636025923f37775805e36666d"
version: "9d7544f92377138ae4fa1f8e12c0171d"
build_date: "2020-09-26T00:45:55.467Z"
size_mb: 119
size: 55762975
sif: "https://datasets.datalad.org/shub/netcatninja/glibc/latest/2020-09-26-1a5ecb57-9d7544f9/9d7544f92377138ae4fa1f8e12c0171d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/netcatninja/glibc/latest/2020-09-26-1a5ecb57-9d7544f9/
recipe: https://datasets.datalad.org/shub/netcatninja/glibc/latest/2020-09-26-1a5ecb57-9d7544f9/Singularity
collection: netcatninja/glibc
---

# netcatninja/glibc:latest

```bash
$ singularity pull shub://netcatninja/glibc:latest
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

 - Name: [netcatninja/glibc](https://github.com/netcatninja/glibc)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

