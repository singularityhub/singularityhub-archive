---
id: 6072
name: "byee4/singularity"
branch: "master"
tag: "cutadapt"
commit: "de01826b947fd772aa7178f38b5430e5f72f0854"
version: "e5446fc8f958c2996cf40a95be0554bd"
build_date: "2019-01-01T02:25:06.911Z"
size_mb: 757
size: 279371807
sif: "https://datasets.datalad.org/shub/byee4/singularity/cutadapt/2019-01-01-de01826b-e5446fc8/e5446fc8f958c2996cf40a95be0554bd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/byee4/singularity/cutadapt/2019-01-01-de01826b-e5446fc8/
recipe: https://datasets.datalad.org/shub/byee4/singularity/cutadapt/2019-01-01-de01826b-e5446fc8/Singularity
collection: byee4/singularity
---

# byee4/singularity:cutadapt

```bash
$ singularity pull shub://byee4/singularity:cutadapt
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: brianyee/cutadapt

%runscript
  cutadapt

%post
chmod -R 755 /opt
```

## Collection

 - Name: [byee4/singularity](https://github.com/byee4/singularity)
 - License: None

