---
id: 2818
name: "khanlab/prepT2space"
branch: "master"
tag: "v0.0.1"
commit: "1745d0dcbd1ba3610775d1cf68fe4cfabb8f1197"
version: "694c45ddaf0c85d19613d9948aa4d532"
build_date: "2018-05-18T02:49:51.747Z"
size_mb: 3432
size: 1236414495
sif: "https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1/2018-05-18-1745d0dc-694c45dd/694c45ddaf0c85d19613d9948aa4d532.simg"
url: https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1/2018-05-18-1745d0dc-694c45dd/
recipe: https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1/2018-05-18-1745d0dc-694c45dd/Singularity
collection: khanlab/prepT2space
---

# khanlab/prepT2space:v0.0.1

```bash
$ singularity pull shub://khanlab/prepT2space:v0.0.1
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: khanlab/neuroglia-core-minc:v1.0.0


#########
%setup
#########
mkdir $SINGULARITY_ROOTFS/src
cp -Rv . $SINGULARITY_ROOTFS/src

#########
%post
#########


#########
%environment

%runscript
/src/prepT2space $@
```

## Collection

 - Name: [khanlab/prepT2space](https://github.com/khanlab/prepT2space)
 - License: None

