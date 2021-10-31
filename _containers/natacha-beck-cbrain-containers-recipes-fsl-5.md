---
id: 3328
name: "natacha-beck/cbrain-containers-recipes"
branch: "fct"
tag: "fsl-5"
commit: "8dd3a8d6df6dd9da0183e2556035d03c9c750764"
version: "f0802614d18c08b916f0d0434623401b"
build_date: "2018-06-26T14:29:40.066Z"
size_mb: 1898
size: 1460404255
sif: "https://datasets.datalad.org/shub/natacha-beck/cbrain-containers-recipes/fsl-5/2018-06-26-8dd3a8d6-f0802614/f0802614d18c08b916f0d0434623401b.simg"
url: https://datasets.datalad.org/shub/natacha-beck/cbrain-containers-recipes/fsl-5/2018-06-26-8dd3a8d6-f0802614/
recipe: https://datasets.datalad.org/shub/natacha-beck/cbrain-containers-recipes/fsl-5/2018-06-26-8dd3a8d6-f0802614/Singularity
collection: natacha-beck/cbrain-containers-recipes
---

# natacha-beck/cbrain-containers-recipes:fsl-5

```bash
$ singularity pull shub://natacha-beck/cbrain-containers-recipes:fsl-5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: neurodebian:artful-non-free

%labels
  Maintainer Natacha Beck

%help
This container execute any fsl-core command it contain all the fsl data too. 
For more information see FSL website: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki

%post
  apt-get update
  apt-get install -y fsl-complete

%environment
  export FSLDIR=/usr/share/fsl/5.0 
  export FSLOUTPUTTYPE=NIFTI_GZ 
  export PATH=/usr/lib/fsl/5.0:$PATH 
  export FSLMULTIFILEQUIT=TRUE 
  export POSSUMDIR=/usr/share/fsl/5.0 
  export LD_LIBRARY_PATH=/usr/lib/fsl/5.0:$LD_LIBRARY_PATH 
  export FSLTCLSH=/usr/bin/tclsh 
  export FSLWISH=/usr/bin/wish 
  export FSLOUTPUTTYPE=NIFTI_GZ
```

## Collection

 - Name: [natacha-beck/cbrain-containers-recipes](https://github.com/natacha-beck/cbrain-containers-recipes)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

