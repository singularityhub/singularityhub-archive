---
id: 2849
name: "khanlab/prepT2space"
branch: "master"
tag: "v0.0.1c"
commit: "98b0a84b323dc939c911553003354f884cf35113"
version: "b507350e2a1af618e808c3c3e3f60bb5"
build_date: "2018-05-21T16:35:56.273Z"
size_mb: 3432
size: 1236430879
sif: "https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1c/2018-05-21-98b0a84b-b507350e/b507350e2a1af618e808c3c3e3f60bb5.simg"
url: https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1c/2018-05-21-98b0a84b-b507350e/
recipe: https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1c/2018-05-21-98b0a84b-b507350e/Singularity
collection: khanlab/prepT2space
---

# khanlab/prepT2space:v0.0.1c

```bash
$ singularity pull shub://khanlab/prepT2space:v0.0.1c
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

