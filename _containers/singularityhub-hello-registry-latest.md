---
id: 390
name: "singularityhub/hello-registry"
branch: "master"
tag: "latest"
commit: "3f4d63cadba1b3a6867868f9a85417751baba521"
version: "22aa66e0c80847c676f34f35e70ea066"
build_date: "2017-10-18T17:55:06.034Z"
size_mb: 341
size: 65347615
sif: "https://datasets.datalad.org/shub/singularityhub/hello-registry/latest/2017-10-18-3f4d63ca-22aa66e0/22aa66e0c80847c676f34f35e70ea066.simg"
url: https://datasets.datalad.org/shub/singularityhub/hello-registry/latest/2017-10-18-3f4d63ca-22aa66e0/
recipe: https://datasets.datalad.org/shub/singularityhub/hello-registry/latest/2017-10-18-3f4d63ca-22aa66e0/Singularity
collection: singularityhub/hello-registry
---

# singularityhub/hello-registry:latest

```bash
$ singularity pull shub://singularityhub/hello-registry:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:14.04

%runscript

exec echo "Tacotacotaco"
```

## Collection

 - Name: [singularityhub/hello-registry](https://github.com/singularityhub/hello-registry)
 - License: None

