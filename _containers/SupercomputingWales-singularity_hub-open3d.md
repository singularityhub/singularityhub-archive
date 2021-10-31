---
id: 14579
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "open3d"
commit: "c81e03ed048193610040606e36264047e88ea2ed"
version: "d86b8ce77238045de43400c0e572f1346b8fdb7d92c08d315c75ebc4407fc847"
build_date: "2020-10-11T17:21:16.017Z"
size_mb: 683.578125
size: 716783616
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/open3d/2020-10-11-c81e03ed-d86b8ce7/d86b8ce77238045de43400c0e572f1346b8fdb7d92c08d315c75ebc4407fc847.sif"
url: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/open3d/2020-10-11-c81e03ed-d86b8ce7/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/open3d/2020-10-11-c81e03ed-d86b8ce7/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:open3d

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:open3d
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:continuumio/miniconda3:4.8.2

%labels
MAINTAINER Thomas Green

%environment

%runscript
exec /bin/bash /bin/echo "Not supported"

%post
# Create some common mountpoints for systems without overlayfs
mkdir /scratch
mkdir /apps

. /etc/profile
cd /tmp
conda update -n base -c defaults conda
conda install -c open3d-admin open3d
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

