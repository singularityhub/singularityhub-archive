---
id: 6845
name: "powerPlant/eddypro-engine-srf"
branch: "master"
tag: "6.2.0"
commit: "d8fad427ea8e058689943cdd37887f38a99897c4"
version: "6b744cee2dba040f308ea0689e5c6d1d"
build_date: "2019-02-11T22:21:31.705Z"
size_mb: 132
size: 65400863
sif: "https://datasets.datalad.org/shub/powerPlant/eddypro-engine-srf/6.2.0/2019-02-11-d8fad427-6b744cee/6b744cee2dba040f308ea0689e5c6d1d.simg"
url: https://datasets.datalad.org/shub/powerPlant/eddypro-engine-srf/6.2.0/2019-02-11-d8fad427-6b744cee/
recipe: https://datasets.datalad.org/shub/powerPlant/eddypro-engine-srf/6.2.0/2019-02-11-d8fad427-6b744cee/Singularity
collection: powerPlant/eddypro-engine-srf
---

# powerPlant/eddypro-engine-srf:6.2.0

```bash
$ singularity pull shub://powerPlant/eddypro-engine-srf:6.2.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 6.2.0

%environment
 PATH=/eddypro-engine-6.2.0/bin/linux:$PATH
 export PATH

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install gfortran libgfortran4 make wget

  wget -q https://github.com/LI-COR/eddypro-engine/archive/v6.2.0.tar.gz
  tar -xzf v6.2.0.tar.gz
  cd /eddypro-engine-6.2.0/prj
  make rp
  make fcc

  ## Cleanup
  rm -rf /eddypro-engine-6.2.0/prj /eddypro-engine-6.2.0/src /v6.2.0.tar.gz
  apt-get -y remove --autoremove gfortran make wget
  apt-get -y clean all

%runscript
if [[ $# -eq 0 ]]; then
  echo -e "This Singularity image cannot provide a single entrypoint. Please use `<image-name.simg> <CMD>` or `singularity exec <image-name.simg> <CMD>`, where <CMD> is one of the  following:\n"
  ls /eddypro-engine-6.2.0/bin/linux
else
  "$@"
fi
```

## Collection

 - Name: [powerPlant/eddypro-engine-srf](https://github.com/powerPlant/eddypro-engine-srf)
 - License: None

