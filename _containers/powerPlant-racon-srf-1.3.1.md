---
id: 6783
name: "powerPlant/racon-srf"
branch: "master"
tag: "1.3.1"
commit: "a433d32cb75024bcde882f6383dabaa1675c01a5"
version: "bc8b548c00e5bc86f1b092357cca1aed"
build_date: "2019-02-05T05:54:32.453Z"
size_mb: 234
size: 71413791
sif: "https://datasets.datalad.org/shub/powerPlant/racon-srf/1.3.1/2019-02-05-a433d32c-bc8b548c/bc8b548c00e5bc86f1b092357cca1aed.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/racon-srf/1.3.1/2019-02-05-a433d32c-bc8b548c/
recipe: https://datasets.datalad.org/shub/powerPlant/racon-srf/1.3.1/2019-02-05-a433d32c-bc8b548c/Singularity
collection: powerPlant/racon-srf
---

# powerPlant/racon-srf:1.3.1

```bash
$ singularity pull shub://powerPlant/racon-srf:1.3.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: fedora:27

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 1.3.1

%post
  ## Download build prerequisites
  dnf -y install cmake clang gcc libstdc++ make

  curl -OL https://github.com/isovic/racon/releases/download/1.3.1/racon-v1.3.1.tar.gz

  tar -xvf racon-v1.3.1.tar.gz
  cd racon-v1.3.1
  mkdir build
  cd build/
  cmake -DCMAKE_BUILD_TYPE=Release ..
  make
  make install

  ## Cleanup
  dnf -y remove cmake clang gcc make
  dnf -y clean all
  rm -rf /racon*

%runscript
  exec racon "$@"
```

## Collection

 - Name: [powerPlant/racon-srf](https://github.com/powerPlant/racon-srf)
 - License: None

