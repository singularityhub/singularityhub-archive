---
id: 3826
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "salmon_0.11.1"
commit: "bdb01c1da8c4cf082e99c40bd472e87609c1a5e9"
version: "142467036cee071f53ea3e258dd2e3fb"
build_date: "2020-11-17T02:31:01.655Z"
size_mb: 1180
size: 350535711
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/salmon_0.11.1/2020-11-17-bdb01c1d-14246703/142467036cee071f53ea3e258dd2e3fb.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/salmon_0.11.1/2020-11-17-bdb01c1d-14246703/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/salmon_0.11.1/2020-11-17-bdb01c1d-14246703/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:salmon_0.11.1

```bash
$ singularity pull shub://TomHarrop/singularity-containers:salmon_0.11.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: combinelab/salmon:0.11.1

%help

    Salmon 0.11.1
    https://github.com/COMBINE-lab/salmon/releases

%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "salmon 0.11.1"

%runscript

    exec /usr/local/bin/salmon "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

