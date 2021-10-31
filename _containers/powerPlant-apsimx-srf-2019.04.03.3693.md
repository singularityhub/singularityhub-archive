---
id: 8110
name: "powerPlant/apsimx-srf"
branch: "master"
tag: "2019.04.03.3693"
commit: "6e59e6919b1cfa1140d84f94f78cf8b530d02ae3"
version: "585d445601b527533077e5844621a9a0"
build_date: "2020-10-22T02:42:04.415Z"
size_mb: 942
size: 331186207
sif: "https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2019.04.03.3693/2020-10-22-6e59e691-585d4456/585d445601b527533077e5844621a9a0.simg"
url: https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2019.04.03.3693/2020-10-22-6e59e691-585d4456/
recipe: https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2019.04.03.3693/2020-10-22-6e59e691-585d4456/Singularity
collection: powerPlant/apsimx-srf
---

# powerPlant/apsimx-srf:2019.04.03.3693

```bash
$ singularity pull shub://powerPlant/apsimx-srf:2019.04.03.3693
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2019.04.03.3693

%setup
  curl --silent -o ${SINGULARITY_ROOTFS}/tmp/ApsimSetup.deb http://www.apsim.info/ApsimXFiles/ApsimSetup3693.deb

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

