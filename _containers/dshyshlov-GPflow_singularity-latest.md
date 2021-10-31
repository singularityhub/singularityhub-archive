---
id: 2484
name: "dshyshlov/GPflow_singularity"
branch: "master"
tag: "latest"
commit: "40e37c06d25b1a3645f3ab11b8e39946391f03d0"
version: "39e5c86355f70d745125b13bdb9c60f5"
build_date: "2018-04-13T04:44:04.862Z"
size_mb: 1410
size: 467394591
sif: "https://datasets.datalad.org/shub/dshyshlov/GPflow_singularity/latest/2018-04-13-40e37c06-39e5c863/39e5c86355f70d745125b13bdb9c60f5.simg"
url: https://datasets.datalad.org/shub/dshyshlov/GPflow_singularity/latest/2018-04-13-40e37c06-39e5c863/
recipe: https://datasets.datalad.org/shub/dshyshlov/GPflow_singularity/latest/2018-04-13-40e37c06-39e5c863/Singularity
collection: dshyshlov/GPflow_singularity
---

# dshyshlov/GPflow_singularity:latest

```bash
$ singularity pull shub://dshyshlov/GPflow_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow

%post
    apt-get -y install git-core
    git clone https://github.com/GPflow/GPflow.git
    cd GPflow
    pip install .
```

## Collection

 - Name: [dshyshlov/GPflow_singularity](https://github.com/dshyshlov/GPflow_singularity)
 - License: None

