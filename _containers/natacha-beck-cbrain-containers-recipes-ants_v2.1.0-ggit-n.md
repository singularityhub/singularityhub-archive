---
id: 3330
name: "natacha-beck/cbrain-containers-recipes"
branch: "fct"
tag: "ants_v2.1.0-ggit-n"
commit: "6970a17479639ba2f031ccc4272072327714fe0e"
version: "9d2a03cf24c5ba078fc9b2fff126aa66"
build_date: "2018-06-26T19:08:46.249Z"
size_mb: 790
size: 242901023
sif: "https://datasets.datalad.org/shub/natacha-beck/cbrain-containers-recipes/ants_v2.1.0-ggit-n/2018-06-26-6970a174-9d2a03cf/9d2a03cf24c5ba078fc9b2fff126aa66.simg"
url: https://datasets.datalad.org/shub/natacha-beck/cbrain-containers-recipes/ants_v2.1.0-ggit-n/2018-06-26-6970a174-9d2a03cf/
recipe: https://datasets.datalad.org/shub/natacha-beck/cbrain-containers-recipes/ants_v2.1.0-ggit-n/2018-06-26-6970a174-9d2a03cf/Singularity
collection: natacha-beck/cbrain-containers-recipes
---

# natacha-beck/cbrain-containers-recipes:ants_v2.1.0-ggit-n

```bash
$ singularity pull shub://natacha-beck/cbrain-containers-recipes:ants_v2.1.0-ggit-n
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

 - Name: [natacha-beck/cbrain-containers-recipes](https://github.com/natacha-beck/cbrain-containers-recipes)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

