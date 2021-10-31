---
id: 3327
name: "natacha-beck/cbrain-containers-recipes"
branch: "fct"
tag: "ants"
commit: "8dd3a8d6df6dd9da0183e2556035d03c9c750764"
version: "92365604e6b0e9895a96f68388d785e1"
build_date: "2018-06-26T14:29:40.072Z"
size_mb: 790
size: 242905119
sif: "https://datasets.datalad.org/shub/natacha-beck/cbrain-containers-recipes/ants/2018-06-26-8dd3a8d6-92365604/92365604e6b0e9895a96f68388d785e1.simg"
url: https://datasets.datalad.org/shub/natacha-beck/cbrain-containers-recipes/ants/2018-06-26-8dd3a8d6-92365604/
recipe: https://datasets.datalad.org/shub/natacha-beck/cbrain-containers-recipes/ants/2018-06-26-8dd3a8d6-92365604/Singularity
collection: natacha-beck/cbrain-containers-recipes
---

# natacha-beck/cbrain-containers-recipes:ants

```bash
$ singularity pull shub://natacha-beck/cbrain-containers-recipes:ants
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

 - Name: [natacha-beck/cbrain-containers-recipes](https://github.com/natacha-beck/cbrain-containers-recipes)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

