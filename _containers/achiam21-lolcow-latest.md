---
id: 7800
name: "achiam21/lolcow"
branch: "master"
tag: "latest"
commit: "a59d8de3121579fe9c95ab8af0297c2e3aefd827"
version: "de708bcac9886eec381735167b2b9a20"
build_date: "2021-03-27T08:06:46.922Z"
size_mb: 205
size: 81621023
sif: "https://datasets.datalad.org/shub/achiam21/lolcow/latest/2021-03-27-a59d8de3-de708bca/de708bcac9886eec381735167b2b9a20.simg"
url: https://datasets.datalad.org/shub/achiam21/lolcow/latest/2021-03-27-a59d8de3-de708bca/
recipe: https://datasets.datalad.org/shub/achiam21/lolcow/latest/2021-03-27-a59d8de3-de708bca/Singularity
collection: achiam21/lolcow
---

# achiam21/lolcow:latest

```bash
$ singularity pull shub://achiam21/lolcow:latest
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

 - Name: [achiam21/lolcow](https://github.com/achiam21/lolcow)
 - License: None

