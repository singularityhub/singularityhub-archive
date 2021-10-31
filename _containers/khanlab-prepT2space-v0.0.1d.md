---
id: 2889
name: "khanlab/prepT2space"
branch: "master"
tag: "v0.0.1d"
commit: "bc743feff56bbb2f4c642ee0af0169e1a12b09b9"
version: "7ad6306f7dbe0d61596a185888b596a3"
build_date: "2018-05-23T02:20:46.786Z"
size_mb: 3432
size: 1236434975
sif: "https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1d/2018-05-23-bc743fef-7ad6306f/7ad6306f7dbe0d61596a185888b596a3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/prepT2space/v0.0.1d/2018-05-23-bc743fef-7ad6306f/
recipe: https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1d/2018-05-23-bc743fef-7ad6306f/Singularity
collection: khanlab/prepT2space
---

# khanlab/prepT2space:v0.0.1d

```bash
$ singularity pull shub://khanlab/prepT2space:v0.0.1d
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

