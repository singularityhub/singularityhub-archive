---
id: 2820
name: "khanlab/prepT2space"
branch: "master"
tag: "v0.0.1a"
commit: "3f50d8499af813b132359fd1d965fdbee524365b"
version: "2e805f35dee4413d565b62b46a59677e"
build_date: "2018-05-18T07:40:56.300Z"
size_mb: 3432
size: 1236422687
sif: "https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1a/2018-05-18-3f50d849-2e805f35/2e805f35dee4413d565b62b46a59677e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/prepT2space/v0.0.1a/2018-05-18-3f50d849-2e805f35/
recipe: https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1a/2018-05-18-3f50d849-2e805f35/Singularity
collection: khanlab/prepT2space
---

# khanlab/prepT2space:v0.0.1a

```bash
$ singularity pull shub://khanlab/prepT2space:v0.0.1a
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

