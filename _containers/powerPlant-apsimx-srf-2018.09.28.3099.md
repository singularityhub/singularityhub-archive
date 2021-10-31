---
id: 6791
name: "powerPlant/apsimx-srf"
branch: "master"
tag: "2018.09.28.3099"
commit: "6e59e6919b1cfa1140d84f94f78cf8b530d02ae3"
version: "8329f89ea9a9dce7b3be975eba3386aafee4dd126091384f7ba9907e033936df"
build_date: "2020-10-22T03:08:30.318Z"
size_mb: 323.51171875
size: 339226624
sif: "https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2018.09.28.3099/2020-10-22-6e59e691-8329f89e/8329f89ea9a9dce7b3be975eba3386aafee4dd126091384f7ba9907e033936df.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/apsimx-srf/2018.09.28.3099/2020-10-22-6e59e691-8329f89e/
recipe: https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2018.09.28.3099/2020-10-22-6e59e691-8329f89e/Singularity
collection: powerPlant/apsimx-srf
---

# powerPlant/apsimx-srf:2018.09.28.3099

```bash
$ singularity pull shub://powerPlant/apsimx-srf:2018.09.28.3099
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2018.09.28.3099

%setup
  curl --silent -o ${SINGULARITY_ROOTFS}/ApsimSetup.deb http://apsimdev.apsim.info/ApsimXFiles/ApsimSetup3099.deb

%post
  ## Configure timezone
  apt-get update
  apt-get -y install tzdata
  ln -fs /usr/share/zoneinfo/Pacific/Auckland /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
  
  ## Install from deb file
  apt -y install /ApsimSetup.deb
  
  ## Create entrypoint
  cp -a /usr/local/bin/apsim /usr/local/bin/apsimmodels
  sed -i 's/ApsimNG/Models/' /usr/local/bin/apsimmodels

  ## Cleanup
  rm -rf /ApsimSetup.deb
  apt-get -y clean all
  apt-get -y autoremove --purge

%runscript
  exec /usr/local/bin/apsimmodels "$@"
```

## Collection

 - Name: [powerPlant/apsimx-srf](https://github.com/powerPlant/apsimx-srf)
 - License: None

