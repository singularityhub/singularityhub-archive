---
id: 6763
name: "powerPlant/gromacs-srf"
branch: "master"
tag: "2018.1"
commit: "f2951e2a20a5f090fff26f30a7a77b2f737f0191"
version: "7b047e14204d303359edf97c1c1fe1b6"
build_date: "2019-02-01T14:00:56.100Z"
size_mb: 139
size: 62144543
sif: "https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2018.1/2019-02-01-f2951e2a-7b047e14/7b047e14204d303359edf97c1c1fe1b6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/gromacs-srf/2018.1/2019-02-01-f2951e2a-7b047e14/
recipe: https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2018.1/2019-02-01-f2951e2a-7b047e14/Singularity
collection: powerPlant/gromacs-srf
---

# powerPlant/gromacs-srf:2018.1

```bash
$ singularity pull shub://powerPlant/gromacs-srf:2018.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2018.1

%setup
  wget -q -O ${SINGULARITY_ROOTFS}/tmp/gromacs-2018.1.tar.gz ftp://ftp.gromacs.org/pub/gromacs/gromacs-2018.1.tar.gz

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install cmake gcc g++
  
  ## Build gromacs 
  cd /tmp
  tar -xzf gromacs-2018.1.tar.gz
  cd gromacs-2018.1
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

