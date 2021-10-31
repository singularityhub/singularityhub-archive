---
id: 7355
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "pigz_2.4.0"
commit: "e1c830e52f82f32c66674064277845d4c083ab8e"
version: "63652a494e5b17ab67cce88205d737b5"
build_date: "2019-12-19T01:39:28.458Z"
size_mb: 17
size: 5169183
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/pigz_2.4.0/2019-12-19-e1c830e5-63652a49/63652a494e5b17ab67cce88205d737b5.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/pigz_2.4.0/2019-12-19-e1c830e5-63652a49/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/pigz_2.4.0/2019-12-19-e1c830e5-63652a49/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:pigz_2.4.0

```bash
$ singularity pull shub://TomHarrop/singularity-containers:pigz_2.4.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.9

%help

    Container for pigz 2.4.0

%labels

    VERSION "pigz 2.4.0"


%post

    apk add --update bash pigz

%runscript
    exec /usr/bin/pigz "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

