---
id: 5739
name: "statgen/singularity-epacts"
branch: "master"
tag: "latest"
commit: "668553aa9f47888e764baf70fd71ce9d3a9f6dd5"
version: "28d9e7ba258d492e8c9f682ccbed0b8d"
build_date: "2018-11-29T17:21:08.898Z"
size_mb: 1207
size: 580218911
sif: "https://datasets.datalad.org/shub/statgen/singularity-epacts/latest/2018-11-29-668553aa-28d9e7ba/28d9e7ba258d492e8c9f682ccbed0b8d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/statgen/singularity-epacts/latest/2018-11-29-668553aa-28d9e7ba/
recipe: https://datasets.datalad.org/shub/statgen/singularity-epacts/latest/2018-11-29-668553aa-28d9e7ba/Singularity
collection: statgen/singularity-epacts
---

# statgen/singularity-epacts:latest

```bash
$ singularity pull shub://statgen/singularity-epacts:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: statgen/epacts:dev

%help
  A container for EPACTS.

%environment
  PATH=/usr/local/bin:$PATH

%post
  # post-setup script

  export LC_ALL=C.UTF-8
  export LANG=C.UTF-8
  echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
  echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [statgen/singularity-epacts](https://github.com/statgen/singularity-epacts)
 - License: None

