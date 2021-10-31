---
id: 14692
name: "powerPlant/apsimx-srf"
branch: "master"
tag: "2020.10.21.5755"
commit: "4885b3ffe72f192e05ed5bf3d757f2cc1cfd6c6d"
version: "e0323fbcf81213e2ff15f171ae2d33b6a6c5e1344e0a531ac5ff26bd460533aa"
build_date: "2020-10-22T02:51:06.767Z"
size_mb: 359.0234375
size: 376463360
sif: "https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2020.10.21.5755/2020-10-22-4885b3ff-e0323fbc/e0323fbcf81213e2ff15f171ae2d33b6a6c5e1344e0a531ac5ff26bd460533aa.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/apsimx-srf/2020.10.21.5755/2020-10-22-4885b3ff-e0323fbc/
recipe: https://datasets.datalad.org/shub/powerPlant/apsimx-srf/2020.10.21.5755/2020-10-22-4885b3ff-e0323fbc/Singularity
collection: powerPlant/apsimx-srf
---

# powerPlant/apsimx-srf:2020.10.21.5755

```bash
$ singularity pull shub://powerPlant/apsimx-srf:2020.10.21.5755
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2020.10.21.5755

%setup
  curl --silent -o ${SINGULARITY_ROOTFS}/ApsimSetup.deb http://apsimdev.apsim.info/ApsimXFiles/ApsimSetup5755.deb

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

