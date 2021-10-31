---
id: 6773
name: "powerPlant/opendronemap-srf"
branch: "master"
tag: "0.4.1"
commit: "8e54aa0759c00d67c6441475c46e6e1ccf1aa8d8"
version: "659de9095516d683eb695fcada8011c6"
build_date: "2019-02-05T05:54:32.392Z"
size_mb: 2967
size: 871137311
sif: "https://datasets.datalad.org/shub/powerPlant/opendronemap-srf/0.4.1/2019-02-05-8e54aa07-659de909/659de9095516d683eb695fcada8011c6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/opendronemap-srf/0.4.1/2019-02-05-8e54aa07-659de909/
recipe: https://datasets.datalad.org/shub/powerPlant/opendronemap-srf/0.4.1/2019-02-05-8e54aa07-659de909/Singularity
collection: powerPlant/opendronemap-srf
---

# powerPlant/opendronemap-srf:0.4.1

```bash
$ singularity pull shub://powerPlant/opendronemap-srf:0.4.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: opendronemap/odm@sha256:07a17c8668397272cd85f3a9fea8756cb9b51aa0850d27e525944ec37042cc74

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 0.4.1

%runscript
  exec run.py "$@"
```

## Collection

 - Name: [powerPlant/opendronemap-srf](https://github.com/powerPlant/opendronemap-srf)
 - License: None

