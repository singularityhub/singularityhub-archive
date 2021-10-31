---
id: 7124
name: "powerPlant/pcl-srf"
branch: "master"
tag: "1.8.1"
commit: "4fb5a5464874f126de7d76557046ec07cee7a6ec"
version: "80fed0a1a83ac31a9af2999185250d24"
build_date: "2019-02-14T08:45:04.962Z"
size_mb: 1027
size: 342343711
sif: "https://datasets.datalad.org/shub/powerPlant/pcl-srf/1.8.1/2019-02-14-4fb5a546-80fed0a1/80fed0a1a83ac31a9af2999185250d24.simg"
url: https://datasets.datalad.org/shub/powerPlant/pcl-srf/1.8.1/2019-02-14-4fb5a546-80fed0a1/
recipe: https://datasets.datalad.org/shub/powerPlant/pcl-srf/1.8.1/2019-02-14-4fb5a546-80fed0a1/Singularity
collection: powerPlant/pcl-srf
---

# powerPlant/pcl-srf:1.8.1

```bash
$ singularity pull shub://powerPlant/pcl-srf:1.8.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 1.8.1

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

