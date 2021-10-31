---
id: 4552
name: "aghozlane/Let-it-bin"
branch: "master"
tag: "samtools"
commit: "d3e9df3bcc153d6bef21cc8b6583e52216975b9f"
version: "9bfeab63b34b1093a47883359a1ec66b"
build_date: "2018-08-30T14:39:44.320Z"
size_mb: 516
size: 155217951
sif: "https://datasets.datalad.org/shub/aghozlane/Let-it-bin/samtools/2018-08-30-d3e9df3b-9bfeab63/9bfeab63b34b1093a47883359a1ec66b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/aghozlane/Let-it-bin/samtools/2018-08-30-d3e9df3b-9bfeab63/
recipe: https://datasets.datalad.org/shub/aghozlane/Let-it-bin/samtools/2018-08-30-d3e9df3b-9bfeab63/Singularity
collection: aghozlane/Let-it-bin
---

# aghozlane/Let-it-bin:samtools

```bash
$ singularity pull shub://aghozlane/Let-it-bin:samtools
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%environment
    export LC_ALL=C

%post
    apt -y update && apt -y install wget zlib1g zlib1g-dev bzip2 build-essential libncurses5-dev
    wget https://github.com/samtools/samtools/releases/download/1.3/samtools-1.3.tar.bz2
    tar -xjf samtools-1.3.tar.bz2
    cd samtools-1.3 && ./configure &&  make && make install
    mkdir /pasteur
```

## Collection

 - Name: [aghozlane/Let-it-bin](https://github.com/aghozlane/Let-it-bin)
 - License: None

