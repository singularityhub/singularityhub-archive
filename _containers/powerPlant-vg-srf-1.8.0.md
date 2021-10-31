---
id: 7027
name: "powerPlant/vg-srf"
branch: "master"
tag: "1.8.0"
commit: "5cd9cc84b348edf811fb48b749ddcf43518f6102"
version: "e996a12e9117f1e12d2b25ccbd0b44ff"
build_date: "2019-02-08T05:38:46.718Z"
size_mb: 597
size: 214487071
sif: "https://datasets.datalad.org/shub/powerPlant/vg-srf/1.8.0/2019-02-08-5cd9cc84-e996a12e/e996a12e9117f1e12d2b25ccbd0b44ff.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/vg-srf/1.8.0/2019-02-08-5cd9cc84-e996a12e/
recipe: https://datasets.datalad.org/shub/powerPlant/vg-srf/1.8.0/2019-02-08-5cd9cc84-e996a12e/Singularity
collection: powerPlant/vg-srf
---

# powerPlant/vg-srf:1.8.0

```bash
$ singularity pull shub://powerPlant/vg-srf:1.8.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: quay.io/vgteam/vg:v1.8.0-0-g3cb239e2-t176-run

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 1.8.0

%runscript
  exec vg "$@"
```

## Collection

 - Name: [powerPlant/vg-srf](https://github.com/powerPlant/vg-srf)
 - License: None

