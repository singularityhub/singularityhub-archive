---
id: 3000
name: "kozusznik/proof-singularity"
branch: "master"
tag: "latest"
commit: "4d4f3a8cda8287025fa608b818a057ef118de3b6"
version: "ea14d604eb674156f147d80057ce0c86"
build_date: "2018-06-01T09:59:30.918Z"
size_mb: 220
size: 93085727
sif: "https://datasets.datalad.org/shub/kozusznik/proof-singularity/latest/2018-06-01-4d4f3a8c-ea14d604/ea14d604eb674156f147d80057ce0c86.simg"
url: https://datasets.datalad.org/shub/kozusznik/proof-singularity/latest/2018-06-01-4d4f3a8c-ea14d604/
recipe: https://datasets.datalad.org/shub/kozusznik/proof-singularity/latest/2018-06-01-4d4f3a8c-ea14d604/Singularity
collection: kozusznik/proof-singularity
---

# kozusznik/proof-singularity:latest

```bash
$ singularity pull shub://kozusznik/proof-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%setup
    cp proof.txt $SINGULARITY_ROOTFS/

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

 - Name: [kozusznik/proof-singularity](https://github.com/kozusznik/proof-singularity)
 - License: None

