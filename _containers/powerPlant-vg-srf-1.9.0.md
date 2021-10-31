---
id: 7026
name: "powerPlant/vg-srf"
branch: "master"
tag: "1.9.0"
commit: "5cd9cc84b348edf811fb48b749ddcf43518f6102"
version: "3e74b4653957aa51922ab18c62048797"
build_date: "2019-02-08T05:38:46.725Z"
size_mb: 609
size: 218169375
sif: "https://datasets.datalad.org/shub/powerPlant/vg-srf/1.9.0/2019-02-08-5cd9cc84-3e74b465/3e74b4653957aa51922ab18c62048797.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/vg-srf/1.9.0/2019-02-08-5cd9cc84-3e74b465/
recipe: https://datasets.datalad.org/shub/powerPlant/vg-srf/1.9.0/2019-02-08-5cd9cc84-3e74b465/Singularity
collection: powerPlant/vg-srf
---

# powerPlant/vg-srf:1.9.0

```bash
$ singularity pull shub://powerPlant/vg-srf:1.9.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: quay.io/vgteam/vg:v1.9.0-0-g3286e131-t206-run

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 1.9.0

%runscript
  exec vg "$@"
```

## Collection

 - Name: [powerPlant/vg-srf](https://github.com/powerPlant/vg-srf)
 - License: None

