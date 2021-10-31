---
id: 11680
name: "powerPlant/mrbayes-srf"
branch: "master"
tag: "3.2.7a-gpu"
commit: "0e6fcd3af7180d2348fac9613eec7b65cb7a8a89"
version: "d14daca964292075551ab6a655524e89bbe0eb1ba57a344e5a0698ab84e55dbb"
build_date: "2019-11-21T08:43:23.627Z"
size_mb: 89.265625
size: 93601792
sif: "https://datasets.datalad.org/shub/powerPlant/mrbayes-srf/3.2.7a-gpu/2019-11-21-0e6fcd3a-d14daca9/d14daca964292075551ab6a655524e89bbe0eb1ba57a344e5a0698ab84e55dbb.sif"
url: https://datasets.datalad.org/shub/powerPlant/mrbayes-srf/3.2.7a-gpu/2019-11-21-0e6fcd3a-d14daca9/
recipe: https://datasets.datalad.org/shub/powerPlant/mrbayes-srf/3.2.7a-gpu/2019-11-21-0e6fcd3a-d14daca9/Singularity
collection: powerPlant/mrbayes-srf
---

# powerPlant/mrbayes-srf:3.2.7a-gpu

```bash
$ singularity pull shub://powerPlant/mrbayes-srf:3.2.7a-gpu
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: powerPlant/open-mpi-srf:4.0.2

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 3.2.7a with OpenMPI 4.0.2

%post
  ## Download prerequisites
  apt-get -y install g++ libhmsbeagle1v5 libhmsbeagle-dev libnvidia-compute-430 make ocl-icd-libopencl1 wget
  
  ## Build
  cd /opt
  wget https://github.com/NBISweden/MrBayes/releases/download/v3.2.7a/mrbayes-3.2.7a.tar.gz
  tar -xzf mrbayes-3.2.7a.tar.gz
  cd mrbayes-3.2.7a
  ./configure
  make -j`nproc` install

  ## Cleanup
  apt-get -y remove g++ libhmsbeagle-dev make wget
  apt-get -y autoremove
  rm -rf /opt/*

%runscript
  exec mb "$@"
```

## Collection

 - Name: [powerPlant/mrbayes-srf](https://github.com/powerPlant/mrbayes-srf)
 - License: None

