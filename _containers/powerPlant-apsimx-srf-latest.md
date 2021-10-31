---
id: 6789
name: "powerPlant/apsimx-srf"
branch: "master"
tag: "latest"
commit: "4d50c8535df8763586a96f676900c73fb0e28924"
version: "d14c060082cc86f140c24cbca966506fce0a9634b0c74186d77911e7f32f5bfd"
build_date: "2021-04-16T03:12:12.072Z"
size_mb: 364.7734375
size: 382492672
sif: "https://datasets.datalad.org/shub/powerPlant/apsimx-srf/latest/2021-04-16-4d50c853-d14c0600/d14c060082cc86f140c24cbca966506fce0a9634b0c74186d77911e7f32f5bfd.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/apsimx-srf/latest/2021-04-16-4d50c853-d14c0600/
recipe: https://datasets.datalad.org/shub/powerPlant/apsimx-srf/latest/2021-04-16-4d50c853-d14c0600/Singularity
collection: powerPlant/apsimx-srf
---

# powerPlant/apsimx-srf:latest

```bash
$ singularity pull shub://powerPlant/apsimx-srf:latest
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

