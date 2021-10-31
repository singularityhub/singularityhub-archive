---
id: 7075
name: "powerPlant/crema-srf"
branch: "master"
tag: "latest"
commit: "45e6e823d6e66138a96b5acd1524dece2ae7eb5a"
version: "8a031fa01334bb076f4fe687219bc55f"
build_date: "2019-02-15T05:11:19.197Z"
size_mb: 1312
size: 520540191
sif: "https://datasets.datalad.org/shub/powerPlant/crema-srf/latest/2019-02-15-45e6e823-8a031fa0/8a031fa01334bb076f4fe687219bc55f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/crema-srf/latest/2019-02-15-45e6e823-8a031fa0/
recipe: https://datasets.datalad.org/shub/powerPlant/crema-srf/latest/2019-02-15-45e6e823-8a031fa0/Singularity
collection: powerPlant/crema-srf
---

# powerPlant/crema-srf:latest

```bash
$ singularity pull shub://powerPlant/crema-srf:latest
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

