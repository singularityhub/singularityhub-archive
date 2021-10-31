---
id: 3331
name: "natacha-beck/cbrain-containers-recipes"
branch: "fct"
tag: "fsl_v5.0.9"
commit: "6970a17479639ba2f031ccc4272072327714fe0e"
version: "9d4464ac3a9ffc431490daff5e3b11c7"
build_date: "2018-06-26T19:08:46.243Z"
size_mb: 1898
size: 1460404255
sif: "https://datasets.datalad.org/shub/natacha-beck/cbrain-containers-recipes/fsl_v5.0.9/2018-06-26-6970a174-9d4464ac/9d4464ac3a9ffc431490daff5e3b11c7.simg"
url: https://datasets.datalad.org/shub/natacha-beck/cbrain-containers-recipes/fsl_v5.0.9/2018-06-26-6970a174-9d4464ac/
recipe: https://datasets.datalad.org/shub/natacha-beck/cbrain-containers-recipes/fsl_v5.0.9/2018-06-26-6970a174-9d4464ac/Singularity
collection: natacha-beck/cbrain-containers-recipes
---

# natacha-beck/cbrain-containers-recipes:fsl_v5.0.9

```bash
$ singularity pull shub://natacha-beck/cbrain-containers-recipes:fsl_v5.0.9
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: neurodebian:artful-non-free

#####################################################
#                                                   #
# MCIN (McGill Centre for Integrative Neuroscience) #
#                                                   #
# Singularity recipe for FSL to build a container   #
# used in CBRAIN (https://github.com/aces/cbrain)   #
#                                                   #
#####################################################

%labels
  Maintainer Natacha Beck

%help
This container executes any fsl-core command, and it contain all the fsl data too. 
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

