---
id: 9230
name: "edwardchalstrey1/turingbench"
branch: "master"
tag: "mandelbrot_gpu"
commit: "fc40b8ed95d1c82870aff8a61a17a323b3298a0e"
version: "998f4d0ae99c1cc6ef9b90f55ef14675"
build_date: "2020-09-22T14:36:26.700Z"
size_mb: 4580
size: 2718154783
sif: "https://datasets.datalad.org/shub/edwardchalstrey1/turingbench/mandelbrot_gpu/2020-09-22-fc40b8ed-998f4d0a/998f4d0ae99c1cc6ef9b90f55ef14675.simg"
url: https://datasets.datalad.org/shub/edwardchalstrey1/turingbench/mandelbrot_gpu/2020-09-22-fc40b8ed-998f4d0a/
recipe: https://datasets.datalad.org/shub/edwardchalstrey1/turingbench/mandelbrot_gpu/2020-09-22-fc40b8ed-998f4d0a/Singularity
collection: edwardchalstrey1/turingbench
---

# edwardchalstrey1/turingbench:mandelbrot_gpu

```bash
$ singularity pull shub://edwardchalstrey1/turingbench:mandelbrot_gpu
```

## Singularity Recipe

```singularity
BootStrap: docker 
From: edwardchalstrey/mandelbrot_gpu

%post
    apt-get -y update

%files      
    mandelbrot_gpu.py /mandelbrot_gpu.py
```

## Collection

 - Name: [edwardchalstrey1/turingbench](https://github.com/edwardchalstrey1/turingbench)
 - License: None

