---
id: 2291
name: "natacha-beck/containers"
branch: "master"
tag: "fsl-5"
commit: "40b00b2d316979eacf391bf66fb9d1571213edab"
version: "de3da7e0a2d27b50e961717fb1565b35"
build_date: "2018-08-09T15:28:12.807Z"
size_mb: 1901
size: 1460129823
sif: "https://datasets.datalad.org/shub/natacha-beck/containers/fsl-5/2018-08-09-40b00b2d-de3da7e0/de3da7e0a2d27b50e961717fb1565b35.simg"
url: https://datasets.datalad.org/shub/natacha-beck/containers/fsl-5/2018-08-09-40b00b2d-de3da7e0/
recipe: https://datasets.datalad.org/shub/natacha-beck/containers/fsl-5/2018-08-09-40b00b2d-de3da7e0/Singularity
collection: natacha-beck/containers
---

# natacha-beck/containers:fsl-5

```bash
$ singularity pull shub://natacha-beck/containers:fsl-5
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

 - Name: [natacha-beck/containers](https://github.com/natacha-beck/containers)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

