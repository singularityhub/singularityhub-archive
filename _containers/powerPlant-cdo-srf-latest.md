---
id: 6754
name: "powerPlant/cdo-srf"
branch: "master"
tag: "latest"
commit: "690bb96e061dfe7d13270b4eabcb51f0a49253b7"
version: "23af1c8401224323f02389fcc32aedcc"
build_date: "2019-01-31T21:34:14.440Z"
size_mb: 1462
size: 465399839
sif: "https://datasets.datalad.org/shub/powerPlant/cdo-srf/latest/2019-01-31-690bb96e-23af1c84/23af1c8401224323f02389fcc32aedcc.simg"
url: https://datasets.datalad.org/shub/powerPlant/cdo-srf/latest/2019-01-31-690bb96e-23af1c84/
recipe: https://datasets.datalad.org/shub/powerPlant/cdo-srf/latest/2019-01-31-690bb96e-23af1c84/Singularity
collection: powerPlant/cdo-srf
---

# powerPlant/cdo-srf:latest

```bash
$ singularity pull shub://powerPlant/cdo-srf:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:cosmic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 1.9.5

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install tzdata
  ln -fs /usr/share/zoneinfo/Pacific/Auckland /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
  apt-get -y install cdo
  
  ## Cleanup
  apt-get -y clean all

%runscript
  cdo "$@"
```

## Collection

 - Name: [powerPlant/cdo-srf](https://github.com/powerPlant/cdo-srf)
 - License: None

