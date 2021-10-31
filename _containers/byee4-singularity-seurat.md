---
id: 6221
name: "byee4/singularity"
branch: "master"
tag: "seurat"
commit: "0a01841244751d4834f07d9c29066787d10026fe"
version: "aaa056581abc222dbc2ac074ccda69c9"
build_date: "2019-01-14T21:19:29.835Z"
size_mb: 7863
size: 3511308319
sif: "https://datasets.datalad.org/shub/byee4/singularity/seurat/2019-01-14-0a018412-aaa05658/aaa056581abc222dbc2ac074ccda69c9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/byee4/singularity/seurat/2019-01-14-0a018412-aaa05658/
recipe: https://datasets.datalad.org/shub/byee4/singularity/seurat/2019-01-14-0a018412-aaa05658/Singularity
collection: byee4/singularity
---

# byee4/singularity:seurat

```bash
$ singularity pull shub://byee4/singularity:seurat
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: brianyee/r-seurat

%post
  mkdir /oasis
  mkdir /projects

%runscript
  R
```

## Collection

 - Name: [byee4/singularity](https://github.com/byee4/singularity)
 - License: None

