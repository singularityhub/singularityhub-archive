---
id: 405
name: "truatpasteurdotfr/singularity-docker-alpine-roca"
branch: "master"
tag: "latest"
commit: "18e9b7e99e3bbd2d133ff54e16ce894f21cdc21d"
version: "24b1501dee0060f9f16dfba7658c6f55"
build_date: "2020-12-11T19:20:58.563Z"
size_mb: 375
size: 72552479
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-alpine-roca/latest/2020-12-11-18e9b7e9-24b1501d/24b1501dee0060f9f16dfba7658c6f55.simg"
url: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-alpine-roca/latest/2020-12-11-18e9b7e9-24b1501d/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-alpine-roca/latest/2020-12-11-18e9b7e9-24b1501d/Singularity
collection: truatpasteurdotfr/singularity-docker-alpine-roca
---

# truatpasteurdotfr/singularity-docker-alpine-roca:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-docker-alpine-roca:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: alpine:3.6
# more details at https://keychest.net/roca and https://github.com/crocs-muni/roca 

%runscript
echo "running roca-detect from the container:"
roca-detect "$@"

%post
echo "Hello from inside the container"
apk update
apk upgrade
apk add py2-pip python-dev python libressl-dev libffi-dev swig gcc musl-dev
pip install roca-detect

touch /singularity-`date +%Y%m%d-%H%M%S`

# specific to my setup, required if you don't have overlay support (CentOS-6)
# CentOS-7 host can ignore that mkdir line
mkdir -p /local-storage /mnt/beegfs /baycells/home /baycells/scratch /c6/shared /c6/eb /local/gensoft2 /c6/shared/rpm /Bis/Scratch2 /mnt/beegfs
```

## Collection

 - Name: [truatpasteurdotfr/singularity-docker-alpine-roca](https://github.com/truatpasteurdotfr/singularity-docker-alpine-roca)
 - License: None

