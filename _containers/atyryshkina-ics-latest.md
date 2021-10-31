---
id: 11453
name: "atyryshkina/ics"
branch: "master"
tag: "latest"
commit: "2a43450217ca8a889c83c6b3e390684963d9fa31"
version: "b7fab0b1cca44fed41617be5426181a5"
build_date: "2019-11-15T19:45:29.238Z"
size_mb: 496.0
size: 183865375
sif: "https://datasets.datalad.org/shub/atyryshkina/ics/latest/2019-11-15-2a434502-b7fab0b1/b7fab0b1cca44fed41617be5426181a5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/atyryshkina/ics/latest/2019-11-15-2a434502-b7fab0b1/
recipe: https://datasets.datalad.org/shub/atyryshkina/ics/latest/2019-11-15-2a434502-b7fab0b1/Singularity
collection: atyryshkina/ics
---

# atyryshkina/ics:latest

```bash
$ singularity pull shub://atyryshkina/ics:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

%post
yum -y install gcc-* python-devel wget
yum -y update
```

## Collection

 - Name: [atyryshkina/ics](https://github.com/atyryshkina/ics)
 - License: None

