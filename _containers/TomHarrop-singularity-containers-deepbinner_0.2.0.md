---
id: 7543
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "deepbinner_0.2.0"
commit: "278df3134ff1efdba41fa76fc5d7da5e1ccd014f"
version: "dfde6a30d653fa6c1b75326de3bef431"
build_date: "2019-03-01T09:51:05.606Z"
size_mb: 1767
size: 649572383
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/deepbinner_0.2.0/2019-03-01-278df313-dfde6a30/dfde6a30d653fa6c1b75326de3bef431.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/deepbinner_0.2.0/2019-03-01-278df313-dfde6a30/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/deepbinner_0.2.0/2019-03-01-278df313-dfde6a30/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:deepbinner_0.2.0

```bash
$ singularity pull shub://TomHarrop/singularity-containers:deepbinner_0.2.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.6.8-stretch

%help

    Deepbinner 0.2.0 319bae8
    
%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com) "
    VERSION "deepbinner 0.2.0 319bae8"

%runscript

    exec /usr/local/bin/deepbinner "$@"

%post

    apt-get update
    apt-get install -y \
        locales

    # install Deepbinner
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
    /usr/sbin/locale-gen

    export LANG=en_US.UTF-8  
    export LANGUAGE=en_US:en
    export LC_ALL=en_US.UTF-8     

    pip3 install \
        tensorflow \
        ont-fast5-api \
        git+git://github.com/rrwick/Deepbinner.git@319bae84bfb3b0f3ab279b70e9e0a886156414bf
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

