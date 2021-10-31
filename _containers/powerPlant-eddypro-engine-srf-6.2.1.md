---
id: 6846
name: "powerPlant/eddypro-engine-srf"
branch: "master"
tag: "6.2.1"
commit: "d8fad427ea8e058689943cdd37887f38a99897c4"
version: "ea5cc11d2d81d8bc7d21dcf904052132"
build_date: "2019-02-11T22:21:31.730Z"
size_mb: 132
size: 65400863
sif: "https://datasets.datalad.org/shub/powerPlant/eddypro-engine-srf/6.2.1/2019-02-11-d8fad427-ea5cc11d/ea5cc11d2d81d8bc7d21dcf904052132.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/eddypro-engine-srf/6.2.1/2019-02-11-d8fad427-ea5cc11d/
recipe: https://datasets.datalad.org/shub/powerPlant/eddypro-engine-srf/6.2.1/2019-02-11-d8fad427-ea5cc11d/Singularity
collection: powerPlant/eddypro-engine-srf
---

# powerPlant/eddypro-engine-srf:6.2.1

```bash
$ singularity pull shub://powerPlant/eddypro-engine-srf:6.2.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 6.2.1

%environment
 PATH=/eddypro-engine-6.2.1/bin/linux:$PATH
 export PATH

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install gfortran libgfortran4 make wget

  wget -q https://github.com/LI-COR/eddypro-engine/archive/v6.2.1.tar.gz
  tar -xzf v6.2.1.tar.gz
  cd /eddypro-engine-6.2.1/prj
  make rp
  make fcc

  ## Cleanup
  rm -rf /eddypro-engine-6.2.1/prj /eddypro-engine-6.2.1/src /v6.2.1.tar.gz
  apt-get -y remove --autoremove gfortran make wget
  apt-get -y clean all

%runscript
if [[ $# -eq 0 ]]; then
  echo -e "This Singularity image cannot provide a single entrypoint. Please use `<image-name.simg> <CMD>` or `singularity exec <image-name.simg> <CMD>`, where <CMD> is one of the  following:\n"
  ls /eddypro-engine-6.2.1/bin/linux
else
  "$@"
fi
```

## Collection

 - Name: [powerPlant/eddypro-engine-srf](https://github.com/powerPlant/eddypro-engine-srf)
 - License: None

