---
id: 1992
name: "markxiao/fsl"
branch: "master"
tag: "latest"
commit: "68d4507cd9b4580442f16a7807bb61555ff3ffd2"
version: "eb811b73cbccd3254b9a4d186e23da2d"
build_date: "2020-06-18T16:32:32.559Z"
size_mb: 5764
size: 2516492319
sif: "https://datasets.datalad.org/shub/markxiao/fsl/latest/2020-06-18-68d4507c-eb811b73/eb811b73cbccd3254b9a4d186e23da2d.simg"
url: https://datasets.datalad.org/shub/markxiao/fsl/latest/2020-06-18-68d4507c-eb811b73/
recipe: https://datasets.datalad.org/shub/markxiao/fsl/latest/2020-06-18-68d4507c-eb811b73/Singularity
collection: markxiao/fsl
---

# markxiao/fsl:latest

```bash
$ singularity pull shub://markxiao/fsl:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: mustxyk/fsl:latest

%environment

PATH=/usr/local/fsl/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
FSLDIR=/usr/local/fsl

export PATH FSLDIR
```

## Collection

 - Name: [markxiao/fsl](https://github.com/markxiao/fsl)
 - License: None

