---
id: 4601
name: "aces/cbrain-containers-recipes"
branch: "master"
tag: "dcm2nii_v4august2014"
commit: "83b9287b742619b7dc864fbe24b160fecb8a262e"
version: "f488dd1ab39424afbe6e3d6e1369dd7f"
build_date: "2018-08-31T19:20:29.107Z"
size_mb: 249
size: 102080543
sif: "https://datasets.datalad.org/shub/aces/cbrain-containers-recipes/dcm2nii_v4august2014/2018-08-31-83b9287b-f488dd1a/f488dd1ab39424afbe6e3d6e1369dd7f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/aces/cbrain-containers-recipes/dcm2nii_v4august2014/2018-08-31-83b9287b-f488dd1a/
recipe: https://datasets.datalad.org/shub/aces/cbrain-containers-recipes/dcm2nii_v4august2014/2018-08-31-83b9287b-f488dd1a/Singularity
collection: aces/cbrain-containers-recipes
---

# aces/cbrain-containers-recipes:dcm2nii_v4august2014

```bash
$ singularity pull shub://aces/cbrain-containers-recipes:dcm2nii_v4august2014
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
This container provides 'dcm2nii' from the mricron package.
That supports converting DICOM and PAR/REC images into the NIfTI format. 
http://people.cas.sc.edu/rorden/mricron/index.html  

%post
  apt-get update
  apt-get install -y mricron
```

## Collection

 - Name: [aces/cbrain-containers-recipes](https://github.com/aces/cbrain-containers-recipes)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

