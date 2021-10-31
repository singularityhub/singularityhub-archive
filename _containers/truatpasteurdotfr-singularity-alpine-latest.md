---
id: 404
name: "truatpasteurdotfr/singularity-alpine"
branch: "master"
tag: "latest"
commit: "12c84e093194d895ff2dbf4fb9257e2926bbf1d7"
version: "bc6bb8a73d483b47ea07c94081e40d49"
build_date: "2020-11-26T08:10:10.625Z"
size_mb: 180
size: 3035167
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-alpine/latest/2020-11-26-12c84e09-bc6bb8a7/bc6bb8a73d483b47ea07c94081e40d49.simg"
url: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-alpine/latest/2020-11-26-12c84e09-bc6bb8a7/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-alpine/latest/2020-11-26-12c84e09-bc6bb8a7/Singularity
collection: truatpasteurdotfr/singularity-alpine
---

# truatpasteurdotfr/singularity-alpine:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-alpine:latest
```

## Singularity Recipe

```singularity
#!/bin/bash
# 
# Tru Huynh <tru@pasteur.fr>
# 2017/06/07: initial version

BootStrap: docker
From: alpine:latest

%runscript
echo "This is what happens when you run the container..."
/bin/sh

%post
echo "Hello from inside the container"
apk update && apk upgrade
touch /`date -u -Iseconds`

# tars.pasteur.fr specific (no overlays on CentOS-6)
mkdir -p /pasteur/{homes,scratch,entites} /local/{scratch,flash} /mount/gensoft2 

%labels
MAINTAINER truatpasteurdotfr
```

## Collection

 - Name: [truatpasteurdotfr/singularity-alpine](https://github.com/truatpasteurdotfr/singularity-alpine)
 - License: [MIT License](https://api.github.com/licenses/mit)

