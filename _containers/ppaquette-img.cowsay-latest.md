---
id: 4594
name: "ppaquette/img.cowsay"
branch: "master"
tag: "latest"
commit: "084e7a44a7bbda3e064d43e14217f94ac2d0d7d0"
version: "956687f6064198acc18996fff8dfb93a"
build_date: "2018-08-31T18:06:37.436Z"
size_mb: 220
size: 93384735
sif: "https://datasets.datalad.org/shub/ppaquette/img.cowsay/latest/2018-08-31-084e7a44-956687f6/956687f6064198acc18996fff8dfb93a.simg"
url: https://datasets.datalad.org/shub/ppaquette/img.cowsay/latest/2018-08-31-084e7a44-956687f6/
recipe: https://datasets.datalad.org/shub/ppaquette/img.cowsay/latest/2018-08-31-084e7a44-956687f6/Singularity
collection: ppaquette/img.cowsay
---

# ppaquette/img.cowsay:latest

```bash
$ singularity pull shub://ppaquette/img.cowsay:latest
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

 - Name: [ppaquette/img.cowsay](https://github.com/ppaquette/img.cowsay)
 - License: None

