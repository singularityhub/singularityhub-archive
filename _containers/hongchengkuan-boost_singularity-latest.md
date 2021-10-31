---
id: 12867
name: "hongchengkuan/boost_singularity"
branch: "master"
tag: "latest"
commit: "ce2782cd3c3200eccf2006583894ad521304e15d"
version: "e4d15f0b3fa79be903f00bb61955ab99"
build_date: "2020-05-02T05:58:27.257Z"
size_mb: 1028.0
size: 310652959
sif: "https://datasets.datalad.org/shub/hongchengkuan/boost_singularity/latest/2020-05-02-ce2782cd-e4d15f0b/e4d15f0b3fa79be903f00bb61955ab99.sif"
url: https://datasets.datalad.org/shub/hongchengkuan/boost_singularity/latest/2020-05-02-ce2782cd-e4d15f0b/
recipe: https://datasets.datalad.org/shub/hongchengkuan/boost_singularity/latest/2020-05-02-ce2782cd-e4d15f0b/Singularity
collection: hongchengkuan/boost_singularity
---

# hongchengkuan/boost_singularity:latest

```bash
$ singularity pull shub://hongchengkuan/boost_singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:10

%post
    apt-get -y update
    apt-get -y install libboost-all-dev
    # Clean up
    apt-get -y autoremove
    rm -rvf /var/lib/apt/lists/*
```

## Collection

 - Name: [hongchengkuan/boost_singularity](https://github.com/hongchengkuan/boost_singularity)
 - License: None

