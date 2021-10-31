---
id: 8978
name: "d-bohn/emorec_aci"
branch: "master"
tag: "latest"
commit: "7ee69e2f49f63d88da17c590dde6670da60a4c14"
version: "f8c1fb9aa924480acc6e883dafaf0863"
build_date: "2020-06-29T13:05:09.646Z"
size_mb: 2177
size: 843259935
sif: "https://datasets.datalad.org/shub/d-bohn/emorec_aci/latest/2020-06-29-7ee69e2f-f8c1fb9a/f8c1fb9aa924480acc6e883dafaf0863.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/d-bohn/emorec_aci/latest/2020-06-29-7ee69e2f-f8c1fb9a/
recipe: https://datasets.datalad.org/shub/d-bohn/emorec_aci/latest/2020-06-29-7ee69e2f-f8c1fb9a/Singularity
collection: d-bohn/emorec_aci
---

# d-bohn/emorec_aci:latest

```bash
$ singularity pull shub://d-bohn/emorec_aci:latest
```

## Singularity Recipe

```singularity
BOOTSTRAP: docker
FROM: dalbohn/emorec_aci

%labels
MAINTAINER Daniel Albohn <d.albohn@gmail.com>

%post
#ACI mappings so you can access your files.
mkdir -p /storage/home
mkdir -p /storage/work
mkdir -p /gpfs/group
```

## Collection

 - Name: [d-bohn/emorec_aci](https://github.com/d-bohn/emorec_aci)
 - License: [MIT License](https://api.github.com/licenses/mit)

