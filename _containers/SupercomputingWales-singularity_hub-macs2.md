---
id: 7269
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "macs2"
commit: "a8355d4aa8839dbf4f5c42d5baff2b71f813ef80"
version: "3954a4d2c17f43d4c24c62a66d72e2bb"
build_date: "2019-02-15T19:29:42.778Z"
size_mb: 1031
size: 359120927
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/macs2/2019-02-15-a8355d4a-3954a4d2/3954a4d2c17f43d4c24c62a66d72e2bb.simg"
url: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/macs2/2019-02-15-a8355d4a-3954a4d2/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/macs2/2019-02-15-a8355d4a-3954a4d2/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:macs2

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:macs2
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:fooliu/macs2

%labels
MAINTAINER Thomas Green

%environment

%runscript
exec /bin/bash /bin/echo "Not supported"

%post  

mkdir /apps
mkdir /scratch
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

