---
id: 6759
name: "powerPlant/bismark-srf"
branch: "master"
tag: "0.19.1"
commit: "7e407f114e8063b214f392c541d6793b17182a6b"
version: "0213131f630f879988e55d41b20e22c5"
build_date: "2019-02-05T05:54:32.371Z"
size_mb: 274
size: 99037215
sif: "https://datasets.datalad.org/shub/powerPlant/bismark-srf/0.19.1/2019-02-05-7e407f11-0213131f/0213131f630f879988e55d41b20e22c5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/bismark-srf/0.19.1/2019-02-05-7e407f11-0213131f/
recipe: https://datasets.datalad.org/shub/powerPlant/bismark-srf/0.19.1/2019-02-05-7e407f11-0213131f/Singularity
collection: powerPlant/bismark-srf
---

# powerPlant/bismark-srf:0.19.1

```bash
$ singularity pull shub://powerPlant/bismark-srf:0.19.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 0.19.1

%environment
  PATH=/Bismark-0.19.1:$PATH
  export PATH

%post
  ## Download prerequisites
  apt-get update
  apt-get -y install bowtie2 curl libfile-copy-recursive-perl samtools

  curl -OL https://github.com/FelixKrueger/Bismark/archive/0.19.1.tar.gz

  tar -xvf 0.19.1.tar.gz
  
  ## Cleanup
  apt-get -y remove --purge curl
  apt-get -y clean all
  apt-get -y autoremove --purge
  rm -rf /0.19.1.tar.gz

%runscript
  exec bismark "$@"
```

## Collection

 - Name: [powerPlant/bismark-srf](https://github.com/powerPlant/bismark-srf)
 - License: None

