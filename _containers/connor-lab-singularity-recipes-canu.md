---
id: 6953
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "canu"
commit: "a43cefa7f62c25a6726a49f5634f285ba75ea6a9"
version: "23d139eb7f9377eedd448af284aea408"
build_date: "2021-02-16T02:45:34.861Z"
size_mb: 306
size: 128073759
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/canu/2021-02-16-a43cefa7-23d139eb/23d139eb7f9377eedd448af284aea408.simg"
url: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/canu/2021-02-16-a43cefa7-23d139eb/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/canu/2021-02-16-a43cefa7-23d139eb/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:canu

```bash
$ singularity pull shub://connor-lab/singularity-recipes:canu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.8

%post
    apk update
    apk upgrade
    apk add git make
    apk add bash curl openjdk8-jre-base perl zlib-dev
    

    cd /usr/local/bin
    curl -fsSL 'https://github.com/marbl/canu/releases/download/v1.8/canu-1.8.Linux-amd64.tar.xz' | tar -xJ
    find /usr/local/bin/canu-1.8 -maxdepth 3 -perm /u=x -type f -exec ln -s {} /usr/local/bin/ \;
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

