---
id: 8986
name: "d-bohn/emorec_aci"
branch: "16.04"
tag: "16.04"
commit: "417fc3670912615cac9313088ee3d4deb31b7c55"
version: "f1cd94fbbad3f774ee13dcaeede1f384"
build_date: "2020-06-29T13:09:51.227Z"
size_mb: 1871
size: 720637983
sif: "https://datasets.datalad.org/shub/d-bohn/emorec_aci/16.04/2020-06-29-417fc367-f1cd94fb/f1cd94fbbad3f774ee13dcaeede1f384.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/d-bohn/emorec_aci/16.04/2020-06-29-417fc367-f1cd94fb/
recipe: https://datasets.datalad.org/shub/d-bohn/emorec_aci/16.04/2020-06-29-417fc367-f1cd94fb/Singularity
collection: d-bohn/emorec_aci
---

# d-bohn/emorec_aci:16.04

```bash
$ singularity pull shub://d-bohn/emorec_aci:16.04
```

## Singularity Recipe

```singularity
BOOTSTRAP: docker
FROM: dalbohn/emorec_aci:16.04

%labels
MAINTAINER Daniel Albohn <d.albohn@gmail.com>

%post
#ACI mappings so you can access your files.
mkdir -p /storage/home
mkdir -p /storage/work
mkdir -p /storage/scratch
mkdir -p /gpfs/group
```

## Collection

 - Name: [d-bohn/emorec_aci](https://github.com/d-bohn/emorec_aci)
 - License: [MIT License](https://api.github.com/licenses/mit)

