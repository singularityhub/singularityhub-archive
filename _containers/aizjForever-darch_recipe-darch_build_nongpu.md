---
id: 2377
name: "aizjForever/darch_recipe"
branch: "master"
tag: "darch_build_nongpu"
commit: "5a560c4fc525664714478e595a2788680f7fedf7"
version: "2e4e2e79c96c779216839c3318732794"
build_date: "2018-06-05T19:17:38.169Z"
size_mb: 1135
size: 458493983
sif: "https://datasets.datalad.org/shub/aizjForever/darch_recipe/darch_build_nongpu/2018-06-05-5a560c4f-2e4e2e79/2e4e2e79c96c779216839c3318732794.simg"
url: https://datasets.datalad.org/shub/aizjForever/darch_recipe/darch_build_nongpu/2018-06-05-5a560c4f-2e4e2e79/
recipe: https://datasets.datalad.org/shub/aizjForever/darch_recipe/darch_build_nongpu/2018-06-05-5a560c4f-2e4e2e79/Singularity
collection: aizjForever/darch_recipe
---

# aizjForever/darch_recipe:darch_build_nongpu

```bash
$ singularity pull shub://aizjForever/darch_recipe:darch_build_nongpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu: 16.04

%post
 apt-get -y update
 apt-get -y install python
 apt-get -y install python-pip python-dev
 pip install tensorflow
 pip install scipy
 pip install numpy
 pip install sklearn
 pip install keras
 pip install matplotlib
 pip install progressbar
 
%environment
 export LC_ALL=C
```

## Collection

 - Name: [aizjForever/darch_recipe](https://github.com/aizjForever/darch_recipe)
 - License: None

