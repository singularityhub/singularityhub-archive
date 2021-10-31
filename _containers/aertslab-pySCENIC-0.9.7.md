---
id: 7945
name: "aertslab/pySCENIC"
branch: "master"
tag: "0.9.7"
commit: "b492340343950f2b978e5222d814300d527053eb"
version: "1486525b46972582cc9d16525c0dd7c2"
build_date: "2020-12-08T01:16:39.687Z"
size_mb: 798
size: 227680287
sif: "https://datasets.datalad.org/shub/aertslab/pySCENIC/0.9.7/2020-12-08-b4923403-1486525b/1486525b46972582cc9d16525c0dd7c2.simg"
url: https://datasets.datalad.org/shub/aertslab/pySCENIC/0.9.7/2020-12-08-b4923403-1486525b/
recipe: https://datasets.datalad.org/shub/aertslab/pySCENIC/0.9.7/2020-12-08-b4923403-1486525b/Singularity
collection: aertslab/pySCENIC
---

# aertslab/pySCENIC:0.9.7

```bash
$ singularity pull shub://aertslab/pySCENIC:0.9.7
```

## Singularity Recipe

```singularity
BootStrap: docker
From: python:3.6.8-slim

%post
    BUILDPKGS="build-essential apt-utils" && \
    apt-get update && \
    apt-get install -y $BUILDPKGS && \
    apt-get install -y procps && \
    rm -rf /var/lib/apt/lists/*
    pip install --no-cache-dir --upgrade pyscenic==0.9.7 ipykernel dask==1.0.0 pandas==0.23.4
    apt-get remove --purge -y $BUILDPKGS
```

## Collection

 - Name: [aertslab/pySCENIC](https://github.com/aertslab/pySCENIC)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

