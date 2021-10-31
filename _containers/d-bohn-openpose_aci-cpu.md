---
id: 9498
name: "d-bohn/openpose_aci"
branch: "gpu"
tag: "cpu"
commit: "5ced7ecebed9272fe7de6a6e7f35292864cb0a4c"
version: "6f620d19bc98119a58faa6a0dffaa70b"
build_date: "2019-06-03T16:24:55.009Z"
size_mb: 3717
size: 1864470559
sif: "https://datasets.datalad.org/shub/d-bohn/openpose_aci/cpu/2019-06-03-5ced7ece-6f620d19/6f620d19bc98119a58faa6a0dffaa70b.simg"
url: https://datasets.datalad.org/shub/d-bohn/openpose_aci/cpu/2019-06-03-5ced7ece-6f620d19/
recipe: https://datasets.datalad.org/shub/d-bohn/openpose_aci/cpu/2019-06-03-5ced7ece-6f620d19/Singularity
collection: d-bohn/openpose_aci
---

# d-bohn/openpose_aci:cpu

```bash
$ singularity pull shub://d-bohn/openpose_aci:cpu
```

## Singularity Recipe

```singularity
BOOTSTRAP: docker
FROM: dalbohn/openpose_aci:cpu

%labels
MAINTAINER Daniel Albohn <d.albohn@gmail.com>

%post
#ACI mappings so you can access your files.
mkdir -p /storage/home
mkdir -p /storage/work
mkdir -p /gpfs/group
```

## Collection

 - Name: [d-bohn/openpose_aci](https://github.com/d-bohn/openpose_aci)
 - License: None

