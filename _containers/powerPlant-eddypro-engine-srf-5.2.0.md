---
id: 6796
name: "powerPlant/eddypro-engine-srf"
branch: "master"
tag: "5.2.0"
commit: "d8fad427ea8e058689943cdd37887f38a99897c4"
version: "6663f2ff870f69be603ab7c5f9d1cc48"
build_date: "2019-02-12T08:29:40.442Z"
size_mb: 112
size: 53551135
sif: "https://datasets.datalad.org/shub/powerPlant/eddypro-engine-srf/5.2.0/2019-02-12-d8fad427-6663f2ff/6663f2ff870f69be603ab7c5f9d1cc48.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/eddypro-engine-srf/5.2.0/2019-02-12-d8fad427-6663f2ff/
recipe: https://datasets.datalad.org/shub/powerPlant/eddypro-engine-srf/5.2.0/2019-02-12-d8fad427-6663f2ff/Singularity
collection: powerPlant/eddypro-engine-srf
---

# powerPlant/eddypro-engine-srf:5.2.0

```bash
$ singularity pull shub://powerPlant/eddypro-engine-srf:5.2.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 5.2.0

%environment
 PATH=/eddypro-engine-5.2.0/bin/linux:$PATH
 export PATH

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install gfortran libgfortran4 make wget

  wget -q https://github.com/LI-COR/eddypro-engine/archive/v5.2.0.tar.gz
  tar -xzf v5.2.0.tar.gz
  cd /eddypro-engine-5.2.0/prj
  make Makefile_rp
  make Makefile_fcc

  ## Cleanup
  rm -rf /eddypro-engine-5.2.0/prj /eddypro-engine-5.2.0/src /v5.2.0.tar.gz
  apt-get -y remove --autoremove gfortran make wget
  apt-get -y clean all

%runscript
if [ $# -eq 0 ]; then
  /bin/echo -e 'This Singularity image cannot provide a single entrypoint. Please use `<image-name.simg> <CMD>` or `singularity exec <image-name.simg> <CMD>`, where <CMD> is one of the following:\n'
  exec ls /eddypro-engine-5.2.0/bin/linux
else
  exec "$@"
fi
```

## Collection

 - Name: [powerPlant/eddypro-engine-srf](https://github.com/powerPlant/eddypro-engine-srf)
 - License: None

