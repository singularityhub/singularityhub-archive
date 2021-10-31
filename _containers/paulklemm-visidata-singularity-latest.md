---
id: 5798
name: "paulklemm/visidata-singularity"
branch: "master"
tag: "latest"
commit: "747b4b344c7ee6b6c09cc333578889e583616aee"
version: "0c27f198049f708dae86d870b457d494"
build_date: "2018-12-17T16:03:53.034Z"
size_mb: 769
size: 306876447
sif: "https://datasets.datalad.org/shub/paulklemm/visidata-singularity/latest/2018-12-17-747b4b34-0c27f198/0c27f198049f708dae86d870b457d494.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/paulklemm/visidata-singularity/latest/2018-12-17-747b4b34-0c27f198/
recipe: https://datasets.datalad.org/shub/paulklemm/visidata-singularity/latest/2018-12-17-747b4b34-0c27f198/Singularity
collection: paulklemm/visidata-singularity
---

# paulklemm/visidata-singularity:latest

```bash
$ singularity pull shub://paulklemm/visidata-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:stretch

%post
    apt-get -y update
    apt-get -y install less python3-pip man
    pip3 install PyYAML pypng requests psycopg2 openpyxl xlrd h5py fonttools mapbox lxml xport sas7bdat pandas pyshp python-dateutil visidata

%runscript
    vd
```

## Collection

 - Name: [paulklemm/visidata-singularity](https://github.com/paulklemm/visidata-singularity)
 - License: None

