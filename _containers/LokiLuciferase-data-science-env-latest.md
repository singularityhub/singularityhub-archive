---
id: 6672
name: "LokiLuciferase/data-science-env"
branch: "master"
tag: "latest"
commit: "663ce0cbd04082da85ec79a4d66fd7faefdcdff6"
version: "3ad50d2d45890e254052b0d616df3bb6"
build_date: "2019-02-11T09:36:54.817Z"
size_mb: 3148
size: 901984287
sif: "https://datasets.datalad.org/shub/LokiLuciferase/data-science-env/latest/2019-02-11-663ce0cb-3ad50d2d/3ad50d2d45890e254052b0d616df3bb6.simg"
url: https://datasets.datalad.org/shub/LokiLuciferase/data-science-env/latest/2019-02-11-663ce0cb-3ad50d2d/
recipe: https://datasets.datalad.org/shub/LokiLuciferase/data-science-env/latest/2019-02-11-663ce0cb-3ad50d2d/Singularity
collection: LokiLuciferase/data-science-env
---

# LokiLuciferase/data-science-env:latest

```bash
$ singularity pull shub://LokiLuciferase/data-science-env:latest
```

## Singularity Recipe

```singularity
From:continuumio/miniconda3
Bootstrap:docker

%labels
    MAINTAINER Lukas Lueftinger <lukas.lueftinger@imp.ac.at>
    DESCRIPTION Data Science Dev Environment, Miniconda3-based
    VERSION 0.2

%files
    . /install

%post
    /bin/bash /install/install_container.sh

%environment
    PATH=/opt/conda/bin:$PATH
    QT_QPA_PLATFORM=offscreen
    export PATH
    export QT_QPA_PLATFORM

%runscript
    exec /opt/conda/bin/jupyter lab --port 8888 --no-browser
```

## Collection

 - Name: [LokiLuciferase/data-science-env](https://github.com/LokiLuciferase/data-science-env)
 - License: None

