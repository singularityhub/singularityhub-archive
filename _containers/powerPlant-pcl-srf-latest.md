---
id: 7123
name: "powerPlant/pcl-srf"
branch: "master"
tag: "latest"
commit: "c6e8c235f4943fe212ce3c8ce4968ae5b298dd86"
version: "1deaff10a91effb9a89321316e22b47e"
build_date: "2019-10-02T11:32:23.855Z"
size_mb: 1187
size: 386277407
sif: "https://datasets.datalad.org/shub/powerPlant/pcl-srf/latest/2019-10-02-c6e8c235-1deaff10/1deaff10a91effb9a89321316e22b47e.simg"
url: https://datasets.datalad.org/shub/powerPlant/pcl-srf/latest/2019-10-02-c6e8c235-1deaff10/
recipe: https://datasets.datalad.org/shub/powerPlant/pcl-srf/latest/2019-10-02-c6e8c235-1deaff10/Singularity
collection: powerPlant/pcl-srf
---

# powerPlant/pcl-srf:latest

```bash
$ singularity pull shub://powerPlant/pcl-srf:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:disco

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 1.9.1

%post
  apt-get update
  apt-get -y install pcl-tools
  
  ## Cleanup
  apt-get -y clean all

%runscript
if [ $# -eq 0 ]; then
  /bin/echo -e "This Singularity image cannot provide a single entrypoint. Please use \"$SINGULARITY_NAME <cmd>\" or \"singularity exec $SINGULARITY_NAME <cmd>\", where <cmd> is one of the following:\n"
  cd /usr/bin
  exec ls pcl_*
else
  exec "$@"
fi
```

## Collection

 - Name: [powerPlant/pcl-srf](https://github.com/powerPlant/pcl-srf)
 - License: None

