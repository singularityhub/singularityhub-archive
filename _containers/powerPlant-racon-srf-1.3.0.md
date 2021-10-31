---
id: 6782
name: "powerPlant/racon-srf"
branch: "master"
tag: "1.3.0"
commit: "a433d32cb75024bcde882f6383dabaa1675c01a5"
version: "9255f45b341806365355bdc28840a9e2"
build_date: "2019-02-05T05:54:32.459Z"
size_mb: 234
size: 71413791
sif: "https://datasets.datalad.org/shub/powerPlant/racon-srf/1.3.0/2019-02-05-a433d32c-9255f45b/9255f45b341806365355bdc28840a9e2.simg"
url: https://datasets.datalad.org/shub/powerPlant/racon-srf/1.3.0/2019-02-05-a433d32c-9255f45b/
recipe: https://datasets.datalad.org/shub/powerPlant/racon-srf/1.3.0/2019-02-05-a433d32c-9255f45b/Singularity
collection: powerPlant/racon-srf
---

# powerPlant/racon-srf:1.3.0

```bash
$ singularity pull shub://powerPlant/racon-srf:1.3.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: fedora:27

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 1.3.0

%post
  ## Download build prerequisites
  dnf -y install cmake clang gcc libstdc++ make

  curl -OL https://github.com/isovic/racon/releases/download/1.3.0/racon-v1.3.0.tar.gz

  tar -xvf racon-v1.3.0.tar.gz
  cd racon-v1.3.0
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

