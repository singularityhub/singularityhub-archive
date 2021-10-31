---
id: 6784
name: "powerPlant/racon-srf"
branch: "master"
tag: "1.3.2"
commit: "a433d32cb75024bcde882f6383dabaa1675c01a5"
version: "02f3cad9adb4559b8868d9eb60feaa62"
build_date: "2019-02-05T05:54:32.447Z"
size_mb: 234
size: 71413791
sif: "https://datasets.datalad.org/shub/powerPlant/racon-srf/1.3.2/2019-02-05-a433d32c-02f3cad9/02f3cad9adb4559b8868d9eb60feaa62.simg"
url: https://datasets.datalad.org/shub/powerPlant/racon-srf/1.3.2/2019-02-05-a433d32c-02f3cad9/
recipe: https://datasets.datalad.org/shub/powerPlant/racon-srf/1.3.2/2019-02-05-a433d32c-02f3cad9/Singularity
collection: powerPlant/racon-srf
---

# powerPlant/racon-srf:1.3.2

```bash
$ singularity pull shub://powerPlant/racon-srf:1.3.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: fedora:27

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 1.3.2

%post
  ## Download build prerequisites
  dnf -y install cmake clang gcc libstdc++ make

  curl -OL https://github.com/isovic/racon/releases/download/1.3.2/racon-v1.3.2.tar.gz

  tar -xvf racon-v1.3.2.tar.gz
  cd racon-v1.3.2
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

