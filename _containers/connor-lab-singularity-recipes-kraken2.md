---
id: 6982
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "kraken2"
commit: "5e322d4c80acb21db9d53649a55a0349c4378009"
version: "6d7a499043db7d63cce4fa48873a8d6c"
build_date: "2019-02-07T15:45:22.855Z"
size_mb: 226
size: 72134687
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/kraken2/2019-02-07-5e322d4c-6d7a4990/6d7a499043db7d63cce4fa48873a8d6c.simg"
url: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/kraken2/2019-02-07-5e322d4c-6d7a4990/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/kraken2/2019-02-07-5e322d4c-6d7a4990/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:kraken2

```bash
$ singularity pull shub://connor-lab/singularity-recipes:kraken2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.8

%post
    apk update
    apk upgrade
    apk add git make
    apk add bash curl g++ gcc bzip2-dev libc-dev ncurses-dev xz-dev zlib-dev
    apk add perl

    cd /usr/local/bin
    curl -fsSL "https://github.com/DerrickWood/kraken2/archive/v2.0.7-beta.tar.gz" | tar xz
    cd kraken2-2.0.7-beta
    ./install_kraken2.sh /usr/local/bin

%labels
    Maintainer m-bull
    Version kraken2-v2.0.7
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

