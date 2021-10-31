---
id: 6760
name: "powerPlant/bismark-srf"
branch: "master"
tag: "0.20.0"
commit: "7e407f114e8063b214f392c541d6793b17182a6b"
version: "37af84131357c5f2a0c40ed165cc2098"
build_date: "2019-02-05T05:54:32.365Z"
size_mb: 288
size: 102805535
sif: "https://datasets.datalad.org/shub/powerPlant/bismark-srf/0.20.0/2019-02-05-7e407f11-37af8413/37af84131357c5f2a0c40ed165cc2098.simg"
url: https://datasets.datalad.org/shub/powerPlant/bismark-srf/0.20.0/2019-02-05-7e407f11-37af8413/
recipe: https://datasets.datalad.org/shub/powerPlant/bismark-srf/0.20.0/2019-02-05-7e407f11-37af8413/Singularity
collection: powerPlant/bismark-srf
---

# powerPlant/bismark-srf:0.20.0

```bash
$ singularity pull shub://powerPlant/bismark-srf:0.20.0
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
  exec bismark "$@"
```

## Collection

 - Name: [powerPlant/bismark-srf](https://github.com/powerPlant/bismark-srf)
 - License: None

