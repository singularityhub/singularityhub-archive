---
id: 13859
name: "powerPlant/apsimx-srf"
branch: "master"
tag: "2020.08.04.5350"
commit: "6e59e6919b1cfa1140d84f94f78cf8b530d02ae3"
version: "67099a9fbeaa47c1eea6db82e94119f6b8b5a359d4bbe05b342be5c8a55243c8"
build_date: "2020-10-22T02:42:04.631Z"
size_mb: 354.0703125
size: 371269632
sif: "https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2020.08.04.5350/2020-10-22-6e59e691-67099a9f/67099a9fbeaa47c1eea6db82e94119f6b8b5a359d4bbe05b342be5c8a55243c8.sif"
url: https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2020.08.04.5350/2020-10-22-6e59e691-67099a9f/
recipe: https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2020.08.04.5350/2020-10-22-6e59e691-67099a9f/Singularity
collection: powerPlant/apsimx-srf
---

# powerPlant/apsimx-srf:2020.08.04.5350

```bash
$ singularity pull shub://powerPlant/apsimx-srf:2020.08.04.5350
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2020.08.04.5350

%setup
  curl --silent -o ${SINGULARITY_ROOTFS}/tmp/ApsimSetup.deb http://apsimdev.apsim.info/ApsimXFiles/ApsimSetup5350.deb

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

