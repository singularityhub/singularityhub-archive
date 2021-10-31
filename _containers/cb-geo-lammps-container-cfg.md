---
id: 723
name: "cb-geo/lammps-container"
branch: "master"
tag: "cfg"
commit: "c5b476f4efffabbe1e9222022cf5f121956aadd3"
version: "fe2db2b0684dade03ce01f41372de431"
build_date: "2017-11-08T16:12:34.174Z"
size_mb: 1269
size: 485920799
sif: "https://datasets.datalad.org/shub/cb-geo/lammps-container/cfg/2017-11-08-c5b476f4-fe2db2b0/fe2db2b0684dade03ce01f41372de431.simg"
url: https://datasets.datalad.org/shub/cb-geo/lammps-container/cfg/2017-11-08-c5b476f4-fe2db2b0/
recipe: https://datasets.datalad.org/shub/cb-geo/lammps-container/cfg/2017-11-08-c5b476f4-fe2db2b0/Singularity
collection: cb-geo/lammps-container
---

# cb-geo/lammps-container:cfg

```bash
$ singularity pull shub://cb-geo/lammps-container:cfg
```

## Singularity Recipe

```singularity
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

