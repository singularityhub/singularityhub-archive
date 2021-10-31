---
id: 722
name: "cb-geo/lammps-container"
branch: "master"
tag: "latest"
commit: "6ff797380c5ce21416e9897ab7742d72bdf192a4"
version: "61de148d0e8ba4a442cbcad158514300"
build_date: "2021-04-05T13:20:16.633Z"
size_mb: 1337
size: 502829087
sif: "https://datasets.datalad.org/shub/cb-geo/lammps-container/latest/2021-04-05-6ff79738-61de148d/61de148d0e8ba4a442cbcad158514300.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cb-geo/lammps-container/latest/2021-04-05-6ff79738-61de148d/
recipe: https://datasets.datalad.org/shub/cb-geo/lammps-container/latest/2021-04-05-6ff79738-61de148d/Singularity
collection: cb-geo/lammps-container
---

# cb-geo/lammps-container:latest

```bash
$ singularity pull shub://cb-geo/lammps-container:latest
```

## Singularity Recipe

```singularity
# LAMMPS Serial with Granular
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%setup
  cd $SINGULARITY_ROOTFS/opt
  wget http://lammps.sandia.gov/tars/lammps-stable.tar.gz

%post
  yum -y groupinstall "Development Tools"

  mkdir -p /opt/lammps
  cd /opt/lammps
  tar xf ../lammps-stable.tar.gz --strip-components 1

  cd src
  make yes-granular |& tee log.make_yes_granular
  make -j serial |& tee log.make_serial

%runscript
  /opt/lammps/src/lmp_serial "$@"
```

## Collection

 - Name: [cb-geo/lammps-container](https://github.com/cb-geo/lammps-container)
 - License: None

