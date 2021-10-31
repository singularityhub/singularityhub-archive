---
id: 9337
name: "alan0415/Singularity-build"
branch: "master"
tag: "v1"
commit: "636a4d897c5f147aa0ebeb56c976180c0b1d076e"
version: "3e7f49c51fc726f4f2827b56363e4109"
build_date: "2019-05-26T05:45:57.619Z"
size_mb: 13767
size: 4569153567
sif: "https://datasets.datalad.org/shub/alan0415/Singularity-build/v1/2019-05-26-636a4d89-3e7f49c5/3e7f49c51fc726f4f2827b56363e4109.simg"
url: https://datasets.datalad.org/shub/alan0415/Singularity-build/v1/2019-05-26-636a4d89-3e7f49c5/
recipe: https://datasets.datalad.org/shub/alan0415/Singularity-build/v1/2019-05-26-636a4d89-3e7f49c5/Singularity
collection: alan0415/Singularity-build
---

# alan0415/Singularity-build:v1

```bash
$ singularity pull shub://alan0415/Singularity-build:v1
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From: alan0415/cp2k_omp3.1.2_cuda10:1.0

apt-get -y install iputils-ping
apt -y install net-tools
```

## Collection

 - Name: [alan0415/Singularity-build](https://github.com/alan0415/Singularity-build)
 - License: None

