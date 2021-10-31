---
id: 10486
name: "haqle314/cow-singularity"
branch: "master"
tag: "latest"
commit: "089dd1d4817ffa73525d3b2eb8039f51d6deae9e"
version: "acac5c0948c076c6cf0b9c3126be5377"
build_date: "2019-08-05T20:51:58.285Z"
size_mb: 205.0
size: 82026527
sif: "https://datasets.datalad.org/shub/haqle314/cow-singularity/latest/2019-08-05-089dd1d4-acac5c09/acac5c0948c076c6cf0b9c3126be5377.sif"
url: https://datasets.datalad.org/shub/haqle314/cow-singularity/latest/2019-08-05-089dd1d4-acac5c09/
recipe: https://datasets.datalad.org/shub/haqle314/cow-singularity/latest/2019-08-05-089dd1d4-acac5c09/Singularity
collection: haqle314/cow-singularity
---

# haqle314/cow-singularity:latest

```bash
$ singularity pull shub://haqle314/cow-singularity:latest
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

 - Name: [haqle314/cow-singularity](https://github.com/haqle314/cow-singularity)
 - License: None

