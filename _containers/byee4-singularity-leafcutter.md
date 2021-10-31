---
id: 6218
name: "byee4/singularity"
branch: "master"
tag: "leafcutter"
commit: "c884e2fde196ca3066390d83dc22342ded73278a"
version: "57dd30e31d6a676e133fdca6e30d5eb3"
build_date: "2019-01-14T04:37:52.010Z"
size_mb: 7811
size: 3472936991
sif: "https://datasets.datalad.org/shub/byee4/singularity/leafcutter/2019-01-14-c884e2fd-57dd30e3/57dd30e31d6a676e133fdca6e30d5eb3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/byee4/singularity/leafcutter/2019-01-14-c884e2fd-57dd30e3/
recipe: https://datasets.datalad.org/shub/byee4/singularity/leafcutter/2019-01-14-c884e2fd-57dd30e3/Singularity
collection: byee4/singularity
---

# byee4/singularity:leafcutter

```bash
$ singularity pull shub://byee4/singularity:leafcutter
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

 - Name: [byee4/singularity](https://github.com/byee4/singularity)
 - License: None

