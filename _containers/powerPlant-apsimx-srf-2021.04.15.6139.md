---
id: 15909
name: "powerPlant/apsimx-srf"
branch: "master"
tag: "2021.04.15.6139"
commit: "4d50c8535df8763586a96f676900c73fb0e28924"
version: "c79f2dec05096ca95cc1b47defd3b21d29e332f0442e648834cdec849ccfd725"
build_date: "2021-04-16T03:03:58.790Z"
size_mb: 364.7734375
size: 382492672
sif: "https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2021.04.15.6139/2021-04-16-4d50c853-c79f2dec/c79f2dec05096ca95cc1b47defd3b21d29e332f0442e648834cdec849ccfd725.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/apsimx-srf/2021.04.15.6139/2021-04-16-4d50c853-c79f2dec/
recipe: https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2021.04.15.6139/2021-04-16-4d50c853-c79f2dec/Singularity
collection: powerPlant/apsimx-srf
---

# powerPlant/apsimx-srf:2021.04.15.6139

```bash
$ singularity pull shub://powerPlant/apsimx-srf:2021.04.15.6139
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2021.04.15.6139

%setup
  curl --silent -o ${SINGULARITY_ROOTFS}/ApsimSetup.deb http://apsimdev.apsim.info/ApsimXFiles/ApsimSetup6139.deb

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

