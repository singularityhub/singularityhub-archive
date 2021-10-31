---
id: 4890
name: "truatpasteurdotfr/singularity-docker-alpine-scl2spec"
branch: "master"
tag: "latest"
commit: "adae9b7792c471e988211db1ef7e34af172b805a"
version: "1945752e3bef0c0c0f5b2f279a38020c"
build_date: "2018-09-19T07:00:18.651Z"
size_mb: 72
size: 20680735
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-alpine-scl2spec/latest/2018-09-19-adae9b77-1945752e/1945752e3bef0c0c0f5b2f279a38020c.simg"
url: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-alpine-scl2spec/latest/2018-09-19-adae9b77-1945752e/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-alpine-scl2spec/latest/2018-09-19-adae9b77-1945752e/Singularity
collection: truatpasteurdotfr/singularity-docker-alpine-scl2spec
---

# truatpasteurdotfr/singularity-docker-alpine-scl2spec:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-docker-alpine-scl2spec:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: alpine

%runscript
echo "running scl2spec from the container:"
spec2scl "$@"

%post
echo "Hello from inside the container"
apk update
apk upgrade
apk add py3-pip  python3 
pip3 install --upgrade pip
pip3 install spec2scl

touch /singularity-`date +%Y%m%d-%H%M%S`

# specific to my setup, required if you don't have overlay support (CentOS-6)
# CentOS-7 host can ignore that mkdir line
mkdir -p /local-storage /mnt/beegfs /baycells/home /baycells/scratch /c6/shared /c6/eb /local/gensoft2 /c6/shared/rpm /Bis/Scratch2 /mnt/beegfs
```

## Collection

 - Name: [truatpasteurdotfr/singularity-docker-alpine-scl2spec](https://github.com/truatpasteurdotfr/singularity-docker-alpine-scl2spec)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

