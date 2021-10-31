---
id: 536
name: "libAtoms/QUIP"
branch: "master"
tag: "latest"
commit: "b44be91df97825aa067e2b11256c2308ea67d9d9"
version: "6d7ea951343aef488039cc792c16cbdb"
build_date: "2021-01-29T14:37:41.855Z"
size_mb: 5603
size: 1817960479
sif: "https://datasets.datalad.org/shub/libAtoms/QUIP/latest/2021-01-29-b44be91d-6d7ea951/6d7ea951343aef488039cc792c16cbdb.simg"
url: https://datasets.datalad.org/shub/libAtoms/QUIP/latest/2021-01-29-b44be91d-6d7ea951/
recipe: https://datasets.datalad.org/shub/libAtoms/QUIP/latest/2021-01-29-b44be91d-6d7ea951/Singularity
collection: libAtoms/QUIP
---

# libAtoms/QUIP:latest

```bash
$ singularity pull shub://libAtoms/QUIP:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: libatomsquip/quip:latest

%post
    mkdir /storage
```

## Collection

 - Name: [libAtoms/QUIP](https://github.com/libAtoms/QUIP)
 - License: None

