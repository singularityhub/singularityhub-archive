---
id: 8782
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "star"
commit: "01fd237ed1c7688e532770e499b506f0d189a7b5"
version: "88ebb66c8cf1ca3e0f819b211bc099dd"
build_date: "2020-04-16T12:33:41.468Z"
size_mb: 761
size: 532652063
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/star/2020-04-16-01fd237e-88ebb66c/88ebb66c8cf1ca3e0f819b211bc099dd.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/star/2020-04-16-01fd237e-88ebb66c/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/star/2020-04-16-01fd237e-88ebb66c/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:star

```bash
$ singularity pull shub://jlboat/BioinfoContainers:star
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: debian:latest

%labels
    Topic Bioinformatics
    Input FASTQ
    Output BAM
    STAR latest

%help
singularity run star.simg STAR

%environment
    PATH=$PATH:/STAR/bin/Linux_x86_64/

%post
    apt-get update --fix-missing && apt-get install -y git make g++ libz-dev && rm -rf /var/lib/apt/lists/*
    git clone https://github.com/alexdobin/STAR.git
    chmod -R 777 /STAR
    cd STAR/source
    make STAR
    apt-get remove -y git make g++

%runscript
    exec "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

