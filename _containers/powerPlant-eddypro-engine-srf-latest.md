---
id: 6794
name: "powerPlant/eddypro-engine-srf"
branch: "master"
tag: "latest"
commit: "07aefcc438c0f5f10a1f5de88a836c3e0b7a9fc1"
version: "be00904375d8e737f016ef39257f9444"
build_date: "2019-02-01T14:00:56.299Z"
size_mb: 132
size: 65376287
sif: "https://datasets.datalad.org/shub/powerPlant/eddypro-engine-srf/latest/2019-02-01-07aefcc4-be009043/be00904375d8e737f016ef39257f9444.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/eddypro-engine-srf/latest/2019-02-01-07aefcc4-be009043/
recipe: https://datasets.datalad.org/shub/powerPlant/eddypro-engine-srf/latest/2019-02-01-07aefcc4-be009043/Singularity
collection: powerPlant/eddypro-engine-srf
---

# powerPlant/eddypro-engine-srf:latest

```bash
$ singularity pull shub://powerPlant/eddypro-engine-srf:latest
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

