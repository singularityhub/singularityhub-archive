---
id: 6075
name: "byee4/singularity"
branch: "master"
tag: "makebigwigfiles"
commit: "de01826b947fd772aa7178f38b5430e5f72f0854"
version: "c7f565aab6775bcc172e1b0d8bf210e8"
build_date: "2019-01-01T02:25:06.893Z"
size_mb: 2011
size: 897982495
sif: "https://datasets.datalad.org/shub/byee4/singularity/makebigwigfiles/2019-01-01-de01826b-c7f565aa/c7f565aab6775bcc172e1b0d8bf210e8.simg"
url: https://datasets.datalad.org/shub/byee4/singularity/makebigwigfiles/2019-01-01-de01826b-c7f565aa/
recipe: https://datasets.datalad.org/shub/byee4/singularity/makebigwigfiles/2019-01-01-de01826b-c7f565aa/Singularity
collection: byee4/singularity
---

# byee4/singularity:makebigwigfiles

```bash
$ singularity pull shub://byee4/singularity:makebigwigfiles
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: brianyee/makebigwigfiles

%runscript
  makebigwigfiles

%post

chmod -R 755 /opt
```

## Collection

 - Name: [byee4/singularity](https://github.com/byee4/singularity)
 - License: None

