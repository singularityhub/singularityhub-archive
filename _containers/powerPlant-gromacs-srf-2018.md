---
id: 6762
name: "powerPlant/gromacs-srf"
branch: "master"
tag: "2018"
commit: "f2951e2a20a5f090fff26f30a7a77b2f737f0191"
version: "aa7a706d923792f0dc8e10a3f01227f7"
build_date: "2019-02-01T14:00:56.107Z"
size_mb: 139
size: 62148639
sif: "https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2018/2019-02-01-f2951e2a-aa7a706d/aa7a706d923792f0dc8e10a3f01227f7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/gromacs-srf/2018/2019-02-01-f2951e2a-aa7a706d/
recipe: https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2018/2019-02-01-f2951e2a-aa7a706d/Singularity
collection: powerPlant/gromacs-srf
---

# powerPlant/gromacs-srf:2018

```bash
$ singularity pull shub://powerPlant/gromacs-srf:2018
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2018

%setup
  wget -q -O ${SINGULARITY_ROOTFS}/tmp/gromacs-2018.tar.gz ftp://ftp.gromacs.org/pub/gromacs/gromacs-2018.tar.gz

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install cmake gcc g++
  
  ## Build gromacs 
  cd /tmp
  tar -xzf gromacs-2018.tar.gz
  cd gromacs-2018
  mkdir build
  cd build
  cmake .. -DGMX_BUILD_OWN_FFTW=ON
  make -j 4
  make install
  
  ## Cleanup
  cd /tmp
  rm -rf /tmp/gromacs*
  apt-get -y remove --purge cmake gcc g++
  apt-get -y clean all
  apt-get -y autoremove --purge

  ## Reinstall libogmp
  apt-get -y install libgomp1

%runscript
  . /usr/local/gromacs/bin/GMXRC.bash
  gmx "$@"
```

## Collection

 - Name: [powerPlant/gromacs-srf](https://github.com/powerPlant/gromacs-srf)
 - License: None

