---
id: 393
name: "GodloveD/busybox"
branch: "master"
tag: "latest"
commit: "295af805d481e99e590820e7dedc3f8a26ff8e8d"
version: "ec0f4b513a15b6673b19c16a90b247d3"
build_date: "2020-11-11T17:09:07.019Z"
size_mb: 176
size: 618527
sif: "https://datasets.datalad.org/shub/GodloveD/busybox/latest/2020-11-11-295af805-ec0f4b51/ec0f4b513a15b6673b19c16a90b247d3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/GodloveD/busybox/latest/2020-11-11-295af805-ec0f4b51/
recipe: https://datasets.datalad.org/shub/GodloveD/busybox/latest/2020-11-11-295af805-ec0f4b51/Singularity
collection: GodloveD/busybox
---

# GodloveD/busybox:latest

```bash
$ singularity pull shub://GodloveD/busybox:latest
```

## Singularity Recipe

```singularity
BootStrap: busybox
MirrorURL: https://www.busybox.net/downloads/binaries/1.26.1-defconfig-multiarch/busybox-x86_64

%post
    echo "Hello from inside the container"

%runscript
    echo "Running command: $*"
    exec "$@"
```

## Collection

 - Name: [GodloveD/busybox](https://github.com/GodloveD/busybox)
 - License: None

