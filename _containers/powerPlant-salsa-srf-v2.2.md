---
id: 6851
name: "powerPlant/salsa-srf"
branch: "master"
tag: "v2.2"
commit: "6e7b5933e9c73cad6db188ec787e770345bf858c"
version: "6be7c440f5f51012c6c0ba0900364e00"
build_date: "2019-02-05T05:54:32.614Z"
size_mb: 580
size: 155484191
sif: "https://datasets.datalad.org/shub/powerPlant/salsa-srf/v2.2/2019-02-05-6e7b5933-6be7c440/6be7c440f5f51012c6c0ba0900364e00.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/salsa-srf/v2.2/2019-02-05-6e7b5933-6be7c440/
recipe: https://datasets.datalad.org/shub/powerPlant/salsa-srf/v2.2/2019-02-05-6e7b5933-6be7c440/Singularity
collection: powerPlant/salsa-srf
---

# powerPlant/salsa-srf:v2.2

```bash
$ singularity pull shub://powerPlant/salsa-srf:v2.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: fedora:29

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 2.2

%environment
 PATH=/opt/SALSA-2.2:$PATH
 export PATH

%post
  ## Install build prerequisites
  dnf -y install boost-devel gcc gcc-c++ libgomp make perl python2-networkx-core wget zlib-devel

  cd /opt
  wget https://github.com/machinegun/SALSA/archive/v2.2.tar.gz

  tar -xvf v2.2.tar.gz
  cd /opt/SALSA-2.2
  make
  chmod +x run_pipeline.py

  ## Cleanup
  dnf -y erase boost-devel gcc gcc-c++ wget zlib-devel

  ### Reinstall runtime dependencies
  dnf -y install boost
  dnf -y clean all
  rm -rf /opt/v2.2.tar.gz

%runscript
  exec python /opt/SALSA-2.2/run_pipeline.py "$@"
```

## Collection

 - Name: [powerPlant/salsa-srf](https://github.com/powerPlant/salsa-srf)
 - License: None

