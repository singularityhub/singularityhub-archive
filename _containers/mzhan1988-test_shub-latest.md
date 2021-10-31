---
id: 624
name: "mzhan1988/test_shub"
branch: "master"
tag: "latest"
commit: "7001e666dd9e09574daf6b40c93d5d8e6a26808c"
version: "0245939eb9ec74f5dd8ebf836f5592a0"
build_date: "2017-10-31T10:18:14.465Z"
size_mb: 337
size: 91861023
sif: "https://datasets.datalad.org/shub/mzhan1988/test_shub/latest/2017-10-31-7001e666-0245939e/0245939eb9ec74f5dd8ebf836f5592a0.simg"
url: https://datasets.datalad.org/shub/mzhan1988/test_shub/latest/2017-10-31-7001e666-0245939e/
recipe: https://datasets.datalad.org/shub/mzhan1988/test_shub/latest/2017-10-31-7001e666-0245939e/Singularity
collection: mzhan1988/test_shub
---

# mzhan1988/test_shub:latest

```bash
$ singularity pull shub://mzhan1988/test_shub:latest
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

 - Name: [mzhan1988/test_shub](https://github.com/mzhan1988/test_shub)
 - License: None

