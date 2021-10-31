---
id: 8302
name: "recap/udt-singularity"
branch: "master"
tag: "latest"
commit: "b93f3373f908d17a4f28cdf0fc8d2c28835eff5f"
version: "943c7d3a499dfaa58b102e13dd5ea245"
build_date: "2020-01-13T13:21:31.958Z"
size_mb: 418
size: 162246687
sif: "https://datasets.datalad.org/shub/recap/udt-singularity/latest/2020-01-13-b93f3373-943c7d3a/943c7d3a499dfaa58b102e13dd5ea245.simg"
url: https://datasets.datalad.org/shub/recap/udt-singularity/latest/2020-01-13-b93f3373-943c7d3a/
recipe: https://datasets.datalad.org/shub/recap/udt-singularity/latest/2020-01-13-b93f3373-943c7d3a/Singularity
collection: recap/udt-singularity
---

# recap/udt-singularity:latest

```bash
$ singularity pull shub://recap/udt-singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04
%label
	Author R.S.Cushing@uva.nl
	Version v0.0.1
%setup
   # commands to be executed on host outside container during bootstrap
%test
   # commands to be executed within container at close of bootstrap process
%environment
   LD_LIBRARY_PATH=/udt-git/udt4/src:$LD_LIBRARY_PATH
   PATH=/udt-git/udt4/app:$PATH
%runscript
   # commands to be executed when the container runs
   echo "LD_LIBRARY_PATH: $LD_LIBRARY_PATH"
   echo "PATH: $PATH"
   echo "Arguments received: $*"
   exec "$@"
%post
   # commands to be executed inside container during bootstrap
   apt-get update && apt-get install -y \
        build-essential \
        cmake \
        git 
   git clone https://git.code.sf.net/p/udt/git udt-git
   cd udt-git/udt4
   make arch=AMD64
```

## Collection

 - Name: [recap/udt-singularity](https://github.com/recap/udt-singularity)
 - License: None

