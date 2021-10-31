---
id: 283
name: "singularityhub/hello-world"
branch: "master"
tag: "latest"
commit: "3f4d63cadba1b3a6867868f9a85417751baba521"
version: "80465f30859a88e8a3b0fb8688738704"
build_date: "2021-04-19T20:01:11.257Z"
size_mb: 197.0
size: 62652447
sif: "https://datasets.datalad.org/shub/singularityhub/hello-world/latest/2021-04-19-3f4d63ca-80465f30/80465f30859a88e8a3b0fb8688738704.sif"
url: https://datasets.datalad.org/shub/singularityhub/hello-world/latest/2021-04-19-3f4d63ca-80465f30/
recipe: https://datasets.datalad.org/shub/singularityhub/hello-world/latest/2021-04-19-3f4d63ca-80465f30/Singularity
collection: singularityhub/hello-world
---

# singularityhub/hello-world:latest

```bash
$ singularity pull shub://singularityhub/hello-world:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:14.04

%runscript

exec echo "Tacotacotaco"
```

## Collection

 - Name: [singularityhub/hello-world](https://github.com/singularityhub/hello-world)
 - License: None

