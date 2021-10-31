---
id: 11700
name: "aminHatim/mt-dnn"
branch: "master"
tag: "latest"
commit: "26fe5c40e473ee0c77497a4755ad8c30abf2b8ef"
version: "f1a239e1f9ce4e01eef074f593885ee5"
build_date: "2019-11-26T21:08:12.870Z"
size_mb: 7016.0
size: 4158705695
sif: "https://datasets.datalad.org/shub/aminHatim/mt-dnn/latest/2019-11-26-26fe5c40-f1a239e1/f1a239e1f9ce4e01eef074f593885ee5.sif"
url: https://datasets.datalad.org/shub/aminHatim/mt-dnn/latest/2019-11-26-26fe5c40-f1a239e1/
recipe: https://datasets.datalad.org/shub/aminHatim/mt-dnn/latest/2019-11-26-26fe5c40-f1a239e1/Singularity
collection: aminHatim/mt-dnn
---

# aminHatim/mt-dnn:latest

```bash
$ singularity pull shub://aminHatim/mt-dnn:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: aminehatim/mtdnn:1

%help

Singularity container 

%setup
	mkdir -p  ${SINGULARITY_ROOTFS}/app

%labels
	Maintainer Amine Elhattami
	Version v0.1

%environment
	export PATH=$PATH:/opt/conda/bin
	export COMET_API_KEY=3bWALr0COnbG1firKqDUzCrbi

%runscript
        exec /bin/bash "$@"
```

## Collection

 - Name: [aminHatim/mt-dnn](https://github.com/aminHatim/mt-dnn)
 - License: [MIT License](https://api.github.com/licenses/mit)

