---
id: 8450
name: "recap/http-singularity"
branch: "master"
tag: "latest"
commit: "2b091d50cd41cef9dc6f3dd2346331def155aed8"
version: "7cb8647fc2afb095991ce1751617b86e"
build_date: "2020-01-13T13:04:22.928Z"
size_mb: 157
size: 66678815
sif: "https://datasets.datalad.org/shub/recap/http-singularity/latest/2020-01-13-2b091d50-7cb8647f/7cb8647fc2afb095991ce1751617b86e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/recap/http-singularity/latest/2020-01-13-2b091d50-7cb8647f/
recipe: https://datasets.datalad.org/shub/recap/http-singularity/latest/2020-01-13-2b091d50-7cb8647f/Singularity
collection: recap/http-singularity
---

# recap/http-singularity:latest

```bash
$ singularity pull shub://recap/http-singularity:latest
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
%runscript
   # commands to be executed when the container runs
   echo "LD_LIBRARY_PATH: $LD_LIBRARY_PATH"
   echo "PATH: $PATH"
   echo "Arguments received: $*"
   exec "$@"
%post
   # commands to be executed inside container during bootstrap
   apt-get update && apt-get install -y python wget
```

## Collection

 - Name: [recap/http-singularity](https://github.com/recap/http-singularity)
 - License: None

