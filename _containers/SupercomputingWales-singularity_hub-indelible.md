---
id: 15049
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "indelible"
commit: "b6dd836385756dd6bb4d3d742754c70956934cbc"
version: "a2ef3e211ebcd14383a69e480fc4588608a0cee4e86bfa4b29995347a24a0f12"
build_date: "2021-01-11T01:43:52.122Z"
size_mb: 2718.30859375
size: 2850353152
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/indelible/2021-01-11-b6dd8363-a2ef3e21/a2ef3e211ebcd14383a69e480fc4588608a0cee4e86bfa4b29995347a24a0f12.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/SupercomputingWales/singularity_hub/indelible/2021-01-11-b6dd8363-a2ef3e21/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/indelible/2021-01-11-b6dd8363-a2ef3e21/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:indelible

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:indelible
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:mercury/indelible:hg19only_d62cd07

%labels
MAINTAINER Thomas Green

%environment

%runscript
exec /bin/bash /bin/echo "Not supported"

%post
# Create some common mountpoints for systems without overlayfs
mkdir /scratch 
mkdir /apps

# Make files readable by all users - some are only root.
cd /usr/src/app/Indelible
chmod go+rX data/*
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

