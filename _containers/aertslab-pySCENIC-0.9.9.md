---
id: 9051
name: "aertslab/pySCENIC"
branch: "master"
tag: "0.9.9"
commit: "caded79a17aee3849ec714fe7be2636dcb4fa664"
version: "2b8f66dea8b4897a9349cc42c1c2f501"
build_date: "2021-03-24T07:04:33.067Z"
size_mb: 926
size: 265981983
sif: "https://datasets.datalad.org/shub/aertslab/pySCENIC/0.9.9/2021-03-24-caded79a-2b8f66de/2b8f66dea8b4897a9349cc42c1c2f501.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/aertslab/pySCENIC/0.9.9/2021-03-24-caded79a-2b8f66de/
recipe: https://datasets.datalad.org/shub/aertslab/pySCENIC/0.9.9/2021-03-24-caded79a-2b8f66de/Singularity
collection: aertslab/pySCENIC
---

# aertslab/pySCENIC:0.9.9

```bash
$ singularity pull shub://aertslab/pySCENIC:0.9.9
```

## Singularity Recipe

```singularity
BootStrap: docker
From: python:3.6.8-slim

%files
    ./requirements.txt /tmp/

%post
    BUILDPKGS="build-essential apt-utils" && \
    apt-get update && \
    apt-get install -y $BUILDPKGS && \
    apt-get install -y procps

    pip install --no-cache-dir -r /tmp/requirements.txt
    pip install --no-cache-dir --upgrade pyscenic==0.9.9
    pip install --no-cache-dir --upgrade ipykernel

    apt-get remove --purge -y $BUILDPKGS && \
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [aertslab/pySCENIC](https://github.com/aertslab/pySCENIC)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

