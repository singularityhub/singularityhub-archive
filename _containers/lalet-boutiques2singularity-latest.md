---
id: 499
name: "lalet/boutiques2singularity"
branch: "master"
tag: "latest"
commit: "cc6ac487809186225dc0a4a4e65318104a7437ef"
version: "6d97be342bbab8b552ba6c036dc4726d"
build_date: "2017-10-25T06:15:17.795Z"
size_mb: 480
size: 139542559
sif: "https://datasets.datalad.org/shub/lalet/boutiques2singularity/latest/2017-10-25-cc6ac487-6d97be34/6d97be342bbab8b552ba6c036dc4726d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/lalet/boutiques2singularity/latest/2017-10-25-cc6ac487-6d97be34/
recipe: https://datasets.datalad.org/shub/lalet/boutiques2singularity/latest/2017-10-25-cc6ac487-6d97be34/Singularity
collection: lalet/boutiques2singularity
---

# lalet/boutiques2singularity:latest

```bash
$ singularity pull shub://lalet/boutiques2singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: boutiques/boutiques

%post
  pip install coveralls pytest pytest-runner boutiques
  pip install simplejson jsonschema gitpython PyGithub

%runscript
  bosh -h
```

## Collection

 - Name: [lalet/boutiques2singularity](https://github.com/lalet/boutiques2singularity)
 - License: None

