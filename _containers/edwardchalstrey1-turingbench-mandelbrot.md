---
id: 9231
name: "edwardchalstrey1/turingbench"
branch: "master"
tag: "mandelbrot"
commit: "fc40b8ed95d1c82870aff8a61a17a323b3298a0e"
version: "faaf283eb49fa378a1995939c2a91dc3"
build_date: "2019-05-23T03:52:52.793Z"
size_mb: 2360
size: 1122873375
sif: "https://datasets.datalad.org/shub/edwardchalstrey1/turingbench/mandelbrot/2019-05-23-fc40b8ed-faaf283e/faaf283eb49fa378a1995939c2a91dc3.simg"
url: https://datasets.datalad.org/shub/edwardchalstrey1/turingbench/mandelbrot/2019-05-23-fc40b8ed-faaf283e/
recipe: https://datasets.datalad.org/shub/edwardchalstrey1/turingbench/mandelbrot/2019-05-23-fc40b8ed-faaf283e/Singularity
collection: edwardchalstrey1/turingbench
---

# edwardchalstrey1/turingbench:mandelbrot

```bash
$ singularity pull shub://edwardchalstrey1/turingbench:mandelbrot
```

## Singularity Recipe

```singularity
BootStrap: docker 
From: edwardchalstrey/mandelbrot

%post
    apt-get -y update

%files      
    mandelbrot.py /mandelbrot.py
```

## Collection

 - Name: [edwardchalstrey1/turingbench](https://github.com/edwardchalstrey1/turingbench)
 - License: None

