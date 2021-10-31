---
id: 10057
name: "d-bohn/yolo_aci"
branch: "master"
tag: "latest"
commit: "48d769732d16cb7a7ea29127eb183ab65b3d95c1"
version: "37f7241c798489d11c9319e3c31886b6"
build_date: "2019-06-28T07:13:44.831Z"
size_mb: 4107
size: 2046128159
sif: "https://datasets.datalad.org/shub/d-bohn/yolo_aci/latest/2019-06-28-48d76973-37f7241c/37f7241c798489d11c9319e3c31886b6.simg"
url: https://datasets.datalad.org/shub/d-bohn/yolo_aci/latest/2019-06-28-48d76973-37f7241c/
recipe: https://datasets.datalad.org/shub/d-bohn/yolo_aci/latest/2019-06-28-48d76973-37f7241c/Singularity
collection: d-bohn/yolo_aci
---

# d-bohn/yolo_aci:latest

```bash
$ singularity pull shub://d-bohn/yolo_aci:latest
```

## Singularity Recipe

```singularity
BOOTSTRAP: docker
FROM: dalbohn/yolo_aci

%labels
MAINTAINER Daniel Albohn <d.albohn@gmail.com>
VERSION v1.4

%post
# ACI mappings so you can access your files.
mkdir -p /storage/home
mkdir -p /storage/work
mkdir -p /gpfs/group
mkdir -p /gpfs/scratch
```

## Collection

 - Name: [d-bohn/yolo_aci](https://github.com/d-bohn/yolo_aci)
 - License: None

