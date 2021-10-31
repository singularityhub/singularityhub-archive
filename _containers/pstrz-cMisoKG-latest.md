---
id: 2535
name: "pstrz/cMisoKG"
branch: "master"
tag: "latest"
commit: "1bb5368e39e3f289f8a34192bc39329516fa0d64"
version: "9181ba44ce7a20ceba582b05b2260523"
build_date: "2018-04-14T23:57:02.002Z"
size_mb: 1410
size: 467402783
sif: "https://datasets.datalad.org/shub/pstrz/cMisoKG/latest/2018-04-14-1bb5368e-9181ba44/9181ba44ce7a20ceba582b05b2260523.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pstrz/cMisoKG/latest/2018-04-14-1bb5368e-9181ba44/
recipe: https://datasets.datalad.org/shub/pstrz/cMisoKG/latest/2018-04-14-1bb5368e-9181ba44/Singularity
collection: pstrz/cMisoKG
---

# pstrz/cMisoKG:latest

```bash
$ singularity pull shub://pstrz/cMisoKG:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow

%post
    apt-get -y install git-core
    git clone https://github.com/GPflow/GPflow.git
    cd GPflow
    pip install .
```

## Collection

 - Name: [pstrz/cMisoKG](https://github.com/pstrz/cMisoKG)
 - License: None

