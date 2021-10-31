---
id: 407
name: "truatpasteurdotfr/singularity-alpine-pdftk"
branch: "master"
tag: "latest"
commit: "0d0225408ca558f324f36d6d34c3f0dcd5da1e74"
version: "edd4a226bfafa36fa70dc328c90e1a45"
build_date: "2017-10-19T20:34:17.736Z"
size_mb: 254
size: 30339103
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-alpine-pdftk/latest/2017-10-19-0d022540-edd4a226/edd4a226bfafa36fa70dc328c90e1a45.simg"
url: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-alpine-pdftk/latest/2017-10-19-0d022540-edd4a226/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-alpine-pdftk/latest/2017-10-19-0d022540-edd4a226/Singularity
collection: truatpasteurdotfr/singularity-alpine-pdftk
---

# truatpasteurdotfr/singularity-alpine-pdftk:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-alpine-pdftk:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: alpine:latest

%runscript
echo "running pdftk from the container:"
pdftk "$@"

%post
echo "Hello from inside the container"
apk update
apk upgrade
apk add pdftk
touch /singularity-`date +%Y%m%d-%H%M%S`

%labels
MAINTAINER truatpasteurdotfr
```

## Collection

 - Name: [truatpasteurdotfr/singularity-alpine-pdftk](https://github.com/truatpasteurdotfr/singularity-alpine-pdftk)
 - License: None

