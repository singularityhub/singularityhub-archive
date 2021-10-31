---
id: 482
name: "qbicsoftware/qbic-singularity-pyenvcentraxx"
branch: "master"
tag: "v1.0"
commit: "029520d938fe990f3f267ef561f3b675201147b4"
version: "d791ecec56e98931d514041cb4813a07"
build_date: "2019-07-27T21:23:39.138Z"
size_mb: 436
size: 91791391
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-pyenvcentraxx/v1.0/2019-07-27-029520d9-d791ecec/d791ecec56e98931d514041cb4813a07.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-pyenvcentraxx/v1.0/2019-07-27-029520d9-d791ecec/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-pyenvcentraxx/v1.0/2019-07-27-029520d9-d791ecec/Singularity
collection: qbicsoftware/qbic-singularity-pyenvcentraxx
---

# qbicsoftware/qbic-singularity-pyenvcentraxx:v1.0

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-pyenvcentraxx:v1.0
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine:3.6

%post
/bin/sh build.sh

%files
build.sh

%runscript
    echo "Arguments received: $*"
    exec python2.7 "$@"

%environment
of your container
    PYENVCENTRAXX_VERSION=v1.0

%labels
Maintainer	sven.fillinger@qbic.uni-tuebingen.de

%test
    python2 --version
    pip -V
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-pyenvcentraxx](https://github.com/qbicsoftware/qbic-singularity-pyenvcentraxx)
 - License: None

