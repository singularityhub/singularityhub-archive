---
id: 6981
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "interop"
commit: "5e322d4c80acb21db9d53649a55a0349c4378009"
version: "00adca06b33ff23de2e04b6cd1eb2159"
build_date: "2020-11-05T16:35:18.434Z"
size_mb: 355
size: 104521759
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/interop/2020-11-05-5e322d4c-00adca06/00adca06b33ff23de2e04b6cd1eb2159.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/singularity-recipes/interop/2020-11-05-5e322d4c-00adca06/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/interop/2020-11-05-5e322d4c-00adca06/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:interop

```bash
$ singularity pull shub://connor-lab/singularity-recipes:interop
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.8

%post
    apk update
    apk upgrade
    apk add git make
    apk add bash cmake curl gcc g++ bzip2-dev libc-dev ncurses-dev xz-dev zlib-dev

    cd /usr/local/bin
    git clone https://github.com/Illumina/interop.git
    mkdir build && cd build
    cmake ../interop
    cmake --build .
    make install

%labels
    Maintainer m-bull
    Version interop-v1.1.8
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

