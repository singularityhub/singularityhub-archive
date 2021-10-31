---
id: 6780
name: "powerPlant/qiime2-srf"
branch: "master"
tag: "2019.1"
commit: "196642e99dd2e07c6acb139043bc3e8ea7c7c526"
version: "7a0c843c20394732cdd445a44f2d5fbd"
build_date: "2020-08-19T05:04:37.572Z"
size_mb: 6457
size: 2757165087
sif: "https://datasets.datalad.org/shub/powerPlant/qiime2-srf/2019.1/2020-08-19-196642e9-7a0c843c/7a0c843c20394732cdd445a44f2d5fbd.simg"
url: https://datasets.datalad.org/shub/powerPlant/qiime2-srf/2019.1/2020-08-19-196642e9-7a0c843c/
recipe: https://datasets.datalad.org/shub/powerPlant/qiime2-srf/2019.1/2020-08-19-196642e9-7a0c843c/Singularity
collection: powerPlant/qiime2-srf
---

# powerPlant/qiime2-srf:2019.1

```bash
$ singularity pull shub://powerPlant/qiime2-srf:2019.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: qiime2/core:2019.1

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 2019.1

%post
  chmod 775 /home/qiime2/q2cli/cache/completion.sh

%runscript
  exec qiime "$@"
```

## Collection

 - Name: [powerPlant/qiime2-srf](https://github.com/powerPlant/qiime2-srf)
 - License: None

