---
id: 6755
name: "powerPlant/cdo-srf"
branch: "master"
tag: "1.7.0"
commit: "1803e629ad8da77434925f23932b0e7235d3d547"
version: "c407b2b19a0ca42056ccf6bba226570d"
build_date: "2019-02-05T05:54:32.298Z"
size_mb: 845
size: 233009183
sif: "https://datasets.datalad.org/shub/powerPlant/cdo-srf/1.7.0/2019-02-05-1803e629-c407b2b1/c407b2b19a0ca42056ccf6bba226570d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/cdo-srf/1.7.0/2019-02-05-1803e629-c407b2b1/
recipe: https://datasets.datalad.org/shub/powerPlant/cdo-srf/1.7.0/2019-02-05-1803e629-c407b2b1/Singularity
collection: powerPlant/cdo-srf
---

# powerPlant/cdo-srf:1.7.0

```bash
$ singularity pull shub://powerPlant/cdo-srf:1.7.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 1.7.0

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

