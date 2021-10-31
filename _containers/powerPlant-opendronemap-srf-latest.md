---
id: 6771
name: "powerPlant/opendronemap-srf"
branch: "master"
tag: "latest"
commit: "c09855ceb743b3b7c11f05a525ada0679fed5816"
version: "4f3cad15a325619c1443b2c90cc625a5"
build_date: "2019-02-01T14:00:56.135Z"
size_mb: 2967
size: 871137311
sif: "https://datasets.datalad.org/shub/powerPlant/opendronemap-srf/latest/2019-02-01-c09855ce-4f3cad15/4f3cad15a325619c1443b2c90cc625a5.simg"
url: https://datasets.datalad.org/shub/powerPlant/opendronemap-srf/latest/2019-02-01-c09855ce-4f3cad15/
recipe: https://datasets.datalad.org/shub/powerPlant/opendronemap-srf/latest/2019-02-01-c09855ce-4f3cad15/Singularity
collection: powerPlant/opendronemap-srf
---

# powerPlant/opendronemap-srf:latest

```bash
$ singularity pull shub://powerPlant/opendronemap-srf:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: opendronemap/odm@sha256:07a17c8668397272cd85f3a9fea8756cb9b51aa0850d27e525944ec37042cc74

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 0.4.1

%runscript
  run.py "$@"
```

## Collection

 - Name: [powerPlant/opendronemap-srf](https://github.com/powerPlant/opendronemap-srf)
 - License: None

