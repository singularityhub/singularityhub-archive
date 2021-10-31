---
id: 7014
name: "powerPlant/vg-srf"
branch: "master"
tag: "1.12.0"
commit: "65a82f32f2607dce15bb5a435df8d620919bf893"
version: "520bc1698d52ae2af139dd1f07ad00e2"
build_date: "2019-02-08T05:38:46.737Z"
size_mb: 613
size: 213250079
sif: "https://datasets.datalad.org/shub/powerPlant/vg-srf/1.12.0/2019-02-08-65a82f32-520bc169/520bc1698d52ae2af139dd1f07ad00e2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/vg-srf/1.12.0/2019-02-08-65a82f32-520bc169/
recipe: https://datasets.datalad.org/shub/powerPlant/vg-srf/1.12.0/2019-02-08-65a82f32-520bc169/Singularity
collection: powerPlant/vg-srf
---

# powerPlant/vg-srf:1.12.0

```bash
$ singularity pull shub://powerPlant/vg-srf:1.12.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: quay.io/vgteam/vg:v1.12.0

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 1.12.0

%runscript
  exec vg "$@"
```

## Collection

 - Name: [powerPlant/vg-srf](https://github.com/powerPlant/vg-srf)
 - License: None

