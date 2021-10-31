---
id: 2302
name: "CompBio-TDU-Japan/containers"
branch: "master"
tag: "bwa"
commit: "58478a9f251d425fc6f576e300ac0cf22907274b"
version: "2fcc4f4f851635d1fba89d7251801373"
build_date: "2018-11-16T10:50:05.368Z"
size_mb: 16
size: 3973151
sif: "https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/bwa/2018-11-16-58478a9f-2fcc4f4f/2fcc4f4f851635d1fba89d7251801373.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CompBio-TDU-Japan/containers/bwa/2018-11-16-58478a9f-2fcc4f4f/
recipe: https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/bwa/2018-11-16-58478a9f-2fcc4f4f/Singularity
collection: CompBio-TDU-Japan/containers
---

# CompBio-TDU-Japan/containers:bwa

```bash
$ singularity pull shub://CompBio-TDU-Japan/containers:bwa
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine

%post
    apk add --update --no-cache --virtual build-deps build-base zlib-dev
    apk add --update --no-cache bash
    wget https://github.com/lh3/bwa/releases/download/v0.7.17/bwa-0.7.17.tar.bz2
    tar xf bwa-0.7.17.tar.bz2
    cd bwa-0.7.17
    make
    apk del build-deps
    mv bwa /usr/local/bin/
    cd / ; rm -rf bwa-0.7.17

%runscript
    bwa "$@"
```

## Collection

 - Name: [CompBio-TDU-Japan/containers](https://github.com/CompBio-TDU-Japan/containers)
 - License: None

