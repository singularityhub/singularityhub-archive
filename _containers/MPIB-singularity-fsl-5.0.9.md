---
id: 5358
name: "MPIB/singularity-fsl"
branch: "master"
tag: "5.0.9"
commit: "72f1169a41bb76b75835784f34ce34f956d4085f"
version: "7c4df43f65e4e66c7a5114bd5c56179f"
build_date: "2019-07-24T12:28:54.443Z"
size_mb: 2015
size: 1502879775
sif: "https://datasets.datalad.org/shub/MPIB/singularity-fsl/5.0.9/2019-07-24-72f1169a-7c4df43f/7c4df43f65e4e66c7a5114bd5c56179f.simg"
url: https://datasets.datalad.org/shub/MPIB/singularity-fsl/5.0.9/2019-07-24-72f1169a-7c4df43f/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-fsl/5.0.9/2019-07-24-72f1169a-7c4df43f/Singularity
collection: MPIB/singularity-fsl
---

# MPIB/singularity-fsl:5.0.9

```bash
$ singularity pull shub://MPIB/singularity-fsl:5.0.9
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: neurodebian:non-free

%labels
    AUTHOR krause@mpib-berlin.mpg.de

%post
    apt-get update
    apt-get -y install fsl-5.0-complete

%environment
    . ${FSLDIR}/etc/fsl/5.0/fsl.sh
```

## Collection

 - Name: [MPIB/singularity-fsl](https://github.com/MPIB/singularity-fsl)
 - License: None

