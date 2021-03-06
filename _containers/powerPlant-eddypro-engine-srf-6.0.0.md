---
id: 6847
name: "powerPlant/eddypro-engine-srf"
branch: "master"
tag: "6.0.0"
commit: "d8fad427ea8e058689943cdd37887f38a99897c4"
version: "f2c0f0b8cb15c877214eaeb0f65469fd"
build_date: "2019-02-12T08:29:40.430Z"
size_mb: 134
size: 65286175
sif: "https://datasets.datalad.org/shub/powerPlant/eddypro-engine-srf/6.0.0/2019-02-12-d8fad427-f2c0f0b8/f2c0f0b8cb15c877214eaeb0f65469fd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/eddypro-engine-srf/6.0.0/2019-02-12-d8fad427-f2c0f0b8/
recipe: https://datasets.datalad.org/shub/powerPlant/eddypro-engine-srf/6.0.0/2019-02-12-d8fad427-f2c0f0b8/Singularity
collection: powerPlant/eddypro-engine-srf
---

# powerPlant/eddypro-engine-srf:6.0.0

```bash
$ singularity pull shub://powerPlant/eddypro-engine-srf:6.0.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 6.0.0

%environment
 PATH=/eddypro-engine-6.0.0/bin/linux:$PATH
 export PATH

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install gfortran libgfortran4 make wget

  wget -q https://github.com/LI-COR/eddypro-engine/archive/v6.0.0.tar.gz
  tar -xzf v6.0.0.tar.gz
  cd /eddypro-engine-6.0.0/prj
  make -f Makefile_rp_linux eddypro_rp
  make -f Makefile_fcc_linux eddypro_fcc

  ## Cleanup
  rm -rf /eddypro-engine-6.0.0/prj /eddypro-engine-6.0.0/src /v6.0.0.tar.gz
  apt-get -y remove --autoremove gfortran make wget
  apt-get -y clean all

%runscript
if [ $# -eq 0 ]; then
  /bin/echo -e 'This Singularity image cannot provide a single entrypoint. Please use `<image-name.simg> <CMD>` or `singularity exec <image-name.simg> <CMD>`, where <CMD> is one of the following:\n'
  exec ls /eddypro-engine-6.0.0/bin/linux
else
  exec "$@"
fi
```

## Collection

 - Name: [powerPlant/eddypro-engine-srf](https://github.com/powerPlant/eddypro-engine-srf)
 - License: None

