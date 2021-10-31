---
id: 646
name: "remyd1/alpine_netools"
branch: "master"
tag: "latest"
commit: "b2c1e7008c06a3e8e207d83291b40ce16d97f8ff"
version: "9bbd09b958cf5d55ae5e2eb2b948bc13"
build_date: "2019-08-19T13:34:22.332Z"
size_mb: 200
size: 7180319
sif: "https://datasets.datalad.org/shub/remyd1/alpine_netools/latest/2019-08-19-b2c1e700-9bbd09b9/9bbd09b958cf5d55ae5e2eb2b948bc13.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/remyd1/alpine_netools/latest/2019-08-19-b2c1e700-9bbd09b9/
recipe: https://datasets.datalad.org/shub/remyd1/alpine_netools/latest/2019-08-19-b2c1e700-9bbd09b9/Singularity
collection: remyd1/alpine_netools
---

# remyd1/alpine_netools:latest

```bash
$ singularity pull shub://remyd1/alpine_netools:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.6

%runscript
    exec /usr/bin/nmap "$@"

%labels
   AUTHOR remy.dernat@umontpellier.fr

%post
    echo http://nl.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
    apk update && \
    apk add --no-cache nmap nbtscan iperf nethogs netcat-openbsd
```

## Collection

 - Name: [remyd1/alpine_netools](https://github.com/remyd1/alpine_netools)
 - License: None

