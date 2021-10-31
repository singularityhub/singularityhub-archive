---
id: 15117
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "hello-world"
commit: "75c8d2899bf809749291ffa91e6451ef2f49d833"
version: "b6ea20409f6ab95321b550d52fb560afe1d09189b2a765413d4d8bb9ec4a8daf"
build_date: "2021-03-02T10:14:08.610Z"
size_mb: 65.63671875
size: 68825088
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/hello-world/2021-03-02-75c8d289-b6ea2040/b6ea20409f6ab95321b550d52fb560afe1d09189b2a765413d4d8bb9ec4a8daf.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/SupercomputingWales/singularity_hub/hello-world/2021-03-02-75c8d289-b6ea2040/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/hello-world/2021-03-02-75c8d289-b6ea2040/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:hello-world

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:hello-world
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:14.04

%labels
MAINTAINER vanessasaur
WHATAMI dinosaur

%environment
DINOSAUR=vanessasaurus
export DINOSAUR

%files
rawr.sh /rawr.sh

%post
chmod u+x /rawr.sh

%runscript
exec /bin/bash /rawr.sh
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

