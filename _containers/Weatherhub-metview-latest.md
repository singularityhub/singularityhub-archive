---
id: 2458
name: "Weatherhub/metview"
branch: "master"
tag: "latest"
commit: "74c2b9bc28673001fd02e00194e92c53a897fb62"
version: "15c68ec7b38e569509c3a3952b305f39"
build_date: "2018-04-16T12:51:45.118Z"
size_mb: 3121
size: 909873183
sif: "https://datasets.datalad.org/shub/Weatherhub/metview/latest/2018-04-16-74c2b9bc-15c68ec7/15c68ec7b38e569509c3a3952b305f39.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Weatherhub/metview/latest/2018-04-16-74c2b9bc-15c68ec7/
recipe: https://datasets.datalad.org/shub/Weatherhub/metview/latest/2018-04-16-74c2b9bc-15c68ec7/Singularity
collection: Weatherhub/metview
---

# Weatherhub/metview:latest

```bash
$ singularity pull shub://Weatherhub/metview:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: weatherhub/metview

%labels
MAINTAINER Xin Zhang
SPECIES JCSDA

%runscript
    echo "Welcome, this is Singularity container for METVIEW"

%environments
    DISPLAY=:0.0 \
    export DISPLAY

%post
    echo "Hello from inside the container"
    echo "Install additional software here"
```

## Collection

 - Name: [Weatherhub/metview](https://github.com/Weatherhub/metview)
 - License: None

