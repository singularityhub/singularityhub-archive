---
id: 879
name: "rjeschmi/singularity-easybuild"
branch: "master"
tag: "latest"
commit: "4e7f3e70ded398670a320df18b8b4830e4fe1b4e"
version: "7a102099cbe1ace408e1876ffd4e7794"
build_date: "2017-11-21T18:32:10.934Z"
size_mb: 579
size: 194437151
sif: "https://datasets.datalad.org/shub/rjeschmi/singularity-easybuild/latest/2017-11-21-4e7f3e70-7a102099/7a102099cbe1ace408e1876ffd4e7794.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rjeschmi/singularity-easybuild/latest/2017-11-21-4e7f3e70-7a102099/
recipe: https://datasets.datalad.org/shub/rjeschmi/singularity-easybuild/latest/2017-11-21-4e7f3e70-7a102099/Singularity
collection: rjeschmi/singularity-easybuild
---

# rjeschmi/singularity-easybuild:latest

```bash
$ singularity pull shub://rjeschmi/singularity-easybuild:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rjeschmi/easybuild-centos7-singularity

%runscript
 
    exec /usr/bin/ebcleanenv "$@"
```

## Collection

 - Name: [rjeschmi/singularity-easybuild](https://github.com/rjeschmi/singularity-easybuild)
 - License: None

