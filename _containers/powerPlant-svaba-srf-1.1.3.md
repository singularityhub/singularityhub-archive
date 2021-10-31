---
id: 11414
name: "powerPlant/svaba-srf"
branch: "master"
tag: "1.1.3"
commit: "e621bed5a0d3be41ac268b23206e3c483681d88c"
version: "679e0dbdb9b97f80390752db999d298944bbf2df6aeb3e1346db665830c7c7ee"
build_date: "2019-10-29T21:35:56.032Z"
size_mb: 80.96875
size: 84901888
sif: "https://datasets.datalad.org/shub/powerPlant/svaba-srf/1.1.3/2019-10-29-e621bed5-679e0dbd/679e0dbdb9b97f80390752db999d298944bbf2df6aeb3e1346db665830c7c7ee.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/svaba-srf/1.1.3/2019-10-29-e621bed5-679e0dbd/
recipe: https://datasets.datalad.org/shub/powerPlant/svaba-srf/1.1.3/2019-10-29-e621bed5-679e0dbd/Singularity
collection: powerPlant/svaba-srf
---

# powerPlant/svaba-srf:1.1.3

```bash
$ singularity pull shub://powerPlant/svaba-srf:1.1.3
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

