---
id: 6993
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "quast"
commit: "8358bcb85070064e9e654d9777e534823fe5c9eb"
version: "d8c77745db906b35e5841f04b5d30360"
build_date: "2019-02-07T15:56:31.748Z"
size_mb: 525
size: 180166687
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/quast/2019-02-07-8358bcb8-d8c77745/d8c77745db906b35e5841f04b5d30360.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/singularity-recipes/quast/2019-02-07-8358bcb8-d8c77745/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/quast/2019-02-07-8358bcb8-d8c77745/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:quast

```bash
$ singularity pull shub://connor-lab/singularity-recipes:quast
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.8


%post
    apk update
    apk upgrade
    apk add bash bzip2-dev g++ gcc gcompat libc-dev make ncurses-dev xz-dev zlib-dev musl-dev 
    apk add curl freetype-dev git libpng-dev perl python3 python3-dev py3-pip 
   
    pip3 install matplotlib
    pip3 install git+https://github.com/ablab/quast

%labels
    Maintainer m-bull
    Version quast-git-latest
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

