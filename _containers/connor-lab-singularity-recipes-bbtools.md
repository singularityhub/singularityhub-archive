---
id: 6952
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "bbtools"
commit: "a43cefa7f62c25a6726a49f5634f285ba75ea6a9"
version: "5b6377dc4333b18e85a4ae00bda536d1"
build_date: "2019-02-07T11:31:15.353Z"
size_mb: 126
size: 72605727
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/bbtools/2019-02-07-a43cefa7-5b6377dc/5b6377dc4333b18e85a4ae00bda536d1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/singularity-recipes/bbtools/2019-02-07-a43cefa7-5b6377dc/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/bbtools/2019-02-07-a43cefa7-5b6377dc/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:bbtools

```bash
$ singularity pull shub://connor-lab/singularity-recipes:bbtools
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.8

%post
    apk update
    apk upgrade
    apk add git make
    apk add bash curl openjdk8-jre-base zlib-dev
    

    cd /usr/local/bin
    curl -fsSL 'https://downloads.sourceforge.net/project/bbmap/BBMap_38.25.tar.gz' | tar -xz
    find /usr/local/bin/bbmap -maxdepth 1 -perm /u=x -type f -exec ln -s {} /usr/local/bin/ \;
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

