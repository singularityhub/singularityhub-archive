---
id: 11318
name: "powerPlant/svaba-srf"
branch: "master"
tag: "latest"
commit: "e621bed5a0d3be41ac268b23206e3c483681d88c"
version: "39284a0a17b7a8fa42236091157cf6627a5a532b0b97ef472c8f2afa615a1f44"
build_date: "2019-10-26T16:51:00.441Z"
size_mb: 80.96875
size: 84901888
sif: "https://datasets.datalad.org/shub/powerPlant/svaba-srf/latest/2019-10-26-e621bed5-39284a0a/39284a0a17b7a8fa42236091157cf6627a5a532b0b97ef472c8f2afa615a1f44.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/svaba-srf/latest/2019-10-26-e621bed5-39284a0a/
recipe: https://datasets.datalad.org/shub/powerPlant/svaba-srf/latest/2019-10-26-e621bed5-39284a0a/Singularity
collection: powerPlant/svaba-srf
---

# powerPlant/svaba-srf:latest

```bash
$ singularity pull shub://powerPlant/svaba-srf:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7
Stage: build

%post
  ## Download build prerequisites
  yum -y install bzip2-devel gcc gcc-c++ git make xz-devel zlib-devel
  
  ## Build and Install
  cd /opt
  git clone --recursive https://github.com/walaj/svaba
  cd svaba
  git checkout c0fecb6
  ./configure
  make

Bootstrap: docker
From: centos:7
Stage: final

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 1.1.3

%files from build
  /opt/svaba/src/svaba/svaba /usr/local/bin

%runscript
  exec svaba "$@"
```

## Collection

 - Name: [powerPlant/svaba-srf](https://github.com/powerPlant/svaba-srf)
 - License: None

