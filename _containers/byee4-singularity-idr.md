---
id: 6074
name: "byee4/singularity"
branch: "master"
tag: "idr"
commit: "de01826b947fd772aa7178f38b5430e5f72f0854"
version: "de4e2f3e1cfeefa5f63ec384209c2eaa"
build_date: "2019-01-01T02:25:06.899Z"
size_mb: 1245
size: 485261343
sif: "https://datasets.datalad.org/shub/byee4/singularity/idr/2019-01-01-de01826b-de4e2f3e/de4e2f3e1cfeefa5f63ec384209c2eaa.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/byee4/singularity/idr/2019-01-01-de01826b-de4e2f3e/
recipe: https://datasets.datalad.org/shub/byee4/singularity/idr/2019-01-01-de01826b-de4e2f3e/Singularity
collection: byee4/singularity
---

# byee4/singularity:idr

```bash
$ singularity pull shub://byee4/singularity:idr
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: brianyee/idr

%runscript
  idr
```

## Collection

 - Name: [byee4/singularity](https://github.com/byee4/singularity)
 - License: None

