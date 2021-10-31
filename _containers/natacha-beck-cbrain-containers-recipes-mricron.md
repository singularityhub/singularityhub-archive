---
id: 3329
name: "natacha-beck/cbrain-containers-recipes"
branch: "fct"
tag: "mricron"
commit: "8dd3a8d6df6dd9da0183e2556035d03c9c750764"
version: "0284f49de305a1eb72fd2ff8d706c606"
build_date: "2018-06-26T14:29:40.060Z"
size_mb: 249
size: 102080543
sif: "https://datasets.datalad.org/shub/natacha-beck/cbrain-containers-recipes/mricron/2018-06-26-8dd3a8d6-0284f49d/0284f49de305a1eb72fd2ff8d706c606.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/natacha-beck/cbrain-containers-recipes/mricron/2018-06-26-8dd3a8d6-0284f49d/
recipe: https://datasets.datalad.org/shub/natacha-beck/cbrain-containers-recipes/mricron/2018-06-26-8dd3a8d6-0284f49d/Singularity
collection: natacha-beck/cbrain-containers-recipes
---

# natacha-beck/cbrain-containers-recipes:mricron

```bash
$ singularity pull shub://natacha-beck/cbrain-containers-recipes:mricron
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: neurodebian:artful-non-free

%labels
  Maintainer Natacha Beck

%help
This container provides 'dcm2nii' that supports converting DICOM 
and PAR/REC images into the NIfTI format, from the mricron package. 
http://people.cas.sc.edu/rorden/mricron/index.html  

%post
  apt-get update
  apt-get install -y mricron
```

## Collection

 - Name: [natacha-beck/cbrain-containers-recipes](https://github.com/natacha-beck/cbrain-containers-recipes)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

