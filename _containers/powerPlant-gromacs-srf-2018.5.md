---
id: 6804
name: "powerPlant/gromacs-srf"
branch: "master"
tag: "2018.5"
commit: "015899b193a56cc479c973e589c6a16e14354e46"
version: "71c0de9896dd60f744ebe6246d320c89"
build_date: "2019-02-01T14:00:56.077Z"
size_mb: 139
size: 62050335
sif: "https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2018.5/2019-02-01-015899b1-71c0de98/71c0de9896dd60f744ebe6246d320c89.simg"
url: https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2018.5/2019-02-01-015899b1-71c0de98/
recipe: https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2018.5/2019-02-01-015899b1-71c0de98/Singularity
collection: powerPlant/gromacs-srf
---

# powerPlant/gromacs-srf:2018.5

```bash
$ singularity pull shub://powerPlant/gromacs-srf:2018.5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2018.5

%setup
  wget -q -O ${SINGULARITY_ROOTFS}/tmp/gromacs-2018.5.tar.gz ftp://ftp.gromacs.org/pub/gromacs/gromacs-2018.5.tar.gz

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install cmake gcc g++
  
  ## Build gromacs 
  cd /tmp
  tar -xzf gromacs-2018.5.tar.gz
  cd gromacs-2018.5
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

