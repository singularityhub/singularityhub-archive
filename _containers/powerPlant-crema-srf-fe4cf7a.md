---
id: 7247
name: "powerPlant/crema-srf"
branch: "master"
tag: "fe4cf7a"
commit: "45e6e823d6e66138a96b5acd1524dece2ae7eb5a"
version: "14bbcd97ddf727f768ae6b498576197b"
build_date: "2019-02-15T05:11:19.189Z"
size_mb: 1312
size: 520540191
sif: "https://datasets.datalad.org/shub/powerPlant/crema-srf/fe4cf7a/2019-02-15-45e6e823-14bbcd97/14bbcd97ddf727f768ae6b498576197b.simg"
url: https://datasets.datalad.org/shub/powerPlant/crema-srf/fe4cf7a/2019-02-15-45e6e823-14bbcd97/
recipe: https://datasets.datalad.org/shub/powerPlant/crema-srf/fe4cf7a/2019-02-15-45e6e823-14bbcd97/Singularity
collection: powerPlant/crema-srf
---

# powerPlant/crema-srf:fe4cf7a

```bash
$ singularity pull shub://powerPlant/crema-srf:fe4cf7a
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version fe4cf7a

%post
  ## Download build prerequisites
  apt-get -y update
  apt-get -y install git python python-pip python3 python3-pip r-base
  pip install CPAT
  pip3 install biopython scikit-learn pandas

  cd /opt
  git clone https://github.com/gbgolding/crema.git
  cd crema
  git checkout fe4cf7a
  chmod +x bin/predict.py

  ## Cleanup
  apt-get -y remove git python-pip python3-pip
  apt-get -y autoremove
  apt-get -y clean all

%runscript
  exec python3 /opt/crema/bin/predict.py "$@"
```

## Collection

 - Name: [powerPlant/crema-srf](https://github.com/powerPlant/crema-srf)
 - License: None

