---
id: 4550
name: "aghozlane/Let-it-bin"
branch: "master"
tag: "trimming"
commit: "e843b0d1642589effc7bbcc4048366ebeec0e5af"
version: "c648132dc1f432c9320597e488a8a995"
build_date: "2018-08-30T14:39:44.328Z"
size_mb: 660
size: 213299231
sif: "https://datasets.datalad.org/shub/aghozlane/Let-it-bin/trimming/2018-08-30-e843b0d1-c648132d/c648132dc1f432c9320597e488a8a995.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/aghozlane/Let-it-bin/trimming/2018-08-30-e843b0d1-c648132d/
recipe: https://datasets.datalad.org/shub/aghozlane/Let-it-bin/trimming/2018-08-30-e843b0d1-c648132d/Singularity
collection: aghozlane/Let-it-bin
---

# aghozlane/Let-it-bin:trimming

```bash
$ singularity pull shub://aghozlane/Let-it-bin:trimming
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%post
    mkdir /pasteur
    apt -y update &&  apt -y install wget build-essential gcj-jdk
    wget ftp://ftp.pasteur.fr/pub/gensoft/projects/AlienTrimmer/AlienTrimmer_0.4.0.tar.gz
    tar -xzf AlienTrimmer_0.4.0.tar.gz
    rm AlienTrimmer_0.4.0.tar.gz
    cd AlienTrimmer_0.4.0/src
    sed "s:-march=native::g" -i Makefile 
    make
    mv AlienTrimmer /usr/local/bin/
```

## Collection

 - Name: [aghozlane/Let-it-bin](https://github.com/aghozlane/Let-it-bin)
 - License: None

