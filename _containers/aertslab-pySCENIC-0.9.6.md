---
id: 7824
name: "aertslab/pySCENIC"
branch: "master"
tag: "0.9.6"
commit: "486d602f2d706b415d08efb3aa295b6404830b9d"
version: "fb456e8cb6a9c151790d109566fedfa7"
build_date: "2019-08-08T16:42:00.883Z"
size_mb: 772
size: 221446175
sif: "https://datasets.datalad.org/shub/aertslab/pySCENIC/0.9.6/2019-08-08-486d602f-fb456e8c/fb456e8cb6a9c151790d109566fedfa7.simg"
url: https://datasets.datalad.org/shub/aertslab/pySCENIC/0.9.6/2019-08-08-486d602f-fb456e8c/
recipe: https://datasets.datalad.org/shub/aertslab/pySCENIC/0.9.6/2019-08-08-486d602f-fb456e8c/Singularity
collection: aertslab/pySCENIC
---

# aertslab/pySCENIC:0.9.6

```bash
$ singularity pull shub://aertslab/pySCENIC:0.9.6
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
    pip install --no-cache-dir --upgrade pyscenic==0.9.6 dask==1.0.0 pandas==0.23.4
    apt-get remove --purge -y $BUILDPKGS
```

## Collection

 - Name: [aertslab/pySCENIC](https://github.com/aertslab/pySCENIC)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

