---
id: 8458
name: "d-bohn/openface_aci"
branch: "master"
tag: "latest"
commit: "ffd67b39cce3c803411424bf4e88f8786109fedf"
version: "60695a3139b31f578320703856fbb0d8"
build_date: "2021-04-14T17:50:01.363Z"
size_mb: 5707
size: 3552276511
sif: "https://datasets.datalad.org/shub/d-bohn/openface_aci/latest/2021-04-14-ffd67b39-60695a31/60695a3139b31f578320703856fbb0d8.simg"
url: https://datasets.datalad.org/shub/d-bohn/openface_aci/latest/2021-04-14-ffd67b39-60695a31/
recipe: https://datasets.datalad.org/shub/d-bohn/openface_aci/latest/2021-04-14-ffd67b39-60695a31/Singularity
collection: d-bohn/openface_aci
---

# d-bohn/openface_aci:latest

```bash
$ singularity pull shub://d-bohn/openface_aci:latest
```

## Singularity Recipe

```singularity
BOOTSTRAP: docker
FROM: dalbohn/openface_ics

%labels
MAINTAINER Daniel Albohn <d.albohn@gmail.com>

%post
#ACI mappings so you can access your files.
mkdir -p /storage/home
mkdir -p /storage/work
# mkdir -p /gpfs/group
# mkdir -p /gpfs/scratch
```

## Collection

 - Name: [d-bohn/openface_aci](https://github.com/d-bohn/openface_aci)
 - License: None

