---
id: 1342
name: "vsoch/hello-world.scif"
branch: "master"
tag: "latest"
commit: "2a95715448d11e6790dc5974cdb86e18b4a0308d"
version: "3bb6590d303dc084c5fea487b56c6b2a"
build_date: "2021-02-25T02:25:05.685Z"
size_mb: 759
size: 326381599
sif: "https://datasets.datalad.org/shub/vsoch/hello-world.scif/latest/2021-02-25-2a957154-3bb6590d/3bb6590d303dc084c5fea487b56c6b2a.simg"
url: https://datasets.datalad.org/shub/vsoch/hello-world.scif/latest/2021-02-25-2a957154-3bb6590d/
recipe: https://datasets.datalad.org/shub/vsoch/hello-world.scif/latest/2021-02-25-2a957154-3bb6590d/Singularity
collection: vsoch/hello-world.scif
---

# vsoch/hello-world.scif:latest

```bash
$ singularity pull shub://vsoch/hello-world.scif:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

# sudo singularity build hello-world Singularity

%runscript
    exec /opt/conda/bin/scif "$@"

%labels
    MAINTAINER vsochat@stanford.edu

%files
    hello-world.scif

%post
    apt-get update && apt-get install -y git build-essential
    /opt/conda/bin/pip install dateutils

    # Install SCIF
    cd /opt && git clone https://www.github.com/vsoch/scif.git
    cd scif
    /opt/conda/bin/pip install setuptools
    /opt/conda/bin/pip install -e .
    /opt/conda/bin/scif install /hello-world.scif
```

## Collection

 - Name: [vsoch/hello-world.scif](https://github.com/vsoch/hello-world.scif)
 - License: [GNU Affero General Public License v3.0](https://api.github.com/licenses/agpl-3.0)

