---
id: 13624
name: "bernt-matthias/hello-world-singularity"
branch: "master"
tag: "latest"
commit: "e4fa018905efcf4b4b90f1dd66511ae13db37c3d"
version: "917b2d264961689029d4d2d4635ede0a"
build_date: "2020-07-15T11:57:16.185Z"
size_mb: 96.0
size: 37060639
sif: "https://datasets.datalad.org/shub/bernt-matthias/hello-world-singularity/latest/2020-07-15-e4fa0189-917b2d26/917b2d264961689029d4d2d4635ede0a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/bernt-matthias/hello-world-singularity/latest/2020-07-15-e4fa0189-917b2d26/
recipe: https://datasets.datalad.org/shub/bernt-matthias/hello-world-singularity/latest/2020-07-15-e4fa0189-917b2d26/Singularity
collection: bernt-matthias/hello-world-singularity
---

# bernt-matthias/hello-world-singularity:latest

```bash
$ singularity pull shub://bernt-matthias/hello-world-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%runscript
    exec echo "Polo $@!"
```

## Collection

 - Name: [bernt-matthias/hello-world-singularity](https://github.com/bernt-matthias/hello-world-singularity)
 - License: None

