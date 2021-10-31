---
id: 1161
name: "joshbcohen/VdjcallerSingularity"
branch: "master"
tag: "latest"
commit: "c56386fef2554232d239ecec9c95e2e855cba21f"
version: "1712e1602af8e759e71f2c28ef24806a"
build_date: "2017-12-20T19:57:56.266Z"
size_mb: 3640
size: 1761349663
sif: "https://datasets.datalad.org/shub/joshbcohen/VdjcallerSingularity/latest/2017-12-20-c56386fe-1712e160/1712e1602af8e759e71f2c28ef24806a.simg"
url: https://datasets.datalad.org/shub/joshbcohen/VdjcallerSingularity/latest/2017-12-20-c56386fe-1712e160/
recipe: https://datasets.datalad.org/shub/joshbcohen/VdjcallerSingularity/latest/2017-12-20-c56386fe-1712e160/Singularity
collection: joshbcohen/VdjcallerSingularity
---

# joshbcohen/VdjcallerSingularity:latest

```bash
$ singularity pull shub://joshbcohen/VdjcallerSingularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: joshbcohen/vdj_pipeline:latest
%post
   mkdir /vdj_pipeline
   cp ${HOME}/.bashrc /vdj_pipeline
   mkdir /scratchLocal
   mkdir /scratchLocal/joc2080
   mkdir /cluster001
   mkdir /athena
   mkdir /boot
   mkdir /pbtech_mounts
   mkdir /pbtech_mounts/homes022
   mkdir /pbtech_mounts/homes031
   mkdir /pbtech_mounts/softlib001
```

## Collection

 - Name: [joshbcohen/VdjcallerSingularity](https://github.com/joshbcohen/VdjcallerSingularity)
 - License: None

