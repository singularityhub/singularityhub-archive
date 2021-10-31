---
id: 6761
name: "powerPlant/gromacs-srf"
branch: "master"
tag: "latest"
commit: "d538c597e9e4ece112af14be23676593da265786"
version: "32264035c1e3d86bee7a79ed9d28296c"
build_date: "2020-11-26T14:34:04.680Z"
size_mb: 140
size: 62357535
sif: "https://datasets.datalad.org/shub/powerPlant/gromacs-srf/latest/2020-11-26-d538c597-32264035/32264035c1e3d86bee7a79ed9d28296c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/gromacs-srf/latest/2020-11-26-d538c597-32264035/
recipe: https://datasets.datalad.org/shub/powerPlant/gromacs-srf/latest/2020-11-26-d538c597-32264035/Singularity
collection: powerPlant/gromacs-srf
---

# powerPlant/gromacs-srf:latest

```bash
$ singularity pull shub://powerPlant/gromacs-srf:latest
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

