---
id: 10318
name: "singularityhub/tiny-container"
branch: "master"
tag: "tiny"
commit: "b103475493343c34e20c9ea876c8a1e6a55d9ff3"
version: "3bdf35f386e517db23c0a93caa73e92489118261b315e3337bac0fa7a27702a0"
build_date: "2019-08-05T20:58:14.176Z"
size_mb: 0.74609375
size: 782336
sif: "https://datasets.datalad.org/shub/singularityhub/tiny-container/tiny/2019-08-05-b1034754-3bdf35f3/3bdf35f386e517db23c0a93caa73e92489118261b315e3337bac0fa7a27702a0.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/singularityhub/tiny-container/tiny/2019-08-05-b1034754-3bdf35f3/
recipe: https://datasets.datalad.org/shub/singularityhub/tiny-container/tiny/2019-08-05-b1034754-3bdf35f3/Singularity
collection: singularityhub/tiny-container
---

# singularityhub/tiny-container:tiny

```bash
$ singularity pull shub://singularityhub/tiny-container:tiny
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: busybox:latest

%runscript
echo "This is the tiny container... so tiny :D"
```

## Collection

 - Name: [singularityhub/tiny-container](https://github.com/singularityhub/tiny-container)
 - License: None

