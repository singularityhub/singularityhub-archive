---
id: 1253
name: "vsoch/scif"
branch: "master"
tag: "latest"
commit: "7784f0db925e4656fde83da29c8660195c84594f"
version: "c02b6bf17d5602717a4e5e7b6c3e42b7"
build_date: "2020-06-19T16:16:26.171Z"
size_mb: 758
size: 325922847
sif: "https://datasets.datalad.org/shub/vsoch/scif/latest/2020-06-19-7784f0db-c02b6bf1/c02b6bf17d5602717a4e5e7b6c3e42b7.simg"
url: https://datasets.datalad.org/shub/vsoch/scif/latest/2020-06-19-7784f0db-c02b6bf1/
recipe: https://datasets.datalad.org/shub/vsoch/scif/latest/2020-06-19-7784f0db-c02b6bf1/Singularity
collection: vsoch/scif
---

# vsoch/scif:latest

```bash
$ singularity pull shub://vsoch/scif:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

# sudo singularity build scif.simg Singularity

%runscript
    exec /opt/conda/bin/scif "$@"

%labels
    MAINTAINER vsochat@stanford.edu

%post
    apt-get update && apt-get install -y git build-essential
    /opt/conda/bin/pip install dateutils

    # Install SCIF
    cd /opt && git clone https://www.github.com/vsoch/scif.git
    cd scif
    /opt/conda/bin/pip install setuptools
    /opt/conda/bin/pip install -e .
```

## Collection

 - Name: [vsoch/scif](https://github.com/vsoch/scif)
 - License: [GNU Affero General Public License v3.0](https://api.github.com/licenses/agpl-3.0)

