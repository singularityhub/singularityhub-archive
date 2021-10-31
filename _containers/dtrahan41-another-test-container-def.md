---
id: 8056
name: "dtrahan41/another-test-container"
branch: "master"
tag: "def"
commit: "ec95c5feef2af3382a1234adb956eb2eb30ac1bd"
version: "3ae21527c2d80b028ca058bf94b5b6ba"
build_date: "2019-04-01T19:11:54.020Z"
size_mb: 76
size: 27959327
sif: "https://datasets.datalad.org/shub/dtrahan41/another-test-container/def/2019-04-01-ec95c5fe-3ae21527/3ae21527c2d80b028ca058bf94b5b6ba.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dtrahan41/another-test-container/def/2019-04-01-ec95c5fe-3ae21527/
recipe: https://datasets.datalad.org/shub/dtrahan41/another-test-container/def/2019-04-01-ec95c5fe-3ae21527/Singularity
collection: dtrahan41/another-test-container
---

# dtrahan41/another-test-container:def

```bash
$ singularity pull shub://dtrahan41/another-test-container:def
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu

%enviornment
SAMPLEVAR=21
export SAMPLEVAR
```

## Collection

 - Name: [dtrahan41/another-test-container](https://github.com/dtrahan41/another-test-container)
 - License: None

