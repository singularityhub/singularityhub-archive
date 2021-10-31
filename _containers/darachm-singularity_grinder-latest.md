---
id: 6121
name: "darachm/singularity_grinder"
branch: "master"
tag: "latest"
commit: "11c7c5b50d8eebbdc815b5f63db3c3c364cfa5e5"
version: "3c506498cf5a6a78dd334d52f348adc0"
build_date: "2019-01-04T07:48:36.779Z"
size_mb: 1140
size: 337907743
sif: "https://datasets.datalad.org/shub/darachm/singularity_grinder/latest/2019-01-04-11c7c5b5-3c506498/3c506498cf5a6a78dd334d52f348adc0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/darachm/singularity_grinder/latest/2019-01-04-11c7c5b5-3c506498/
recipe: https://datasets.datalad.org/shub/darachm/singularity_grinder/latest/2019-01-04-11c7c5b5-3c506498/Singularity
collection: darachm/singularity_grinder
---

# darachm/singularity_grinder:latest

```bash
$ singularity pull shub://darachm/singularity_grinder:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
MAINTAINER darachm

%help

    This container is for providing `grinder` for some bioinformatic pipelines.
    
%post

    apt-get -y update
    apt-get -y install grinder

%test

    # ?
```

## Collection

 - Name: [darachm/singularity_grinder](https://github.com/darachm/singularity_grinder)
 - License: None

