---
id: 7013
name: "powerPlant/vg-srf"
branch: "master"
tag: "1.11.0"
commit: "65a82f32f2607dce15bb5a435df8d620919bf893"
version: "b005ac8e35fec51e268dea67453aaf56"
build_date: "2019-02-08T05:38:46.754Z"
size_mb: 617
size: 221077535
sif: "https://datasets.datalad.org/shub/powerPlant/vg-srf/1.11.0/2019-02-08-65a82f32-b005ac8e/b005ac8e35fec51e268dea67453aaf56.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/vg-srf/1.11.0/2019-02-08-65a82f32-b005ac8e/
recipe: https://datasets.datalad.org/shub/powerPlant/vg-srf/1.11.0/2019-02-08-65a82f32-b005ac8e/Singularity
collection: powerPlant/vg-srf
---

# powerPlant/vg-srf:1.11.0

```bash
$ singularity pull shub://powerPlant/vg-srf:1.11.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: quay.io/vgteam/vg:v1.11.0-0-gea4aaded-t238-run

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 1.11.0

%runscript
  exec vg "$@"
```

## Collection

 - Name: [powerPlant/vg-srf](https://github.com/powerPlant/vg-srf)
 - License: None

