---
id: 7012
name: "powerPlant/vg-srf"
branch: "master"
tag: "1.10.0"
commit: "65a82f32f2607dce15bb5a435df8d620919bf893"
version: "c9aa61ca673cf8941357f6b2d60a54b6"
build_date: "2019-02-08T05:38:46.742Z"
size_mb: 617
size: 220893215
sif: "https://datasets.datalad.org/shub/powerPlant/vg-srf/1.10.0/2019-02-08-65a82f32-c9aa61ca/c9aa61ca673cf8941357f6b2d60a54b6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/vg-srf/1.10.0/2019-02-08-65a82f32-c9aa61ca/
recipe: https://datasets.datalad.org/shub/powerPlant/vg-srf/1.10.0/2019-02-08-65a82f32-c9aa61ca/Singularity
collection: powerPlant/vg-srf
---

# powerPlant/vg-srf:1.10.0

```bash
$ singularity pull shub://powerPlant/vg-srf:1.10.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: quay.io/vgteam/vg:v1.10.0-0-ga4811915-t226-run

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 1.10.0

%runscript
  exec vg "$@"
```

## Collection

 - Name: [powerPlant/vg-srf](https://github.com/powerPlant/vg-srf)
 - License: None

