---
id: 10185
name: "DrVale83/bioinfo"
branch: "master"
tag: "samtools"
commit: "0f5c222b326c9283beccdd09add8933c3ccd7ddd"
version: "b88d6678e59a665f49d3cbfe18292168"
build_date: "2019-07-03T13:50:46.936Z"
size_mb: 436
size: 152403999
sif: "https://datasets.datalad.org/shub/DrVale83/bioinfo/samtools/2019-07-03-0f5c222b-b88d6678/b88d6678e59a665f49d3cbfe18292168.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/DrVale83/bioinfo/samtools/2019-07-03-0f5c222b-b88d6678/
recipe: https://datasets.datalad.org/shub/DrVale83/bioinfo/samtools/2019-07-03-0f5c222b-b88d6678/Singularity
collection: DrVale83/bioinfo
---

# DrVale83/bioinfo:samtools

```bash
$ singularity pull shub://DrVale83/bioinfo:samtools
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:latest

%post
    apt-get update --fix-missing && apt-get install -y wget make zlib1g-dev gcc \
        pkg-config autoconf libncurses5-dev libbz2-dev liblzma-dev libcurl4-gnutls-dev libssl-dev
    cd /opt/
    wget --quiet https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
    tar xvfj samtools-1.9.tar.bz2
    rm samtools-1.9.tar.bz2
    cd samtools-1.9
    ./configure
    make
    make install
    chmod -R 777 /opt/*

%runscript
    exec samtools "$@"
```

## Collection

 - Name: [DrVale83/bioinfo](https://github.com/DrVale83/bioinfo)
 - License: None

