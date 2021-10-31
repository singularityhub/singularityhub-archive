---
id: 13290
name: "powerPlant/gromacs-srf"
branch: "master"
tag: "2019.1"
commit: "d538c597e9e4ece112af14be23676593da265786"
version: "0c7f5cb28a466056829c659348789bf542bc636e034d03fd519c7ddf226c735d"
build_date: "2020-06-09T03:17:30.830Z"
size_mb: 60.54296875
size: 63483904
sif: "https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2019.1/2020-06-09-d538c597-0c7f5cb2/0c7f5cb28a466056829c659348789bf542bc636e034d03fd519c7ddf226c735d.sif"
url: https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2019.1/2020-06-09-d538c597-0c7f5cb2/
recipe: https://datasets.datalad.org/shub/powerPlant/gromacs-srf/2019.1/2020-06-09-d538c597-0c7f5cb2/Singularity
collection: powerPlant/gromacs-srf
---

# powerPlant/gromacs-srf:2019.1

```bash
$ singularity pull shub://powerPlant/gromacs-srf:2019.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2019.1

%setup
  wget -q -O ${SINGULARITY_ROOTFS}/tmp/gromacs-2019.1.tar.gz ftp://ftp.gromacs.org/pub/gromacs/gromacs-2019.1.tar.gz

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install cmake gcc g++
  
  ## Build gromacs 
  cd /tmp
  tar -xzf gromacs-2019.1.tar.gz
  cd gromacs-2019.1
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

