---
id: 7015
name: "powerPlant/vg-srf"
branch: "master"
tag: "1.12.1"
commit: "65a82f32f2607dce15bb5a435df8d620919bf893"
version: "be9c6cbfb9087105fb5e1512a15327ee"
build_date: "2019-02-08T05:38:46.731Z"
size_mb: 613
size: 213258271
sif: "https://datasets.datalad.org/shub/powerPlant/vg-srf/1.12.1/2019-02-08-65a82f32-be9c6cbf/be9c6cbfb9087105fb5e1512a15327ee.simg"
url: https://datasets.datalad.org/shub/powerPlant/vg-srf/1.12.1/2019-02-08-65a82f32-be9c6cbf/
recipe: https://datasets.datalad.org/shub/powerPlant/vg-srf/1.12.1/2019-02-08-65a82f32-be9c6cbf/Singularity
collection: powerPlant/vg-srf
---

# powerPlant/vg-srf:1.12.1

```bash
$ singularity pull shub://powerPlant/vg-srf:1.12.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: quay.io/vgteam/vg:v1.12.1

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 1.12.1

%runscript
  exec vg "$@"
```

## Collection

 - Name: [powerPlant/vg-srf](https://github.com/powerPlant/vg-srf)
 - License: None

