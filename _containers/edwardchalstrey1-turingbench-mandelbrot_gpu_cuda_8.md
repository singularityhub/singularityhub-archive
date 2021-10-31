---
id: 9234
name: "edwardchalstrey1/turingbench"
branch: "master"
tag: "mandelbrot_gpu_cuda_8"
commit: "55c11cd0894b381bd0cd8b2a4a2ba77521c8963f"
version: "bb43c7101bf176b86f92b7fd027d773e"
build_date: "2019-05-23T03:52:52.787Z"
size_mb: 4274
size: 2519662623
sif: "https://datasets.datalad.org/shub/edwardchalstrey1/turingbench/mandelbrot_gpu_cuda_8/2019-05-23-55c11cd0-bb43c710/bb43c7101bf176b86f92b7fd027d773e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/edwardchalstrey1/turingbench/mandelbrot_gpu_cuda_8/2019-05-23-55c11cd0-bb43c710/
recipe: https://datasets.datalad.org/shub/edwardchalstrey1/turingbench/mandelbrot_gpu_cuda_8/2019-05-23-55c11cd0-bb43c710/Singularity
collection: edwardchalstrey1/turingbench
---

# edwardchalstrey1/turingbench:mandelbrot_gpu_cuda_8

```bash
$ singularity pull shub://edwardchalstrey1/turingbench:mandelbrot_gpu_cuda_8
```

## Singularity Recipe

```singularity
BootStrap: docker 
From: edwardchalstrey/mandelbrot_gpu:cuda8

%post
    apt-get -y update

%files      
    mandelbrot_gpu.py /mandelbrot_gpu.py
```

## Collection

 - Name: [edwardchalstrey1/turingbench](https://github.com/edwardchalstrey1/turingbench)
 - License: None

