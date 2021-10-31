---
id: 6758
name: "powerPlant/bismark-srf"
branch: "master"
tag: "latest"
commit: "6902b7d2eded6c21c4c804bed5301bd7ba4e7a16"
version: "3285abafa09091fd1122b61c1f161fe6"
build_date: "2019-01-31T22:31:30.567Z"
size_mb: 288
size: 102764575
sif: "https://datasets.datalad.org/shub/powerPlant/bismark-srf/latest/2019-01-31-6902b7d2-3285abaf/3285abafa09091fd1122b61c1f161fe6.simg"
url: https://datasets.datalad.org/shub/powerPlant/bismark-srf/latest/2019-01-31-6902b7d2-3285abaf/
recipe: https://datasets.datalad.org/shub/powerPlant/bismark-srf/latest/2019-01-31-6902b7d2-3285abaf/Singularity
collection: powerPlant/bismark-srf
---

# powerPlant/bismark-srf:latest

```bash
$ singularity pull shub://powerPlant/bismark-srf:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 0.20.0

%environment
 PATH=/Bismark-0.20.0:$PATH
 export PATH

%post
  ## Download prerequisites
  apt-get update
  apt-get -y install bowtie2 curl libfile-copy-recursive-perl samtools

  curl -OL https://github.com/FelixKrueger/Bismark/archive/0.20.0.tar.gz

  tar -xvf 0.20.0.tar.gz
  
  ## Cleanup
  apt-get -y remove --purge curl
  apt-get -y clean all
  apt-get -y autoremove --purge
  rm -rf /0.20.0.tar.gz

%runscript
bismark "$@"
```

## Collection

 - Name: [powerPlant/bismark-srf](https://github.com/powerPlant/bismark-srf)
 - License: None

