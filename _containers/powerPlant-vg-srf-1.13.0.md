---
id: 7028
name: "powerPlant/vg-srf"
branch: "master"
tag: "1.13.0"
commit: "5cd9cc84b348edf811fb48b749ddcf43518f6102"
version: "49918c3930980bf226a3015683272fc7"
build_date: "2019-02-08T05:38:46.710Z"
size_mb: 618
size: 214945823
sif: "https://datasets.datalad.org/shub/powerPlant/vg-srf/1.13.0/2019-02-08-5cd9cc84-49918c39/49918c3930980bf226a3015683272fc7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/vg-srf/1.13.0/2019-02-08-5cd9cc84-49918c39/
recipe: https://datasets.datalad.org/shub/powerPlant/vg-srf/1.13.0/2019-02-08-5cd9cc84-49918c39/Singularity
collection: powerPlant/vg-srf
---

# powerPlant/vg-srf:1.13.0

```bash
$ singularity pull shub://powerPlant/vg-srf:1.13.0
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

