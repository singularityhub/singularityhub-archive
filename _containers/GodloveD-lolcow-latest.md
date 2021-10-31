---
id: 46
name: "GodloveD/lolcow"
branch: "master"
tag: "latest"
commit: "a59d8de3121579fe9c95ab8af0297c2e3aefd827"
version: "ee4aae1ea378ad7c0299b308c703187a"
build_date: "2021-04-19T15:47:49.407Z"
size_mb: 336
size: 91828255
sif: "https://datasets.datalad.org/shub/GodloveD/lolcow/latest/2021-04-19-a59d8de3-ee4aae1e/ee4aae1ea378ad7c0299b308c703187a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/GodloveD/lolcow/latest/2021-04-19-a59d8de3-ee4aae1e/
recipe: https://datasets.datalad.org/shub/GodloveD/lolcow/latest/2021-04-19-a59d8de3-ee4aae1e/Singularity
collection: GodloveD/lolcow
---

# GodloveD/lolcow:latest

```bash
$ singularity pull shub://GodloveD/lolcow:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%post
    apt-get -y update
    apt-get -y install fortune cowsay lolcat

%environment
    export LC_ALL=C
    export PATH=/usr/games:$PATH

%runscript
    fortune | cowsay | lolcat
```

## Collection

 - Name: [GodloveD/lolcow](https://github.com/GodloveD/lolcow)
 - License: None

