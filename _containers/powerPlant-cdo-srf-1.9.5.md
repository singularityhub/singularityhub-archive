---
id: 6757
name: "powerPlant/cdo-srf"
branch: "master"
tag: "1.9.5"
commit: "1803e629ad8da77434925f23932b0e7235d3d547"
version: "f919a4e58cd63666a74e72048a199fb5"
build_date: "2019-02-05T05:54:32.285Z"
size_mb: 1462
size: 465436703
sif: "https://datasets.datalad.org/shub/powerPlant/cdo-srf/1.9.5/2019-02-05-1803e629-f919a4e5/f919a4e58cd63666a74e72048a199fb5.simg"
url: https://datasets.datalad.org/shub/powerPlant/cdo-srf/1.9.5/2019-02-05-1803e629-f919a4e5/
recipe: https://datasets.datalad.org/shub/powerPlant/cdo-srf/1.9.5/2019-02-05-1803e629-f919a4e5/Singularity
collection: powerPlant/cdo-srf
---

# powerPlant/cdo-srf:1.9.5

```bash
$ singularity pull shub://powerPlant/cdo-srf:1.9.5
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
  exec cdo "$@"
```

## Collection

 - Name: [powerPlant/cdo-srf](https://github.com/powerPlant/cdo-srf)
 - License: None

