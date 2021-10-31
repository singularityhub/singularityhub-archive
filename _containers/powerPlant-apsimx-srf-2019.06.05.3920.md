---
id: 9547
name: "powerPlant/apsimx-srf"
branch: "master"
tag: "2019.06.05.3920"
commit: "6e59e6919b1cfa1140d84f94f78cf8b530d02ae3"
version: "260a56e3702b395873214ad840343066"
build_date: "2020-10-22T02:42:04.455Z"
size_mb: 992
size: 338460703
sif: "https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2019.06.05.3920/2020-10-22-6e59e691-260a56e3/260a56e3702b395873214ad840343066.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/apsimx-srf/2019.06.05.3920/2020-10-22-6e59e691-260a56e3/
recipe: https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2019.06.05.3920/2020-10-22-6e59e691-260a56e3/Singularity
collection: powerPlant/apsimx-srf
---

# powerPlant/apsimx-srf:2019.06.05.3920

```bash
$ singularity pull shub://powerPlant/apsimx-srf:2019.06.05.3920
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2019.06.05.3920

%setup
  curl --silent -o ${SINGULARITY_ROOTFS}/tmp/ApsimSetup.deb http://www.apsim.info/ApsimXFiles/ApsimSetup3920.deb

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

