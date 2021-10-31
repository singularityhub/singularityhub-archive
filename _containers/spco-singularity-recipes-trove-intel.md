---
id: 2670
name: "spco/singularity-recipes"
branch: "master"
tag: "trove-intel"
commit: "4c2ee12da4f9e29c2f53c45c208c688bdca0337a"
version: "61532578442ac53881eacdb0baa75dd1"
build_date: "2018-04-27T11:43:12.078Z"
size_mb: 647
size: 252117023
sif: "https://datasets.datalad.org/shub/spco/singularity-recipes/trove-intel/2018-04-27-4c2ee12d-61532578/61532578442ac53881eacdb0baa75dd1.simg"
url: https://datasets.datalad.org/shub/spco/singularity-recipes/trove-intel/2018-04-27-4c2ee12d-61532578/
recipe: https://datasets.datalad.org/shub/spco/singularity-recipes/trove-intel/2018-04-27-4c2ee12d-61532578/Singularity
collection: spco/singularity-recipes
---

# spco/singularity-recipes:trove-intel

```bash
$ singularity pull shub://spco/singularity-recipes:trove-intel
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/

Include: yum

%help
  echo "This is a container to run TROVE on CentOS compiled under Intel. This uses pre-compiled binaries from ALICE2, stored on www1 at Leicester. There is a version of the executable compiled for each of SSE4_2, AVX and AVX2."

%post
  mkdir -p /TROVE/
  yum install -y wget tar gzip gunzip
  cd /TROVE
  wget https://www1.lamp.le.ac.uk/compiled_trove.tar.gz
  tar zxf compiled_trove.tar.gz
  chmod -R 777 /TROVE
  exit 0

%runscript
  cd /TROVE
  pwd
  ls
  mkdir OUT
  export OMP_NUM_THREADS=16
  ./run_trove.sh
  ./run_trove_numa.sh
  exit 0
```

## Collection

 - Name: [spco/singularity-recipes](https://github.com/spco/singularity-recipes)
 - License: None

