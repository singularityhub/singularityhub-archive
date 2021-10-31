---
id: 6097
name: "LokiLuciferase/buchstabensuppe"
branch: "master"
tag: "latest"
commit: "21e86401d7ecca1f054c86cb5561891e907793a4"
version: "8172bc65e6fcda9813e6e0cf6b3ec833"
build_date: "2019-07-16T20:46:14.889Z"
size_mb: 2391
size: 755355679
sif: "https://datasets.datalad.org/shub/LokiLuciferase/buchstabensuppe/latest/2019-07-16-21e86401-8172bc65/8172bc65e6fcda9813e6e0cf6b3ec833.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/LokiLuciferase/buchstabensuppe/latest/2019-07-16-21e86401-8172bc65/
recipe: https://datasets.datalad.org/shub/LokiLuciferase/buchstabensuppe/latest/2019-07-16-21e86401-8172bc65/Singularity
collection: LokiLuciferase/buchstabensuppe
---

# LokiLuciferase/buchstabensuppe:latest

```bash
$ singularity pull shub://LokiLuciferase/buchstabensuppe:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest

%help
    This container encapsulates the annotation,
    text mining, model creation and prediction tools
    of the Buchstabensuppe pipeline.
    Please run this container with the external Buchstabensuppe data folder attached via the Bind (-B) command:

    singularity run -B <path to data folder>:/data <container name> <arguments>

    For a list of all available subcommands,
    please issue:

        singularity run -B <path to data folder>:/data <container name> --help

%files
    . /app

%post
    bash /app/container_install.sh

%environment
    PATH=/opt/conda/bin:$PATH
    PYTHONPATH=/app
    QT_QPA_PLATFORM=offscreen

    export PATH
    export PYTHONPATH
    export QT_QPA_PLATFORM

%runscript
    exec bs "$@"
```

## Collection

 - Name: [LokiLuciferase/buchstabensuppe](https://github.com/LokiLuciferase/buchstabensuppe)
 - License: None

