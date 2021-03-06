---
id: 3335
name: "aces/cbrain-containers-recipes"
branch: "master"
tag: "fsl_v5.0.9"
commit: "23a694a7fa461f5bf87fc6b05127b704b8deeff7"
version: "7b51c2f00bd0f2bbb84fa821f5c18f8f"
build_date: "2018-06-26T19:08:46.196Z"
size_mb: 1898
size: 1460408351
sif: "https://datasets.datalad.org/shub/aces/cbrain-containers-recipes/fsl_v5.0.9/2018-06-26-23a694a7-7b51c2f0/7b51c2f00bd0f2bbb84fa821f5c18f8f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/aces/cbrain-containers-recipes/fsl_v5.0.9/2018-06-26-23a694a7-7b51c2f0/
recipe: https://datasets.datalad.org/shub/aces/cbrain-containers-recipes/fsl_v5.0.9/2018-06-26-23a694a7-7b51c2f0/Singularity
collection: aces/cbrain-containers-recipes
---

# aces/cbrain-containers-recipes:fsl_v5.0.9

```bash
$ singularity pull shub://aces/cbrain-containers-recipes:fsl_v5.0.9
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

 - Name: [aces/cbrain-containers-recipes](https://github.com/aces/cbrain-containers-recipes)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

