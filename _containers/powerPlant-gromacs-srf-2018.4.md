---
id: 6803
name: "powerPlant/gromacs-srf"
branch: "master"
tag: "2018.4"
commit: "015899b193a56cc479c973e589c6a16e14354e46"
version: "6df71697a09921682e88ca8c0745eacd"
build_date: "2019-02-01T14:00:56.083Z"
size_mb: 139
size: 62050335
sif: "https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2018.4/2019-02-01-015899b1-6df71697/6df71697a09921682e88ca8c0745eacd.simg"
url: https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2018.4/2019-02-01-015899b1-6df71697/
recipe: https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2018.4/2019-02-01-015899b1-6df71697/Singularity
collection: powerPlant/gromacs-srf
---

# powerPlant/gromacs-srf:2018.4

```bash
$ singularity pull shub://powerPlant/gromacs-srf:2018.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2018.4

%setup
  wget -q -O ${SINGULARITY_ROOTFS}/tmp/gromacs-2018.4.tar.gz ftp://ftp.gromacs.org/pub/gromacs/gromacs-2018.4.tar.gz

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install cmake gcc g++
  
  ## Build gromacs 
  cd /tmp
  tar -xzf gromacs-2018.4.tar.gz
  cd gromacs-2018.4
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

