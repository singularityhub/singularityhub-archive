---
id: 7011
name: "powerPlant/vg-srf"
branch: "master"
tag: "latest"
commit: "65a82f32f2607dce15bb5a435df8d620919bf893"
version: "164027d26c326504282331971d2aa80b"
build_date: "2019-02-08T05:38:46.748Z"
size_mb: 618
size: 214945823
sif: "https://datasets.datalad.org/shub/powerPlant/vg-srf/latest/2019-02-08-65a82f32-164027d2/164027d26c326504282331971d2aa80b.simg"
url: https://datasets.datalad.org/shub/powerPlant/vg-srf/latest/2019-02-08-65a82f32-164027d2/
recipe: https://datasets.datalad.org/shub/powerPlant/vg-srf/latest/2019-02-08-65a82f32-164027d2/Singularity
collection: powerPlant/vg-srf
---

# powerPlant/vg-srf:latest

```bash
$ singularity pull shub://powerPlant/vg-srf:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: quay.io/vgteam/vg:v1.13.0

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 1.13.0

%runscript
  exec vg "$@"
```

## Collection

 - Name: [powerPlant/vg-srf](https://github.com/powerPlant/vg-srf)
 - License: None

