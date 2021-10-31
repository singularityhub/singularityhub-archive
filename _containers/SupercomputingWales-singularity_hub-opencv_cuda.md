---
id: 7066
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "opencv_cuda"
commit: "7eee244f2730a08ef27b877c53be8d93b0459697"
version: "2e151134765e7e01c38bec301b754a40"
build_date: "2019-02-09T23:03:26.567Z"
size_mb: 4631
size: 1995182111
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/opencv_cuda/2019-02-09-7eee244f-2e151134/2e151134765e7e01c38bec301b754a40.simg"
url: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/opencv_cuda/2019-02-09-7eee244f-2e151134/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/opencv_cuda/2019-02-09-7eee244f-2e151134/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:opencv_cuda

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:opencv_cuda
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:awokeknowing/cuda-opencv

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

