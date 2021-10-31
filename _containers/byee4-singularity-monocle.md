---
id: 6222
name: "byee4/singularity"
branch: "master"
tag: "monocle"
commit: "0a01841244751d4834f07d9c29066787d10026fe"
version: "5ef16f6c934327dcb7fa9d4df339db57"
build_date: "2019-01-14T21:19:29.844Z"
size_mb: 7838
size: 3500339231
sif: "https://datasets.datalad.org/shub/byee4/singularity/monocle/2019-01-14-0a018412-5ef16f6c/5ef16f6c934327dcb7fa9d4df339db57.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/byee4/singularity/monocle/2019-01-14-0a018412-5ef16f6c/
recipe: https://datasets.datalad.org/shub/byee4/singularity/monocle/2019-01-14-0a018412-5ef16f6c/Singularity
collection: byee4/singularity
---

# byee4/singularity:monocle

```bash
$ singularity pull shub://byee4/singularity:monocle
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: brianyee/r-monocle

%post
  mkdir /oasis
  mkdir /projects

%runscript
  R
```

## Collection

 - Name: [byee4/singularity](https://github.com/byee4/singularity)
 - License: None

