---
id: 3067
name: "Martybird/7TBEaST"
branch: "master"
tag: "v0.0.1a"
commit: "df3b0f3298679cc35bfe3f390169e755f9844ac5"
version: "f9c3d0ca6f4f2ae85afb1a3a5b2612d3"
build_date: "2018-06-07T10:20:39.587Z"
size_mb: 3432
size: 1236385823
sif: "https://datasets.datalad.org/shub/Martybird/7TBEaST/v0.0.1a/2018-06-07-df3b0f32-f9c3d0ca/f9c3d0ca6f4f2ae85afb1a3a5b2612d3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Martybird/7TBEaST/v0.0.1a/2018-06-07-df3b0f32-f9c3d0ca/
recipe: https://datasets.datalad.org/shub/Martybird/7TBEaST/v0.0.1a/2018-06-07-df3b0f32-f9c3d0ca/Singularity
collection: Martybird/7TBEaST
---

# Martybird/7TBEaST:v0.0.1a

```bash
$ singularity pull shub://Martybird/7TBEaST:v0.0.1a
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
/src/7TBEAST $@
```

## Collection

 - Name: [Martybird/7TBEaST](https://github.com/Martybird/7TBEaST)
 - License: None

