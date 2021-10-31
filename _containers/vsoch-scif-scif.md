---
id: 1235
name: "vsoch/scif"
branch: "master"
tag: "scif"
commit: "e044ce6c471878799e47ef9e6c2d517ec52d6ec3"
version: "762d0c58ddd409f33a357a43528ae302"
build_date: "2021-04-11T15:37:06.145Z"
size_mb: 3115
size: 1377902623
sif: "https://datasets.datalad.org/shub/vsoch/scif/scif/2021-04-11-e044ce6c-762d0c58/762d0c58ddd409f33a357a43528ae302.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/vsoch/scif/scif/2021-04-11-e044ce6c-762d0c58/
recipe: https://datasets.datalad.org/shub/vsoch/scif/scif/2021-04-11-e044ce6c-762d0c58/Singularity
collection: vsoch/scif
---

# vsoch/scif:scif

```bash
$ singularity pull shub://vsoch/scif:scif
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/anaconda3

# sudo singularity build hello-world-scif.simg Singularity.scif

%environment
    PATH=/opt/conda/bin:$PATH
    export PATH

%post
    cd /opt && git clone https://www.github.com/vsoch/scif.git
    cd scif && /opt/conda/bin/python setup.py install
    /opt/conda/bin/scif install docs/tutorials/hello-world.scif

%runscript
    exec scif "$@"
```

## Collection

 - Name: [vsoch/scif](https://github.com/vsoch/scif)
 - License: [GNU Affero General Public License v3.0](https://api.github.com/licenses/agpl-3.0)

