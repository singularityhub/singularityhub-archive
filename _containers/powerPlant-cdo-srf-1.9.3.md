---
id: 6756
name: "powerPlant/cdo-srf"
branch: "master"
tag: "1.9.3"
commit: "1803e629ad8da77434925f23932b0e7235d3d547"
version: "609d8df2f96fbf514f677923613a0a2e"
build_date: "2019-02-05T05:54:32.292Z"
size_mb: 1490
size: 408752159
sif: "https://datasets.datalad.org/shub/powerPlant/cdo-srf/1.9.3/2019-02-05-1803e629-609d8df2/609d8df2f96fbf514f677923613a0a2e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/cdo-srf/1.9.3/2019-02-05-1803e629-609d8df2/
recipe: https://datasets.datalad.org/shub/powerPlant/cdo-srf/1.9.3/2019-02-05-1803e629-609d8df2/Singularity
collection: powerPlant/cdo-srf
---

# powerPlant/cdo-srf:1.9.3

```bash
$ singularity pull shub://powerPlant/cdo-srf:1.9.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 1.9.3

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

