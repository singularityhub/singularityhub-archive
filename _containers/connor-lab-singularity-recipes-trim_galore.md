---
id: 7004
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "trim_galore"
commit: "3b2f76898f2518a737bc995646da3f2092caa156"
version: "29b57da54637ce67d2912a26e40d5f38"
build_date: "2020-11-05T17:10:37.904Z"
size_mb: 366
size: 181887007
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/trim_galore/2020-11-05-3b2f7689-29b57da5/29b57da54637ce67d2912a26e40d5f38.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/singularity-recipes/trim_galore/2020-11-05-3b2f7689-29b57da5/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/trim_galore/2020-11-05-3b2f7689-29b57da5/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:trim_galore

```bash
$ singularity pull shub://connor-lab/singularity-recipes:trim_galore
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.8

%post
    apk update
    apk upgrade
    apk add git make
    apk add bash curl fontconfig gcc bzip2-dev libc-dev ncurses-dev openjdk8-jre ttf-dejavu xz-dev zlib-dev
    apk add perl python2 python2-dev py2-pip

    pip install cutadapt

    cd /usr/local/bin
    curl -fsSL "https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.8.zip" -o fastqc_v0.11.8.zip
    unzip fastqc_v0.11.8.zip
    find /usr/local/bin/FastQC -name "fastqc" -maxdepth 1 -exec chmod +x {} \;
    find /usr/local/bin/FastQC -name "fastqc" -maxdepth 1 -perm /u+x -exec ln -s {} /usr/local/bin \;

    cd /usr/local/bin
    curl -fsSL "https://github.com/FelixKrueger/TrimGalore/archive/0.5.0.tar.gz" | tar -xz
    find /usr/local/bin/ -name "trim_galore" -exec ln -s {} /usr/local/bin \;

%labels
    Maintainer m-bull
    Version trim_galore-0.5.0
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

