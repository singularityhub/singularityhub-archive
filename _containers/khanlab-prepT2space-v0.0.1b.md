---
id: 2848
name: "khanlab/prepT2space"
branch: "master"
tag: "v0.0.1b"
commit: "32652c0f4d745b34f3fedf9222ff9c9f49c08f5e"
version: "b9dabfc5fd0e4b37d0cbc08b543e255e"
build_date: "2018-05-21T16:35:56.279Z"
size_mb: 3432
size: 1236430879
sif: "https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1b/2018-05-21-32652c0f-b9dabfc5/b9dabfc5fd0e4b37d0cbc08b543e255e.simg"
url: https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1b/2018-05-21-32652c0f-b9dabfc5/
recipe: https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1b/2018-05-21-32652c0f-b9dabfc5/Singularity
collection: khanlab/prepT2space
---

# khanlab/prepT2space:v0.0.1b

```bash
$ singularity pull shub://khanlab/prepT2space:v0.0.1b
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

