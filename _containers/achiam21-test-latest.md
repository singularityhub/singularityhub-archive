---
id: 7814
name: "achiam21/test"
branch: "master"
tag: "latest"
commit: "55dee316bb3b25021e3cea2d9464d7e70515ba1b"
version: "0126a68d10883dde9717aa794f2aad56"
build_date: "2019-03-16T19:00:01.529Z"
size_mb: 205
size: 81637407
sif: "https://datasets.datalad.org/shub/achiam21/test/latest/2019-03-16-55dee316-0126a68d/0126a68d10883dde9717aa794f2aad56.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/achiam21/test/latest/2019-03-16-55dee316-0126a68d/
recipe: https://datasets.datalad.org/shub/achiam21/test/latest/2019-03-16-55dee316-0126a68d/Singularity
collection: achiam21/test
---

# achiam21/test:latest

```bash
$ singularity pull shub://achiam21/test:latest
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

 - Name: [achiam21/test](https://github.com/achiam21/test)
 - License: None

