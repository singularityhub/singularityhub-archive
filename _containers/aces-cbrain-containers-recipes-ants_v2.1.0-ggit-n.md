---
id: 3334
name: "aces/cbrain-containers-recipes"
branch: "master"
tag: "ants_v2.1.0-ggit-n"
commit: "23a694a7fa461f5bf87fc6b05127b704b8deeff7"
version: "85b2f906e08a5853d455554285101e57"
build_date: "2018-06-26T19:08:46.191Z"
size_mb: 790
size: 242905119
sif: "https://datasets.datalad.org/shub/aces/cbrain-containers-recipes/ants_v2.1.0-ggit-n/2018-06-26-23a694a7-85b2f906/85b2f906e08a5853d455554285101e57.simg"
url: https://datasets.datalad.org/shub/aces/cbrain-containers-recipes/ants_v2.1.0-ggit-n/2018-06-26-23a694a7-85b2f906/
recipe: https://datasets.datalad.org/shub/aces/cbrain-containers-recipes/ants_v2.1.0-ggit-n/2018-06-26-23a694a7-85b2f906/Singularity
collection: aces/cbrain-containers-recipes
---

# aces/cbrain-containers-recipes:ants_v2.1.0-ggit-n

```bash
$ singularity pull shub://aces/cbrain-containers-recipes:ants_v2.1.0-ggit-n
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: neurodebian:artful-non-free

#####################################################
#                                                   #
# MCIN (McGill Centre for Integrative Neuroscience) #
#                                                   #
# Singularity recipe for ANTs to build a container  #
# used in CBRAIN (https://github.com/aces/cbrain)   #
#                                                   #
#####################################################

%labels
  Maintainer Natacha Beck

%help
This container provides 'ANTS' Advanced Normalization Tools (ANTS). It is an ITK-based 
suite of normalization, segmentation and template-building tools for quantitative 
morphometric analysis (http://stnava.github.io/ANTs/) 

%post
  apt-get update
  apt-get install -y ants
```

## Collection

 - Name: [aces/cbrain-containers-recipes](https://github.com/aces/cbrain-containers-recipes)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

