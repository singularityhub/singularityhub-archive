---
id: 1050
name: "corinnebosley/singularity-recipes"
branch: "master"
tag: "secret"
commit: "e050c1cd809432353aee942e36029b2172de2da4"
version: "73cdef7b9aef2e46ecf1490c680062ac"
build_date: "2017-12-06T16:44:56.135Z"
size_mb: 131
size: 46370847
sif: "https://datasets.datalad.org/shub/corinnebosley/singularity-recipes/secret/2017-12-06-e050c1cd-73cdef7b/73cdef7b9aef2e46ecf1490c680062ac.simg"
url: https://datasets.datalad.org/shub/corinnebosley/singularity-recipes/secret/2017-12-06-e050c1cd-73cdef7b/
recipe: https://datasets.datalad.org/shub/corinnebosley/singularity-recipes/secret/2017-12-06-e050c1cd-73cdef7b/Singularity
collection: corinnebosley/singularity-recipes
---

# corinnebosley/singularity-recipes:secret

```bash
$ singularity pull shub://corinnebosley/singularity-recipes:secret
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:latest

%runscript
echo "Hi Corinne! Nice glasses"
echo "Psst. Let me tell you a secret" >> secret.txt
```

## Collection

 - Name: [corinnebosley/singularity-recipes](https://github.com/corinnebosley/singularity-recipes)
 - License: None

