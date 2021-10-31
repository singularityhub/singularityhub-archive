---
id: 391
name: "singularityhub/hello-registry"
branch: "master"
tag: "14.04"
commit: "d7cb6fa8c4f45f6ba589ce6c0c2a78c4e93225ee"
version: "1f5854c6142eb170bea1acefd523eb24"
build_date: "2017-10-18T13:21:46.591Z"
size_mb: 333
size: 65347615
sif: "https://datasets.datalad.org/shub/singularityhub/hello-registry/14.04/2017-10-18-d7cb6fa8-1f5854c6/1f5854c6142eb170bea1acefd523eb24.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/singularityhub/hello-registry/14.04/2017-10-18-d7cb6fa8-1f5854c6/
recipe: https://datasets.datalad.org/shub/singularityhub/hello-registry/14.04/2017-10-18-d7cb6fa8-1f5854c6/Singularity
collection: singularityhub/hello-registry
---

# singularityhub/hello-registry:14.04

```bash
$ singularity pull shub://singularityhub/hello-registry:14.04
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:14.04

%runscript

exec echo "This is for ubuntu 14.04"
```

## Collection

 - Name: [singularityhub/hello-registry](https://github.com/singularityhub/hello-registry)
 - License: None

