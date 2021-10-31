---
id: 3400
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "underworld2"
commit: "fb4b14f33436a9c5525c185d6b32459a0489160d"
version: "14cf62245e1180e2cbb8c88408bceb6e"
build_date: "2018-07-03T14:55:06.994Z"
size_mb: 1547
size: 513802271
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/underworld2/2018-07-03-fb4b14f3-14cf6224/14cf62245e1180e2cbb8c88408bceb6e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/SupercomputingWales/singularity_hub/underworld2/2018-07-03-fb4b14f3-14cf6224/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/underworld2/2018-07-03-fb4b14f3-14cf6224/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:underworld2

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:underworld2
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:underworldcode/underworld2:latest

%labels
MAINTAINER Thomas Green

%environment

%runscript
exec /bin/bash /bin/echo "Not supported"

%post
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

