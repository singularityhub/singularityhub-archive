---
id: 6854
name: "powerPlant/gromacs-srf"
branch: "master"
tag: "2019"
commit: "015899b193a56cc479c973e589c6a16e14354e46"
version: "e2a14d071a961d53ea1799a35b982269"
build_date: "2019-02-04T09:08:23.788Z"
size_mb: 140
size: 62382111
sif: "https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2019/2019-02-04-015899b1-e2a14d07/e2a14d071a961d53ea1799a35b982269.simg"
url: https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2019/2019-02-04-015899b1-e2a14d07/
recipe: https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2019/2019-02-04-015899b1-e2a14d07/Singularity
collection: powerPlant/gromacs-srf
---

# powerPlant/gromacs-srf:2019

```bash
$ singularity pull shub://powerPlant/gromacs-srf:2019
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2019

%setup
  wget -q -O ${SINGULARITY_ROOTFS}/tmp/gromacs-2019.tar.gz ftp://ftp.gromacs.org/pub/gromacs/gromacs-2019.tar.gz

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install cmake gcc g++
  
  ## Build gromacs 
  cd /tmp
  tar -xzf gromacs-2019.tar.gz
  cd gromacs-2019
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

