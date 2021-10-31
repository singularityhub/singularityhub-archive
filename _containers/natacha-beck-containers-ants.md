---
id: 2295
name: "natacha-beck/containers"
branch: "master"
tag: "ants"
commit: "904d8053cdbd71f016f10cf95f5b748fa2c9d572"
version: "a28aa0cf42879f2553b39c889def32f9"
build_date: "2018-08-09T15:28:12.788Z"
size_mb: 794
size: 242348063
sif: "https://datasets.datalad.org/shub/natacha-beck/containers/ants/2018-08-09-904d8053-a28aa0cf/a28aa0cf42879f2553b39c889def32f9.simg"
url: https://datasets.datalad.org/shub/natacha-beck/containers/ants/2018-08-09-904d8053-a28aa0cf/
recipe: https://datasets.datalad.org/shub/natacha-beck/containers/ants/2018-08-09-904d8053-a28aa0cf/Singularity
collection: natacha-beck/containers
---

# natacha-beck/containers:ants

```bash
$ singularity pull shub://natacha-beck/containers:ants
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: neurodebian:artful-non-free

%labels
  Maintainer Natacha Beck

%help
This container provides 'ANTS' Advanced Normalization Tools (ANTS) is an ITK-based 
suite of normalization, segmentation and template-building tools for quantitative 
morphometric analysis (http://stnava.github.io/ANTs/) 

%post
  apt-get update
  apt-get install -y ants
```

## Collection

 - Name: [natacha-beck/containers](https://github.com/natacha-beck/containers)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

