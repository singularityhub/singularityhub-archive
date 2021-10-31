---
id: 6850
name: "powerPlant/salsa-srf"
branch: "master"
tag: "latest"
commit: "69a2f2680392d6f7a2ac8f325a0aa4e83f3965a1"
version: "d7e01f97d32fcd13044e374a3d24e6b5"
build_date: "2019-02-04T09:08:23.920Z"
size_mb: 580
size: 155484191
sif: "https://datasets.datalad.org/shub/powerPlant/salsa-srf/latest/2019-02-04-69a2f268-d7e01f97/d7e01f97d32fcd13044e374a3d24e6b5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/salsa-srf/latest/2019-02-04-69a2f268-d7e01f97/
recipe: https://datasets.datalad.org/shub/powerPlant/salsa-srf/latest/2019-02-04-69a2f268-d7e01f97/Singularity
collection: powerPlant/salsa-srf
---

# powerPlant/salsa-srf:latest

```bash
$ singularity pull shub://powerPlant/salsa-srf:latest
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
python /opt/SALSA-2.2/run_pipeline.py "$@"
```

## Collection

 - Name: [powerPlant/salsa-srf](https://github.com/powerPlant/salsa-srf)
 - License: None

