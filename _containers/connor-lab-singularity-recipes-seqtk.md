---
id: 7007
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "seqtk"
commit: "df99279f62163633d6d5fb465bb1a7321fbfe67b"
version: "4d724c656a66c3bc948762e53cbcfdcd"
build_date: "2019-10-17T09:11:48.051Z"
size_mb: 194
size: 98746399
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/seqtk/2019-10-17-df99279f-4d724c65/4d724c656a66c3bc948762e53cbcfdcd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/singularity-recipes/seqtk/2019-10-17-df99279f-4d724c65/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/seqtk/2019-10-17-df99279f-4d724c65/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:seqtk

```bash
$ singularity pull shub://connor-lab/singularity-recipes:seqtk
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.8

%post
    apk update
    apk upgrade
    apk add git make
    apk add bash gcc bzip2-dev libc-dev ncurses-dev openjdk8-jre-base xz-dev zlib-dev
    
    git clone https://github.com/lh3/seqtk.git /tmp/seqtk
    cd /tmp/seqtk
    make
    mv /tmp/seqtk/seqtk /usr/local/bin/
    rm -rf /tmp/seqtk

%labels
    Maintainer m-bull
    Version seqtk-latest
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

