---
id: 5980
name: "LokiLuciferase/data-science-container"
branch: "master"
tag: "latest"
commit: "b7b79f9bf07d901855654a1bd18904cf5cfb2aeb"
version: "15660dbe115c87080af6ed0a4d2392b7"
build_date: "2018-12-16T10:26:35.646Z"
size_mb: 4093
size: 1303982111
sif: "https://datasets.datalad.org/shub/LokiLuciferase/data-science-container/latest/2018-12-16-b7b79f9b-15660dbe/15660dbe115c87080af6ed0a4d2392b7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/LokiLuciferase/data-science-container/latest/2018-12-16-b7b79f9b-15660dbe/
recipe: https://datasets.datalad.org/shub/LokiLuciferase/data-science-container/latest/2018-12-16-b7b79f9b-15660dbe/Singularity
collection: LokiLuciferase/data-science-container
---

# LokiLuciferase/data-science-container:latest

```bash
$ singularity pull shub://LokiLuciferase/data-science-container:latest
```

## Singularity Recipe

```singularity
From:continuumio/anaconda3:5.3.0
Bootstrap:docker

%labels
    MAINTAINER Lukas Lueftinger <lukas.lueftinger@imp.ac.at>
    DESCRIPTION Data Science Dev Environment, Anaconda3-based
    VERSION 0.1.1

%files
    . /install

%post
    /bin/bash /install/install.sh

%environment
    PATH=/opt/conda/bin:$PATH
    QT_QPA_PLATFORM=offscreen
    export PATH
    export QT_QPA_PLATFORM

%runscript
    exec /opt/conda/bin/jupyter lab --port 8888 --no-browser
```

## Collection

 - Name: [LokiLuciferase/data-science-container](https://github.com/LokiLuciferase/data-science-container)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

