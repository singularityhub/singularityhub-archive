---
id: 13293
name: "powerPlant/gromacs-srf"
branch: "master"
tag: "2019.4"
commit: "d538c597e9e4ece112af14be23676593da265786"
version: "ca0ad33456559c3173f5d4627f46297f5ae0ddbeb904d3a4067ae3de1d27eabb"
build_date: "2020-06-09T04:47:41.214Z"
size_mb: 60.54296875
size: 63483904
sif: "https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2019.4/2020-06-09-d538c597-ca0ad334/ca0ad33456559c3173f5d4627f46297f5ae0ddbeb904d3a4067ae3de1d27eabb.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/gromacs-srf/2019.4/2020-06-09-d538c597-ca0ad334/
recipe: https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2019.4/2020-06-09-d538c597-ca0ad334/Singularity
collection: powerPlant/gromacs-srf
---

# powerPlant/gromacs-srf:2019.4

```bash
$ singularity pull shub://powerPlant/gromacs-srf:2019.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2019.4

%setup
  wget -q -O ${SINGULARITY_ROOTFS}/tmp/gromacs-2019.4.tar.gz ftp://ftp.gromacs.org/pub/gromacs/gromacs-2019.4.tar.gz

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install cmake gcc g++
  
  ## Build gromacs 
  cd /tmp
  tar -xzf gromacs-2019.4.tar.gz
  cd gromacs-2019.4
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

