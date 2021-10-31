---
id: 6792
name: "powerPlant/apsimx-srf"
branch: "master"
tag: "2019.01.08.3392"
commit: "6e59e6919b1cfa1140d84f94f78cf8b530d02ae3"
version: "ba3ba1964ad4844339bd360b71e55ccf6ac1be4beafcbca8be076ee51dfde1b6"
build_date: "2020-10-22T03:16:01.454Z"
size_mb: 322.2890625
size: 337944576
sif: "https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2019.01.08.3392/2020-10-22-6e59e691-ba3ba196/ba3ba1964ad4844339bd360b71e55ccf6ac1be4beafcbca8be076ee51dfde1b6.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/apsimx-srf/2019.01.08.3392/2020-10-22-6e59e691-ba3ba196/
recipe: https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2019.01.08.3392/2020-10-22-6e59e691-ba3ba196/Singularity
collection: powerPlant/apsimx-srf
---

# powerPlant/apsimx-srf:2019.01.08.3392

```bash
$ singularity pull shub://powerPlant/apsimx-srf:2019.01.08.3392
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2019.01.08.3392

%setup
  curl --silent -o ${SINGULARITY_ROOTFS}/ApsimSetup.deb http://apsimdev.apsim.info/ApsimXFiles/ApsimSetup3392.deb

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

