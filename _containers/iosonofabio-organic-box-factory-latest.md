---
id: 907
name: "iosonofabio/organic-box-factory"
branch: "stampy"
tag: "latest"
commit: "3c21aa5596448a4647e0e0396dba4768482a9002"
version: "3f7eb06ee09749c7e539963fe7ba13d0"
build_date: "2017-11-22T15:36:09.158Z"
size_mb: 778
size: 259346463
sif: "https://datasets.datalad.org/shub/iosonofabio/organic-box-factory/latest/2017-11-22-3c21aa55-3f7eb06e/3f7eb06ee09749c7e539963fe7ba13d0.simg"
url: https://datasets.datalad.org/shub/iosonofabio/organic-box-factory/latest/2017-11-22-3c21aa55-3f7eb06e/
recipe: https://datasets.datalad.org/shub/iosonofabio/organic-box-factory/latest/2017-11-22-3c21aa55-3f7eb06e/Singularity
collection: iosonofabio/organic-box-factory
---

# iosonofabio/organic-box-factory:latest

```bash
$ singularity pull shub://iosonofabio/organic-box-factory:latest
```

## Singularity Recipe

```singularity
# Fabio Zanini <fabio DOT zanini AT stanford DOT edu>
bootstrap:docker
From:finalduty/archlinux:latest

%setup
    cp configure_image.sh "$SINGULARITY_ROOTFS/configure_image.sh"
    #cp pipeline/pipeline.py "$SINGULARITY_ROOTFS/usr/bin/pipeline"

%post
    bash /configure_image.sh
    mkdir /mnt/singularity_bind

%runscript
    exec /opt/stampy-1.0.32/stampy.py "$@"
```

## Collection

 - Name: [iosonofabio/organic-box-factory](https://github.com/iosonofabio/organic-box-factory)
 - License: [MIT License](https://api.github.com/licenses/mit)

