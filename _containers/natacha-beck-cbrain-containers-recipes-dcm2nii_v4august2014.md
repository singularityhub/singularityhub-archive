---
id: 3332
name: "natacha-beck/cbrain-containers-recipes"
branch: "fct"
tag: "dcm2nii_v4august2014"
commit: "6970a17479639ba2f031ccc4272072327714fe0e"
version: "05efb0119181683219c4610698c11ffb"
build_date: "2018-06-26T19:08:46.237Z"
size_mb: 249
size: 102080543
sif: "https://datasets.datalad.org/shub/natacha-beck/cbrain-containers-recipes/dcm2nii_v4august2014/2018-06-26-6970a174-05efb011/05efb0119181683219c4610698c11ffb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/natacha-beck/cbrain-containers-recipes/dcm2nii_v4august2014/2018-06-26-6970a174-05efb011/
recipe: https://datasets.datalad.org/shub/natacha-beck/cbrain-containers-recipes/dcm2nii_v4august2014/2018-06-26-6970a174-05efb011/Singularity
collection: natacha-beck/cbrain-containers-recipes
---

# natacha-beck/cbrain-containers-recipes:dcm2nii_v4august2014

```bash
$ singularity pull shub://natacha-beck/cbrain-containers-recipes:dcm2nii_v4august2014
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: neurodebian:artful-non-free


#######################################################
#                                                     #
# MCIN (McGill Centre for Integrative Neuroscience)   #
#                                                     #
# Singularity recipe for dcm2nii to build a container #
# used in CBRAIN (https://github.com/aces/cbrain)     #
#                                                     #
#######################################################

%labels
  Maintainer Natacha Beck

%help
This container provides 'dcm2nii'i from the mricron package.
That supports converting DICOM and PAR/REC images into the NIfTI format. 
http://people.cas.sc.edu/rorden/mricron/index.html  

%post
  apt-get update
  apt-get install -y mricron
```

## Collection

 - Name: [natacha-beck/cbrain-containers-recipes](https://github.com/natacha-beck/cbrain-containers-recipes)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

