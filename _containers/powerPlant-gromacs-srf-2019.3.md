---
id: 13292
name: "powerPlant/gromacs-srf"
branch: "master"
tag: "2019.3"
commit: "d538c597e9e4ece112af14be23676593da265786"
version: "37078e6d41f3f22cabf0e73e8893dc7ff92b15f61ae693801c8eda320174e1fe"
build_date: "2020-06-09T04:17:48.430Z"
size_mb: 60.5390625
size: 63479808
sif: "https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2019.3/2020-06-09-d538c597-37078e6d/37078e6d41f3f22cabf0e73e8893dc7ff92b15f61ae693801c8eda320174e1fe.sif"
url: https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2019.3/2020-06-09-d538c597-37078e6d/
recipe: https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2019.3/2020-06-09-d538c597-37078e6d/Singularity
collection: powerPlant/gromacs-srf
---

# powerPlant/gromacs-srf:2019.3

```bash
$ singularity pull shub://powerPlant/gromacs-srf:2019.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2019.3

%setup
  wget -q -O ${SINGULARITY_ROOTFS}/tmp/gromacs-2019.3.tar.gz ftp://ftp.gromacs.org/pub/gromacs/gromacs-2019.3.tar.gz

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install cmake gcc g++
  
  ## Build gromacs 
  cd /tmp
  tar -xzf gromacs-2019.3.tar.gz
  cd gromacs-2019.3
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

