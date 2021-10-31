---
id: 2659
name: "spco/singularity-recipes"
branch: "master"
tag: "milc-intel"
commit: "5db066f23d5889befa8c568e08ff73d43943a4dd"
version: "03a1b690bbfa1baec78c6889ef51c5ea"
build_date: "2018-04-26T16:28:57.007Z"
size_mb: 284
size: 84979743
sif: "https://datasets.datalad.org/shub/spco/singularity-recipes/milc-intel/2018-04-26-5db066f2-03a1b690/03a1b690bbfa1baec78c6889ef51c5ea.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/spco/singularity-recipes/milc-intel/2018-04-26-5db066f2-03a1b690/
recipe: https://datasets.datalad.org/shub/spco/singularity-recipes/milc-intel/2018-04-26-5db066f2-03a1b690/Singularity
collection: spco/singularity-recipes
---

# spco/singularity-recipes:milc-intel

```bash
$ singularity pull shub://spco/singularity-recipes:milc-intel
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/

Include: yum

%help
  echo "This is a container to run MILC on CentOS compiled under Intel. This uses a pair of pre-compiled binaries from ALICE2, sotred on GitHub, and requiring AVX to run."

%setup
  mkdir ${SINGULARITY_ROOTFS}/MILC-Intel

%files
  qla_bench-qla-1.7.1-f3 /MILC-Intel
  qla_bench-qla-1.7.1-d3 /MILC-Intel

%post
  chmod -R 777 /MILC-Intel
  exit 0

%runscript
  cd /MILC-Intel
  export OMP_NUM_THREADS=16
  ./qla_bench-qla-1.7.1-d3 2>&1
  ./qla_bench-qla-1.7.1-f3 2>&1
  exit 0
```

## Collection

 - Name: [spco/singularity-recipes](https://github.com/spco/singularity-recipes)
 - License: None

