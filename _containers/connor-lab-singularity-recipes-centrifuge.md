---
id: 6980
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "centrifuge"
commit: "5e322d4c80acb21db9d53649a55a0349c4378009"
version: "4d187b20e46a2700ef623438cda77ad4"
build_date: "2019-02-07T15:45:22.870Z"
size_mb: 260
size: 76550175
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/centrifuge/2019-02-07-5e322d4c-4d187b20/4d187b20e46a2700ef623438cda77ad4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/singularity-recipes/centrifuge/2019-02-07-5e322d4c-4d187b20/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/centrifuge/2019-02-07-5e322d4c-4d187b20/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:centrifuge

```bash
$ singularity pull shub://connor-lab/singularity-recipes:centrifuge
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
    curl -fsSL "https://github.com/infphilo/centrifuge/archive/v1.0.4-beta.tar.gz" | tar xz
    cd /usr/local/bin/centrifuge-1.0.4-beta
    make -j 4
    make install

%labels
    Maintainer m-bull
    Version centrifuge-1.0.4-beta
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

