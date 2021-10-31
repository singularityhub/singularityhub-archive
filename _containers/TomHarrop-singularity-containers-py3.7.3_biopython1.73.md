---
id: 8752
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "py3.7.3_biopython1.73"
commit: "368c865905bac2d760a5f395a488540b93ae3e40"
version: "9281d838c5984dd35f671bf99a3f2885"
build_date: "2019-05-02T20:56:07.752Z"
size_mb: 625
size: 253968415
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/py3.7.3_biopython1.73/2019-05-02-368c8659-9281d838/9281d838c5984dd35f671bf99a3f2885.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/py3.7.3_biopython1.73/2019-05-02-368c8659-9281d838/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/py3.7.3_biopython1.73/2019-05-02-368c8659-9281d838/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:py3.7.3_biopython1.73

```bash
$ singularity pull shub://TomHarrop/singularity-containers:py3.7.3_biopython1.73
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.04

%help
    Container for testing biopython index_db()
    https://github.com/tomharrop/racon-chunks

    Python 3.7.3 with biopython 1.73

%labels
    MAINTAINER "Tom Harrop"

%runscript
    exec /usr/bin/python3 "$@"

%post
    # dependencies
    apt-get update
    apt-get install -y \
        python3-pip

    # python + biopython
    /usr/bin/pip3 install --upgrade pip
    /usr/local/bin/pip3 install \
        biopython==1.73
    update-alternatives \
        --install /usr/bin/python \
        python \
        /usr/bin/python3 \
        1
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

