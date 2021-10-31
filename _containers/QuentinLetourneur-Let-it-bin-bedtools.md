---
id: 4592
name: "QuentinLetourneur/Let-it-bin"
branch: "master"
tag: "bedtools"
commit: "647c7b5e55f98b734d8bcb0be2bbc1953b9bb875"
version: "24309fdea49aa13eb9f3b6dea7927e4f"
build_date: "2018-09-02T19:38:27.940Z"
size_mb: 431
size: 165691423
sif: "https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/bedtools/2018-09-02-647c7b5e-24309fde/24309fdea49aa13eb9f3b6dea7927e4f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/QuentinLetourneur/Let-it-bin/bedtools/2018-09-02-647c7b5e-24309fde/
recipe: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/bedtools/2018-09-02-647c7b5e-24309fde/Singularity
collection: QuentinLetourneur/Let-it-bin
---

# QuentinLetourneur/Let-it-bin:bedtools

```bash
$ singularity pull shub://QuentinLetourneur/Let-it-bin:bedtools
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
    mkdir /pasteur
    apt -y update
    apt -y install wget build-essential zlib1g-dev python
    
    wget https://github.com/arq5x/bedtools2/releases/download/v2.25.0/bedtools-2.25.0.tar.gz
    tar -xzf bedtools-2.25.0.tar.gz
    rm bedtools-2.25.0.tar.gz
    cd bedtools2
	make
    make install
```

## Collection

 - Name: [QuentinLetourneur/Let-it-bin](https://github.com/QuentinLetourneur/Let-it-bin)
 - License: None

