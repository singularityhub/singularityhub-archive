---
id: 6902
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "opencv"
commit: "5e80dcc43ec97e7a0cca77ed571f0255c8d4567c"
version: "3bb889d5851b02fb7c31a4809b579707"
build_date: "2019-02-09T23:03:26.573Z"
size_mb: 3378
size: 1031303199
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/opencv/2019-02-09-5e80dcc4-3bb889d5/3bb889d5851b02fb7c31a4809b579707.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/SupercomputingWales/singularity_hub/opencv/2019-02-09-5e80dcc4-3bb889d5/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/opencv/2019-02-09-5e80dcc4-3bb889d5/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:opencv

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:opencv
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:spmallick/opencv-docker:opencv

%labels
MAINTAINER Thomas Green

%environment

%runscript
exec /bin/bash /bin/echo "Not supported"

%post  
mkdir /scratch
mkdir /apps
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

