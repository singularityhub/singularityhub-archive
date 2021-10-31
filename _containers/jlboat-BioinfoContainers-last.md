---
id: 9006
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "last"
commit: "9c4212ba689391bf24d37b740ef79d78855c0c73"
version: "2d735c04f7eae1191d2310c85220dac8"
build_date: "2019-09-24T17:49:25.144Z"
size_mb: 403
size: 155594783
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/last/2019-09-24-9c4212ba-2d735c04/2d735c04f7eae1191d2310c85220dac8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jlboat/BioinfoContainers/last/2019-09-24-9c4212ba-2d735c04/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/last/2019-09-24-9c4212ba-2d735c04/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:last

```bash
$ singularity pull shub://jlboat/BioinfoContainers:last
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: debian:latest

%labels
    Topic Bioinformatics
    last ??

%post
    apt-get update --fix-missing && apt-get install -y mercurial python python-pip build-essential zlib1g-dev && rm -rf /var/lib/apt/lists/*
    hg clone http://last.cbrc.jp/last/
    cd last
    make
    make install
    apt-get remove -y mercurial build-essential
    apt autoremove -y
    pip install pillow Image

%runscript
    exec "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

