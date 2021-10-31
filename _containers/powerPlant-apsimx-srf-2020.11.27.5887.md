---
id: 15004
name: "powerPlant/apsimx-srf"
branch: "master"
tag: "2020.11.27.5887"
commit: "1ca931ac4522018c859ff417f84c660d3a0d8515"
version: "e3bd867afd43593d5d7384890bd45205e69f47987fc311dfb31996b2abbe63fb"
build_date: "2020-11-30T00:23:14.010Z"
size_mb: 362.3203125
size: 379920384
sif: "https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2020.11.27.5887/2020-11-30-1ca931ac-e3bd867a/e3bd867afd43593d5d7384890bd45205e69f47987fc311dfb31996b2abbe63fb.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/apsimx-srf/2020.11.27.5887/2020-11-30-1ca931ac-e3bd867a/
recipe: https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2020.11.27.5887/2020-11-30-1ca931ac-e3bd867a/Singularity
collection: powerPlant/apsimx-srf
---

# powerPlant/apsimx-srf:2020.11.27.5887

```bash
$ singularity pull shub://powerPlant/apsimx-srf:2020.11.27.5887
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2020.11.27.5887

%setup
  curl --silent -o ${SINGULARITY_ROOTFS}/ApsimSetup.deb http://apsimdev.apsim.info/ApsimXFiles/ApsimSetup5887.deb

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

