---
id: 6772
name: "powerPlant/opendronemap-srf"
branch: "master"
tag: "0.4.0"
commit: "8e54aa0759c00d67c6441475c46e6e1ccf1aa8d8"
version: "b13bc707c40b4a7ccaa7f1622a3abe53"
build_date: "2019-02-05T05:54:32.398Z"
size_mb: 3023
size: 892174367
sif: "https://datasets.datalad.org/shub/powerPlant/opendronemap-srf/0.4.0/2019-02-05-8e54aa07-b13bc707/b13bc707c40b4a7ccaa7f1622a3abe53.simg"
url: https://datasets.datalad.org/shub/powerPlant/opendronemap-srf/0.4.0/2019-02-05-8e54aa07-b13bc707/
recipe: https://datasets.datalad.org/shub/powerPlant/opendronemap-srf/0.4.0/2019-02-05-8e54aa07-b13bc707/Singularity
collection: powerPlant/opendronemap-srf
---

# powerPlant/opendronemap-srf:0.4.0

```bash
$ singularity pull shub://powerPlant/opendronemap-srf:0.4.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: opendronemap/opendronemap:0.4.0

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 0.4.0

%runscript
  exec run.py "$@"
```

## Collection

 - Name: [powerPlant/opendronemap-srf](https://github.com/powerPlant/opendronemap-srf)
 - License: None

