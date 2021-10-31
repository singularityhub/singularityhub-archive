---
id: 5343
name: "dshyshlov/UAHPC_Singularity_DyNet"
branch: "master"
tag: "latest"
commit: "73a8ec5648225104601c56d0081dec1ed4999eac"
version: "9e90e0e933310d52faa2927b1d23d9ee"
build_date: "2018-10-24T22:41:52.918Z"
size_mb: 3660
size: 1767055391
sif: "https://datasets.datalad.org/shub/dshyshlov/UAHPC_Singularity_DyNet/latest/2018-10-24-73a8ec56-9e90e0e9/9e90e0e933310d52faa2927b1d23d9ee.simg"
url: https://datasets.datalad.org/shub/dshyshlov/UAHPC_Singularity_DyNet/latest/2018-10-24-73a8ec56-9e90e0e9/
recipe: https://datasets.datalad.org/shub/dshyshlov/UAHPC_Singularity_DyNet/latest/2018-10-24-73a8ec56-9e90e0e9/Singularity
collection: dshyshlov/UAHPC_Singularity_DyNet
---

# dshyshlov/UAHPC_Singularity_DyNet:latest

```bash
$ singularity pull shub://dshyshlov/UAHPC_Singularity_DyNet:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: spellrun/dynet

%post
   # in-container bind points for shared filesystems
   mkdir -p /extra /rsgrps /xdisk /uaopt /cm/shared /cm/local
```

## Collection

 - Name: [dshyshlov/UAHPC_Singularity_DyNet](https://github.com/dshyshlov/UAHPC_Singularity_DyNet)
 - License: None

