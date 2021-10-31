---
id: 7159
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "gubbins"
commit: "6e193864667ca9ee0605eed0f72bb410bc6c8c78"
version: "6e85cf6d03d042171f481d5528d5dcf5"
build_date: "2019-02-12T14:29:39.921Z"
size_mb: 590
size: 265302047
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/gubbins/2019-02-12-6e193864-6e85cf6d/6e85cf6d03d042171f481d5528d5dcf5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/SupercomputingWales/singularity_hub/gubbins/2019-02-12-6e193864-6e85cf6d/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/gubbins/2019-02-12-6e193864-6e85cf6d/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:gubbins

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:gubbins
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:sangerpathogens/gubbins:latest

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

