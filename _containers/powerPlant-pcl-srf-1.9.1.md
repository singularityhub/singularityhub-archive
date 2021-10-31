---
id: 7215
name: "powerPlant/pcl-srf"
branch: "master"
tag: "1.9.1"
commit: "c6e8c235f4943fe212ce3c8ce4968ae5b298dd86"
version: "0405e4c178980afbd2892018d92a9b12"
build_date: "2019-02-14T08:45:04.955Z"
size_mb: 1187
size: 386277407
sif: "https://datasets.datalad.org/shub/powerPlant/pcl-srf/1.9.1/2019-02-14-c6e8c235-0405e4c1/0405e4c178980afbd2892018d92a9b12.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/pcl-srf/1.9.1/2019-02-14-c6e8c235-0405e4c1/
recipe: https://datasets.datalad.org/shub/powerPlant/pcl-srf/1.9.1/2019-02-14-c6e8c235-0405e4c1/Singularity
collection: powerPlant/pcl-srf
---

# powerPlant/pcl-srf:1.9.1

```bash
$ singularity pull shub://powerPlant/pcl-srf:1.9.1
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

