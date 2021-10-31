---
id: 9499
name: "d-bohn/openpose_aci"
branch: "gpu"
tag: "latest"
commit: "627b80015a63d7aeee70258437f15ea14211c0b2"
version: "a0b0743a65d38b80660bd51c359da470"
build_date: "2019-06-03T16:24:55.002Z"
size_mb: 5331
size: 3206311967
sif: "https://datasets.datalad.org/shub/d-bohn/openpose_aci/latest/2019-06-03-627b8001-a0b0743a/a0b0743a65d38b80660bd51c359da470.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/d-bohn/openpose_aci/latest/2019-06-03-627b8001-a0b0743a/
recipe: https://datasets.datalad.org/shub/d-bohn/openpose_aci/latest/2019-06-03-627b8001-a0b0743a/Singularity
collection: d-bohn/openpose_aci
---

# d-bohn/openpose_aci:latest

```bash
$ singularity pull shub://d-bohn/openpose_aci:latest
```

## Singularity Recipe

```singularity
BOOTSTRAP: docker
FROM: dalbohn/openpose_aci

%labels
MAINTAINER Daniel Albohn <d.albohn@gmail.com>

%post
#ACI mappings so you can access your files.
mkdir -p /storage/home
mkdir -p /storage/work
mkdir -p /gpfs/group
mkdir -p /gpfs/scratch
mkdir -p /var/spool/torque
```

## Collection

 - Name: [d-bohn/openpose_aci](https://github.com/d-bohn/openpose_aci)
 - License: None

