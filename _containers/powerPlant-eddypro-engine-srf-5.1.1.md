---
id: 6795
name: "powerPlant/eddypro-engine-srf"
branch: "master"
tag: "5.1.1"
commit: "d8fad427ea8e058689943cdd37887f38a99897c4"
version: "f1699c5e75d60add48e206f88e94f4f7"
build_date: "2019-02-12T08:29:40.448Z"
size_mb: 112
size: 53551135
sif: "https://datasets.datalad.org/shub/powerPlant/eddypro-engine-srf/5.1.1/2019-02-12-d8fad427-f1699c5e/f1699c5e75d60add48e206f88e94f4f7.simg"
url: https://datasets.datalad.org/shub/powerPlant/eddypro-engine-srf/5.1.1/2019-02-12-d8fad427-f1699c5e/
recipe: https://datasets.datalad.org/shub/powerPlant/eddypro-engine-srf/5.1.1/2019-02-12-d8fad427-f1699c5e/Singularity
collection: powerPlant/eddypro-engine-srf
---

# powerPlant/eddypro-engine-srf:5.1.1

```bash
$ singularity pull shub://powerPlant/eddypro-engine-srf:5.1.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 5.1.1

%environment
 PATH=/eddypro-engine-5.1.1/bin/linux:$PATH
 export PATH

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install gfortran libgfortran4 make wget

  wget -q https://github.com/LI-COR/eddypro-engine/archive/v5.1.1.tar.gz
  tar -xzf v5.1.1.tar.gz
  cd /eddypro-engine-5.1.1/prj
  make Makefile_rp
  make Makefile_fcc

  ## Cleanup
  rm -rf /eddypro-engine-5.1.1/prj /eddypro-engine-5.1.1/src /v5.1.1.tar.gz
  apt-get -y remove --autoremove gfortran make wget
  apt-get -y clean all

%runscript
if [ $# -eq 0 ]; then
  /bin/echo -e 'This Singularity image cannot provide a single entrypoint. Please use `<image-name.simg> <CMD>` or `singularity exec <image-name.simg> <CMD>`, where <CMD> is one of the following:\n'
  exec ls /eddypro-engine-5.1.1/bin/linux
else
  exec "$@"
fi
```

## Collection

 - Name: [powerPlant/eddypro-engine-srf](https://github.com/powerPlant/eddypro-engine-srf)
 - License: None

