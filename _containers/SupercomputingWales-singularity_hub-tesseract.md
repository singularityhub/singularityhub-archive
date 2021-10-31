---
id: 8392
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "tesseract"
commit: "b4c4b76a6866b1212d6f3266866c26cce4c5d3a4"
version: "4b92cb50036aaf01242faab49f45705e"
build_date: "2019-04-13T15:18:57.603Z"
size_mb: 905
size: 442834975
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/tesseract/2019-04-13-b4c4b76a-4b92cb50/4b92cb50036aaf01242faab49f45705e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/SupercomputingWales/singularity_hub/tesseract/2019-04-13-b4c4b76a-4b92cb50/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/tesseract/2019-04-13-b4c4b76a-4b92cb50/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:tesseract

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:tesseract
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:tesseractshadow/tesseract4re

%labels
MAINTAINER Thomas Green

%environment

%runscript
exec /bin/bash /bin/echo "Not supported"

%post
# Create some common mountpoints for systems without overlayfs
mkdir /scratch
mkdir /apps
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

