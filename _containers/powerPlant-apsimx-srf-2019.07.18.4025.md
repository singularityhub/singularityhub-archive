---
id: 12732
name: "powerPlant/apsimx-srf"
branch: "master"
tag: "2019.07.18.4025"
commit: "6e59e6919b1cfa1140d84f94f78cf8b530d02ae3"
version: "8e10548283de75c34a9b8dba304798286296b4b5201874c96ccd89d22157786f"
build_date: "2020-10-22T02:42:04.496Z"
size_mb: 325.2109375
size: 341008384
sif: "https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2019.07.18.4025/2020-10-22-6e59e691-8e105482/8e10548283de75c34a9b8dba304798286296b4b5201874c96ccd89d22157786f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/apsimx-srf/2019.07.18.4025/2020-10-22-6e59e691-8e105482/
recipe: https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2019.07.18.4025/2020-10-22-6e59e691-8e105482/Singularity
collection: powerPlant/apsimx-srf
---

# powerPlant/apsimx-srf:2019.07.18.4025

```bash
$ singularity pull shub://powerPlant/apsimx-srf:2019.07.18.4025
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2019.07.18.4025

%setup
  curl --silent -o ${SINGULARITY_ROOTFS}/tmp/ApsimSetup.deb http://apsimdev.apsim.info/ApsimXFiles/ApsimSetup4025.deb

%post
  ## Configure timezone
  apt-get update
  apt-get -y install tzdata
  ln -fs /usr/share/zoneinfo/Pacific/Auckland /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
  
  ## Install from deb file
  apt -y install /tmp/ApsimSetup.deb
  
  ## Create entrypoint
  cp -a /usr/local/bin/apsim /usr/local/bin/apsimmodels
  sed -i 's/ApsimNG/Models/' /usr/local/bin/apsimmodels

  ## Cleanup
  rm -rf /tmp/ApsimSetup.deb
  apt-get -y clean all
  apt-get -y autoremove --purge

%runscript
  exec /usr/local/bin/apsimmodels "$@"
```

## Collection

 - Name: [powerPlant/apsimx-srf](https://github.com/powerPlant/apsimx-srf)
 - License: None

