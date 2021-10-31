---
id: 2660
name: "spco/singularity-recipes"
branch: "master"
tag: "milc-gcc"
commit: "5db066f23d5889befa8c568e08ff73d43943a4dd"
version: "baf70683099cd22c40a7e6d916055ff9"
build_date: "2018-04-26T16:28:57.015Z"
size_mb: 494
size: 169058335
sif: "https://datasets.datalad.org/shub/spco/singularity-recipes/milc-gcc/2018-04-26-5db066f2-baf70683/baf70683099cd22c40a7e6d916055ff9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/spco/singularity-recipes/milc-gcc/2018-04-26-5db066f2-baf70683/
recipe: https://datasets.datalad.org/shub/spco/singularity-recipes/milc-gcc/2018-04-26-5db066f2-baf70683/Singularity
collection: spco/singularity-recipes
---

# spco/singularity-recipes:milc-gcc

```bash
$ singularity pull shub://spco/singularity-recipes:milc-gcc
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/

Include: yum

%help
  echo "This is a container to run MILC on CentOS compiled at build time under GCC."


%post
  yum install -y tar wget bzip2 make gcc gcc-c++
  wget https://asc.llnl.gov/CORAL-benchmarks/Micro/MILCmk-v1.tar.bz2
  tar xjf MILCmk-v1.tar.bz2
  cd MILCmk-v1/
  sed -i '1s/.*/CC = gcc/' Makefile
  sed -i '3s/.*/COPT = -O3 -mavx2/' Makefile
  sed -i '4s/.*/OMP = -fopenmp/' Makefile
  sed -i '8s/.*/CFLAGSA = -lm -std=c99/' Makefile
  make
  chmod -R 777 /MILCmk-v1
  exit 0

%runscript
  echo "run MILC"
  cd /MILCmk-v1
  export OMP_NUM_THREADS=16
  ./qla_bench-qla-1.7.1-d3
  ./qla_bench-qla-1.7.1-f3
  exit 0
```

## Collection

 - Name: [spco/singularity-recipes](https://github.com/spco/singularity-recipes)
 - License: None

