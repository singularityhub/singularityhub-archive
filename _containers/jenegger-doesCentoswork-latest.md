---
id: 3791
name: "jenegger/doesCentoswork"
branch: "master"
tag: "latest"
commit: "5ae9cbc7748de259391982ca75546cecfcdf1563"
version: "c7a86089f37592d6bacb035d19429362"
build_date: "2018-07-31T15:32:55.928Z"
size_mb: 220
size: 93294623
sif: "https://datasets.datalad.org/shub/jenegger/doesCentoswork/latest/2018-07-31-5ae9cbc7-c7a86089/c7a86089f37592d6bacb035d19429362.simg"
url: https://datasets.datalad.org/shub/jenegger/doesCentoswork/latest/2018-07-31-5ae9cbc7-c7a86089/
recipe: https://datasets.datalad.org/shub/jenegger/doesCentoswork/latest/2018-07-31-5ae9cbc7-c7a86089/Singularity
collection: jenegger/doesCentoswork
---

# jenegger/doesCentoswork:latest

```bash
$ singularity pull shub://jenegger/doesCentoswork:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
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

 - Name: [jenegger/doesCentoswork](https://github.com/jenegger/doesCentoswork)
 - License: None

