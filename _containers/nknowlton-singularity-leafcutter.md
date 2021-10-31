---
id: 8933
name: "nknowlton/singularity"
branch: "master"
tag: "leafcutter"
commit: "c884e2fde196ca3066390d83dc22342ded73278a"
version: "ef765dc6a1ff58ef640b23aafcb3cd94"
build_date: "2019-05-08T15:10:10.780Z"
size_mb: 7725
size: 3461402655
sif: "https://datasets.datalad.org/shub/nknowlton/singularity/leafcutter/2019-05-08-c884e2fd-ef765dc6/ef765dc6a1ff58ef640b23aafcb3cd94.simg"
url: https://datasets.datalad.org/shub/nknowlton/singularity/leafcutter/2019-05-08-c884e2fd-ef765dc6/
recipe: https://datasets.datalad.org/shub/nknowlton/singularity/leafcutter/2019-05-08-c884e2fd-ef765dc6/Singularity
collection: nknowlton/singularity
---

# nknowlton/singularity:leafcutter

```bash
$ singularity pull shub://nknowlton/singularity:leafcutter
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: brianyee/r-leafcutter

%post
  mkdir /oasis
  mkdir /projects

%runscript
  R
```

## Collection

 - Name: [nknowlton/singularity](https://github.com/nknowlton/singularity)
 - License: None

