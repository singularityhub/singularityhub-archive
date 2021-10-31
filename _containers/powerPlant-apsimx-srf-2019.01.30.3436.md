---
id: 6793
name: "powerPlant/apsimx-srf"
branch: "master"
tag: "2019.01.30.3436"
commit: "6e59e6919b1cfa1140d84f94f78cf8b530d02ae3"
version: "8ad9b80b2048a8d68ab238a2620de972"
build_date: "2020-10-22T02:42:04.375Z"
size_mb: 940
size: 330739743
sif: "https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2019.01.30.3436/2020-10-22-6e59e691-8ad9b80b/8ad9b80b2048a8d68ab238a2620de972.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/apsimx-srf/2019.01.30.3436/2020-10-22-6e59e691-8ad9b80b/
recipe: https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2019.01.30.3436/2020-10-22-6e59e691-8ad9b80b/Singularity
collection: powerPlant/apsimx-srf
---

# powerPlant/apsimx-srf:2019.01.30.3436

```bash
$ singularity pull shub://powerPlant/apsimx-srf:2019.01.30.3436
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2019.01.30.3436

%setup
  curl --silent -o ${SINGULARITY_ROOTFS}/tmp/ApsimSetup.deb http://www.apsim.info/ApsimXFiles/ApsimSetup3436.deb

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

